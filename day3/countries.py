import requests

country = input("Country? ")
resp = requests.get("https://restcountries.com/v2/name/" + country)

if resp.status_code == 404:
    print("No such country")
else:
    data = resp.json()
    for country in data:
        if "capital" in country:
            print(country['name'], country["capital"])
        else:
            print(f"{country['name']} has no capital")