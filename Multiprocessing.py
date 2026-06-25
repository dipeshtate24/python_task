import multiprocessing
import requests
import os
import concurrent.futures

os.makedirs("files", exist_ok=True)


def downloadFile(url, name):
    print(f"Started downloading {name}")
    response = requests.get(url)
    open(f"files/file_{name}.jpg", "wb").write(response.content)
    print(f"Finished downloading {name}")


if __name__ == "__main__":
    url = "https://instagram.com/favicon.ico"
#     pros = []
#     for i in range(5):
#         # downloadFile(url, i)
#         p = multiprocessing.Process(target=downloadFile, args=[url, i])
#         p.start()
#         pros.append(p)

#     for p in pros:
#         p.join()


    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(10)]
        l2 = [i for i in  range(10)]
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            print(r)