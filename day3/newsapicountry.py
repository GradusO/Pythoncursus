import requests

apiKey = "80559f68dddf48a689a7d5d5d9074522"

country = input("Select a country: ")
if not country:
    print("You did not enter a country. Please try again.")
else:
    r = requests.get(f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={apiKey}')

data = r.json()

if not data['totalResults']:
    print(f"Cannot find news for country: {country}")
else:
    for article in data['articles']:
        print(article['title'])