import requests, json

mcversion = 1.18
url = f"https://nitroxenon-minecraft-forge-v1.p.rapidapi.com/optifine/{mcversion}"

headers = {
    'x-rapidapi-key': "a6f51f9ea2mshf179951f6fc0d97p1b476ejsndba62ed12b1d",
    'x-rapidapi-host': "nitroxenon-minecraft-forge-v1.p.rapidapi.com"
    }

def download(data):
    for info in data:
        url = f'https://optifine.net/download?f={info.get("filename")}' #Optifine Download Link
        print(url)  
        #break  #Remove # before break if you want only 1 url.
    
def request():
    try:
        r = requests.get(url, headers=headers,timeout=5)
        data = json.loads(r.text)
        download(data)
    except requests.exceptions.Timeout:
        print("Connection Timeout! Retrying...")
        request()
request()
