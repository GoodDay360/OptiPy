import requests
from distutils.version import LooseVersion

def getVersionList(timeout: int = 30):

    url = "https://nitroxenon-minecraft-forge-v1.p.rapidapi.com/optifine/versionlist"
    headers = {
        'x-rapidapi-key': "a6f51f9ea2mshf179951f6fc0d97p1b476ejsndba62ed12b1d",
        'x-rapidapi-host': "nitroxenon-minecraft-forge-v1.p.rapidapi.com"
        }
    try:
        r = requests.get(url, headers=headers, timeout=timeout)
        data = r.json()
        data = sorted(data, key=lambda i: (LooseVersion(i.get('mcversion'))),reverse=True)
        return data
    except requests.exceptions.Timeout:
        return "408 Request Time-out"

if __name__ == "__main__":
    while True:
        data = getVersionList(timeout=15)
        if "408" not in data:
            print(data)
            break