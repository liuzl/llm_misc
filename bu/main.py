from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio, os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

async def main():
    agent = Agent(
        task="帮我做一个去承德、赤峰三日自驾游的旅游攻略",
        llm=ChatOpenAI(model=os.getenv("MODEL"), api_key=os.getenv("OPENAI_API_KEY"), base_url=os.getenv("OPENAI_BASE_URL"),),
    )
    await agent.run()

asyncio.run(main())