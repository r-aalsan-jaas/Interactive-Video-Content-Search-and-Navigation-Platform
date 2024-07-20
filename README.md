# Interactive-Video-Content-Search-and-Navigation-Platform

An effective web tool called Interactive-Video-Content-Search-and-Navigation-Platform is made to unlock the mysteries contained in YouTube videos. Using AI technology, you may easily find insights and comprehend your favorite video content with Interactive-Video-Content-Search-and-Navigation-Platform. It leverages the OpenAI API [Embeddings](https://platform.openai.com/docs/api-reference/embeddings) and [Chat Completion](https://platform.openai.com/docs/api-reference/completions) endpoints to generate AI assistant responses. It builds an LLM (Large Language Model)-enabled data pipeline in Python and joins data from multiple input sources.



## Features

- **Simplify Complexity:** The Interactive-Video-Content-Search-and-Navigation-Platform uses the most recent developments in artificial intelligence to condense long YouTube videos into brief synopses, making complicated content simple to understand.
  
- **Uncover Insights:** Inquire directly about the substance of your videos to delve deeper into the subject. The AI-powered question-answering system on Interactive-Video-Content-Search-and-Navigation-Platform delivers precise and pertinent answers.
  

- **User-Friendly Interface:** You may engage with the app and gain useful insights with ease thanks to our user-friendly interface, which guarantees smooth navigation.


  

## Installation
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/r-aalsan-jaas/Interactive-Video-Content-Search-and-Navigation-Platform.git
    ```
    
2. **Create a conda environment using environment.yml file:**
3. **Create a .env file with following content**
   ```bash
    HOST = 0.0.0.0
    PORT = 8080
    EMBEDDER_LOCATOR=text-embedding-ada-002
    MODEL_LOCATOR=gpt-3.5-turbo
    MAX_TOKENS=200
    TEMPERATURE=0.0
    LOCAL_FOLDER_PATH= {YOUR_FOLDER_PATH}
    EMBEDDING_DIMENSION=1536
    OPENAI_API_TOKEN = {YOUR_API_TOKEN}
    ```
4. **Run the following commands**
   ```bash
   pip install llm_app pathway
    ```

## Usage

1. **Run the main.py file**
    ```bash
    python main.py
    ```
    
2. **Run the Streamlit App:**
    ```bash
    streamlit run streamlit_app/ui.py
    ```
    
3. **Add YouTube Video Links:**
    To explore the YouTube videos, just copy and paste their URLs into the designated text field.
  
4. **Initiate Summarization:**
    To begin the Interactive-Video-Content-Search-and-Navigation-Platform's AI engine synthesising your videos into comprehensible insights, click the "Upload" button.
  
5. **Ask Questions:**
    You can go more into the video material by using the app to ask questions. The AI of the Interactive-Video-Content-Search-and-Navigation-Platform is prepared to offer precise and perceptive responses.

## Contributing

To further improve the capabilities of the Interactive-Video-Content-Search-and-Navigation-Platform, we invite community contributions. Your contributions are important, whether they be in the form of bug fixes, new features, or enhanced user interface. Please do not hesitate to provide a pull request or file an issue.



