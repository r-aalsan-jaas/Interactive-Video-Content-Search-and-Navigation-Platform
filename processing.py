import unicodedata
import pathway as pw

CHARS_PER_TOKEN = 3
PUNCTUATION = [".", "?", "!", "\n"]

@pw.udf
def chunk_texts(
    texts: str | list[str],
    min_tokens: int = 50,
    max_tokens: int = 500,
    encoding_name: str = "cl100k_base",
) -> list[str]:
    
    import tiktoken

    if not isinstance(texts, str):
        texts = "\n".join(texts)

    tokenizer = tiktoken.get_encoding(encoding_name)
    text: str = texts
    text = normalize_unicode(text)
    tokens = tokenizer.encode_ordinary(text)
    output = []
    i = 0
    while i < len(tokens):
        chunk_tokens = tokens[i : i + max_tokens]
        chunk = tokenizer.decode(chunk_tokens)
        last_punctuation = max([chunk.rfind(p) for p in PUNCTUATION], default=-1)
        if last_punctuation != -1 and last_punctuation > CHARS_PER_TOKEN * min_tokens:
            chunk = chunk[: last_punctuation + 1]

        i += len(tokenizer.encode_ordinary(chunk))

        output.append(chunk)
    return output


def normalize_unicode(text: str):
    """
    Get rid of ligatures
    """
    return unicodedata.normalize("NFKC", text)
