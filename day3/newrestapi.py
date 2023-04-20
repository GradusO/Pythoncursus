import requests

apiKey = "sadsfsdgdgrefrsf"
r = requests.get(f'https://newsapi.org/v2/top-headlines?country=nl&apiKey={apiKey}')
data = r.json()