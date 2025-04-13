import requests
from bs4 import BeautifulSoup
import concurrent.futures
import time

s = time.time()

def gathering_data(url):
    try:
        response = requests.get(url)
        code = BeautifulSoup(response.text,"html.parser")
        return {url:code}  
    except requests.exceptions.RequestException as e:
        return {url: str(e)}  


url = r"https://www.python.org/"
response = requests.get(url)
content = BeautifulSoup(response.text,"html.parser")
links = content.select("a")
all_links = [a['href'] for a in content.select('a') if a['href'].startswith('https')]


results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:  
    for result in executor.map(gathering_data,all_links):
        results.append(result)


for result in results:
    print(result)
print(time.time()-s)

