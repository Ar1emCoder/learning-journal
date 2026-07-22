import asyncio
import aiohttp

async def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(data["body"])
asyncio.run(fetch_data())

print("====================================")

async def fetch_body():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(data["body"])
asyncio.run(fetch_body())