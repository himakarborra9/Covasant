import aiohttp
import asyncio
from bs4 import BeautifulSoup
import time

start_time = time.time()

async def gathering_data(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            html = await response.text()
            code = BeautifulSoup(html, "html.parser")
            return {url: code}
    except Exception as e:
        return {url: str(e)}

async def get_main_page_links():
    url = "https://www.python.org/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10) as response:
            html = await response.text()
            code = BeautifulSoup(html, "html.parser")
            links = [a['href'] for a in code.select('a') if a['href'].startswith('https')]
            return links

async def main():
    all_links = await get_main_page_links()

    async with aiohttp.ClientSession() as session:
        tasks = [gathering_data(session, link) for link in all_links]
        results = await asyncio.gather(*tasks)
             
        for result in results:
            print(result)

    print("Time taken to execute all links :", time.time() - start_time)

asyncio.run(main())
