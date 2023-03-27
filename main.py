import os

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str
    to: str
    from_: str
    timeToLifeSec: int

@app.post("/DevOps")
async def send_message(message: Message, x_parse_rest_api_key: str = Header(None), x_jwt_key: str = Header(None)):
    if x_parse_rest_api_key != os.environ['API_KEY']:
        return "ERROR: Invalid API Key"
    if message.from_ == "":
        message.from_ = message.sender
        message.sender = ""
        return "WARNING: 'sender' field should be named 'from_'. 'sender' will be treated as an empty field and from_ will be set to 'sender' value."
        
    return {"message": f"Hello {message.to}, your message will be sent."}
