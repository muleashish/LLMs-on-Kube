import chainlit as cl
import requests
from chainlit.input_widget import Tags

@cl.author_rename
def rename(orig_author: str):
    rename_dict = {"LLMMathChain": "Ashish Mule", "Chatbot": "Assistant", "You": "Awesome User"}
    return rename_dict.get(orig_author, orig_author)




@cl.on_message
async def main(message: cl.Message):
    # start_time = time.time()
    # tool_in(message.content, start_time)
    message_history = cl.user_session.get("message_history")
    if message_history != None:
        message_history.append({"role": "user", "content": message.content})
    else:
        message_history = []

    msg = cl.Message(content="")
    await msg.send()
    stream = requests.post("http://orcaapi:8001/talk", json={"message": message.content}, stream=True)

    for part in stream.iter_content(chunk_size=100):
        if token := part or "":
            await msg.stream_token(token.decode("utf-8"))
    # end_time = time.time()
    # tool_out(start_time, end_time)
    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()