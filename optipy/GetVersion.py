import requests,json

def getversion(**kwargs):
    if kwargs.get('mcversion'):
        url = f"https://nitroxenon-minecraft-forge-v1.p.rapidapi.com/optifine/{kwargs.get('mcversion')}"
        headers = {
            'x-rapidapi-key': "a6f51f9ea2mshf179951f6fc0d97p1b476ejsndba62ed12b1d",
            'x-rapidapi-host': "nitroxenon-minecraft-forge-v1.p.rapidapi.com"
            }
        try:
            r = requests.get(url, headers=headers,timeout=3)
            data = json.loads(r.text)
            if kwargs.get('single'):
                return data[0]
            else:
                return data
        except requests.exceptions.Timeout:
            print("Connection Timeout! Retrying...")
            getversion(kwargs)
    else:
        raise ValueError("Missing Argument: MCVersion!")