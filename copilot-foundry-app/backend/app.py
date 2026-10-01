
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
client = OpenAI(base_url=os.getenv('FOUNDRY_ENDPOINT'), api_key=os.getenv('FOUNDRY_KEY'))
DEPLOYMENT_NAME = os.getenv('DEPLOYMENT_NAME')
class ChatRequest(BaseModel):
    message: str
@app.post('/chat')
async def chat(req: ChatRequest):
    response = client.responses.create(model=DEPLOYMENT_NAME, input=req.message)
    return {'response': response.output_text}
