import requests

apiKey = "8a6ad6b8ec404358838544b28df00ff6"
r = requests.get(f'https://newsapi.org/v2/top-headlines?country=nl&apiKey={apiKey}')
data = r.json()

print(data)
for x in data['articles']:
    print(x['title'])
