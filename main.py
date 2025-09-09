from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()
model = pipeline("text-generation", model="tiiuae/falcon-7b-instruct")

class textgenerationRequest(BaseModel):
    prompt: str
    max_length: int = 1000
    
@app.post("/generate_text")
async def generate_text(request: textgenerationRequest):
    try:
        result = model(request.prompt, max_length=request.max_length, num_return_sequences=1)
        print(result)
        return {"generated_text": result[0]['generated_text']}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return {"message": "Hello World"}