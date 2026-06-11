import multiprocessing
import requests
import os

os.makedirs("files", exist_ok=True)


def downloadFile(url, name):
    response = requests.get(url)
    open(f"files/file_{name}.jpg", "wb").write(response.content)
    pass

url = "https://instagram.com/favicon.ico"
pros = []
for i in range(5):
    # downloadFile(url, i)
    p = multiprocessing.Process(target=downloadFile, args=[url, i])
    p.start()
    pros.append(p)

for p in pros:
    p.join()