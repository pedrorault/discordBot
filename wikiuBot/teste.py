import aiohttp
import asyncio

async def pls():
    nome = input("Digite algo: ")
    url = f'http://wikiu.app/generate?name={nome}'
    res = await aiohttp.request('GET',url)
    print(res)

loop = asyncio.get_event_loop()
result = loop.run_until_complete(pls())