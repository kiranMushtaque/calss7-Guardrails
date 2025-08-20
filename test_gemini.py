import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import asyncio

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-pro",
    openai_client=client,
)

async def main():
    response = await model.get_response("What is the capital of Japan?")
    print(response)

asyncio.run(main())
