import requests

def getUrl(mcversion: bool = False,single: bool = False,timeout: int = 30):
    if mcversion:
        url = f"https://nitroxenon-minecraft-forge-v1.p.rapidapi.com/optifine/{mcversion}"
        headers = {
            'x-rapidapi-key': "a6f51f9ea2mshf179951f6fc0d97p1b476ejsndba62ed12b1d",
            'x-rapidapi-host': "nitroxenon-minecraft-forge-v1.p.rapidapi.com"
            }
        try:
            r = requests.get(url, headers=headers,timeout=timeout)
            data = r.json()
            if len(data) != 0:
                liURL = []
                for info in data:
                    url = f'https://optifine.net/download?f={info.get("filename")}'
                    liURL.append(url)  
                    if single:
                        break
                return(liURL)
            else:
                return None
        except requests.exceptions.Timeout:
            return "408 Request Time-out"
    else:
        raise ValueError("Missing Argument: mcversion")

if __name__ == "__main__":
    while True:
        data = getUrl(mcversion="1.18",single=True)
        if "408" not in data:
            print(data)
            break