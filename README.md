 LangChain Simple Chatbot

This repository contains a simple chatbot implementation using Streamlit and LangChain. The chatbot takes a user input question and provides a response using a language model.

 Features

- Simple chatbot interface built with Streamlit
- Uses LangChain for prompt templating and response parsing
- Utilizes the Ollama language model for generating responses

 Prerequisites

- Python 3.7 or higher
- Streamlit
- LangChain
- LangChain Community
- Ollama

 Installation

  Clone the repository:

   ```bash
   git clone https://github.com/yourusername/langchain-simple-chatbot.git
   cd langchain-simple-chatbot

  pip install streamlit langchain langchain_community ollama
  pip install streamlit langchain langchain_community ollama
  export LANGCHAIN_API_KEY="your_langchain_api_key"
  export LANGCHAIN_TRACING_V2="True"


   Usage
Run the Streamlit application:

bash
Copy code
streamlit run app.py
Open your web browser and navigate to http://localhost:8501. You should see the LangChain Simple Chatbot interface.

Enter a topic in the text input field and press Enter. The chatbot will generate a response based on your input.

Code
Here's a brief overview of the main components in the code:

Imports and environment setup: Necessary libraries and environment variables are imported and set.
Prompt template: A template for the chatbot's responses is defined using LangChain's ChatPromptTemplate.
Streamlit interface: The Streamlit interface is created with a title and a text input field.
Language model and output parser: The Ollama language model and a string output parser are defined.
Chain and invocation: The prompt template, language model, and output parser are chained together. If there's input text, the chain is invoked and the response is displayed.



