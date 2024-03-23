import requests
from langchain.llms import Ollama

search_tool = SerperDevTool()

NGROK_TUNNEL_URL = "<your-ngrok-tunnel-url>" 
MODEL = "<model-name>" # e.g. "llama2"

def pull_model():
    headers = {"Content-Type": "application/json"}
    endpoint_pull = "/api/pull"
    url = NGROK_TUNNEL_URL + endpoint_pull
    payload = {"name": MODEL}

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print("Request successful:")
            print(response.text)
            return True
        else:
            print("Error:", response.status_code, response.text)
            return False
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return False

if __name__ == "__main__":
    model_pulled = pull_model()

    if model_pulled: 
        llm = Ollama(base_url=NGROK_TUNNEL_URL, model=MODEL)
