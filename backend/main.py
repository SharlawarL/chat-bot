from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Chat bot API",
    description="This is a simple API built with FastAPI.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or ["*"] for all origins
    allow_credentials=True,
    allow_methods=["*"],                      # Allow all methods including OPTIONS
    allow_headers=["*"],                      # Allow all headers
)

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

# Session memory (in real app, use database or session ID)
chat_history_ids = None

class Message(BaseModel):
    message: str

@app.post("/chat")
def chat(msg: Message):
    global chat_history_ids

    # Encode user input + append to history
    new_input_ids = tokenizer.encode(msg.message + tokenizer.eos_token, return_tensors='pt')

    if chat_history_ids is not None:
        input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)
    else:
        input_ids = new_input_ids

    chat_history_ids = model.generate(
        input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode only the new output
    response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return {"reply": response}
