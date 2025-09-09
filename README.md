🚀 FastAPI + Falcon-7B Text Generation API 🦅✨

Welcome to the AI Playground, where FastAPI meets Falcon-7B-Instruct and creates a text-generation tool called:

"The REST API that spits out text like there’s no tomorrow."

⚡ What is this?

This repo is a FastAPI server that wraps the Falcon-7B-Instruct LLM (via Hugging Face Transformers).
You send it a prompt 👉 it sends you back pure AI-powered madness (aka generated text).

🎯 Features

✅ Text generation endpoint

✅ JSON-based requests (because we’re civilized)

✅ Swagger docs auto-magically created at /docs

✅ Plug & Play → run locally or deploy anywhere

✅ Powered by Falcon-7B-Instruct 🦅 (big brain energy)

🔥 Endpoints
POST /generate_text

Request body:

{
  "prompt": "Once upon a time in a land of AI...",
  "max_length": 2000
}


Response:

{
  "generated_text": "Once upon a time... the Falcon spread its wings and..."
}

GET /

Just a boring health check:

{"message": "Hello World"}

🛠️ How to Run Locally

Clone it, install stuff, run it. Easy.

# Clone repo
git clone https://github.com/YOUR-USERNAME/fastapi-falcon-textgen.git
cd fastapi-falcon-textgen

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload --host 0.0.0.0 --port 8000


Now go to 👉 http://127.0.0.1:8000/docs

🤯 Warning

Falcon-7B is chonky. It eats VRAM for breakfast. 🥞

If your machine explodes 💥 … don’t blame me.

Recommended: Run on a GPU machine or Hugging Face Spaces.

🐒 Example Curl Command
curl -X POST "http://127.0.0.1:8000/generate_text" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Tell me a joke about AI", "max_length": 100}'

