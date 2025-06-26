import chainlit as cl


# @cl.on_chat_start
# async def start():
#     await cl.Message(
#         author="User Profiling",
#         content="Welcome to the Dynamic User Profiling system!",
#         elements=[cl.Image(name="logo", path="public/logo_light.png")],
#     ).send()


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=f"받은 메시지: {message.content}",
    ).send()
