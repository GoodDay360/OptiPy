import requests, json
from requests_html import HTMLSession

def geturl(**kwargs):
    if kwargs.get('mcversion'):
        url = f"https://nitroxenon-minecraft-forge-v1.p.rapidapi.com/optifine/{kwargs.get('mcversion')}"
        headers = {
            'x-rapidapi-key': "a6f51f9ea2mshf179951f6fc0d97p1b476ejsndba62ed12b1d",
            'x-rapidapi-host': "nitroxenon-minecraft-forge-v1.p.rapidapi.com"
            }
        try:
            r = requests.get(url, headers=headers,timeout=5)
            data = json.loads(r.text)
            liURL = []
            for info in data:
                session = HTMLSession()
                r = session.get(f'https://optifine.net/adloadx?f={info.get("filename")}')
                about = r.html.find('#Download', first=True)
                url = "".join(about.absolute_links)  #Optifine Download Link
                liURL.append(url) 
                if kwargs.get('single'):
                    break
            return(liURL)         
        except requests.exceptions.Timeout:
            print("Connection Timeout! Retrying...")
            geturl(kwargs)
    else:
        raise ValueError("Missing Argument: MCVersion!")