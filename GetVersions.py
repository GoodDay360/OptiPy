import requests

mcversion = 1.18
url = f"https://nitroxenon-minecraft-forge-v1.p.rapidapi.com/optifine/{mcversion}"

headers = {
    'x-rapidapi-key': "a6f51f9ea2mshf179951f6fc0d97p1b476ejsndba62ed12b1d",
    'x-rapidapi-host': "nitroxenon-minecraft-forge-v1.p.rapidapi.com"
    }
def request():
    try:
        r = requests.get(url, headers=headers,timeout=3)
        print(r.text)
    except requests.exceptions.Timeout:
        print("Connection Timeout! Retrying...")
        request()
request()