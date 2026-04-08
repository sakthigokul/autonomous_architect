from fastapi import FastAPI
from agents import manager_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Autonomous Data Quality Agent Running"}

from pydantic import BaseModel

class Request(BaseModel):
    input_text: str

@app.post("/analyze")
def analyze(request: Request):
    result = manager_agent(request.input_text)
    return {"result": result}