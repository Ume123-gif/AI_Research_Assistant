import requests
url = "https://api.search.brave.com/res/v1/web/search"
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip"
}
params={
    "q": "Quantum Computing"
}
try:
    response = requests.get(url, headers = headers, params = params)
    data = response.json()
    print(data)
except Exception as e:
    print("Cannot load results")