from fastapi import FastAPI
from pydantic import BaseModel
from typing import AsyncGenerator
from fastapi.responses import StreamingResponse
import uvicorn
import json

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
# llm = AutoModelForCausalLM.from_pretrained("TheBloke/Orca-2-7B-GGUF", model_file="orca-2-7b.Q6_K.gguf", model_type="llama")
llm = AutoModelForCausalLM.from_pretrained(model_path_or_repo_id="./models/orca-2-7b.Q6_K.gguf", model_type="llama")
print("model loaded!")
# llm("Write Data scientist resume in less than 100 words", max_new_tokens=10000, stream=True)
# print(llm("AI is going to"))

# print(llm("AI is going to"))





app = FastAPI()

class Item(BaseModel):
    message: str


@app.get("/ping")
def read_root():
    return {"Reply": "Hey I received your message!"}


class RequestMessage(BaseModel):
    message: str

def response(msg):
    for response in llm(msg, max_new_tokens=10000, stream=True):
        yield response

@app.post("/talk/")
async def message(
    request: RequestMessage,
):
    return StreamingResponse(
        response(request.message),
        # response_generator(request.message),
        media_type="application/x-ndjson",
    )


if __name__ == "__main__":
    uvicorn.run(host="0.0.0.0", port=8001, app=app)