# Colab Ollama

Utilize Google Colab GPU to run Ollama models.

## 1. Install Ollama on your computer

[https://ollama.com/download](https://ollama.com/download)

## 2. Make ngrok account and generate a token.

[https://ngrok.com/](https://ngrok.com/)

## 3. Upload colab_ollama.ipynb to your Google Drive

Add ngrok token to the notebook.

Run the notebook and copy the ngrok tunnel URL. 

## 4. Connect to ngrok tunnel locally.

Paste the ngrok tunnel URL to client.py

Replace the model name you want to use.

Then use Langchain Ollama class to seamlessly use inference.


