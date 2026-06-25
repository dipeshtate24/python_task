import requests

url = "https://newsapi.org/v2/everything?q=apple&from=2026-06-01&to=2026-06-01&sortBy=popularity&apiKey=API_KEY"
respone = requests.get(url)
print(respone.text)
