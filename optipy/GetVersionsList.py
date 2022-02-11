import requests,json,warnings
from distutils.version import LooseVersion
# This use to ignore sorting *LooseVersion. 
# You can remove it if you want.
warnings.filterwarnings('ignore')

def getversionlist():
    url = "https://nitroxenon-minecraft-forge-v1.p.rapidapi.com/optifine/versionlist"
    headers = {
        'x-rapidapi-key': "a6f51f9ea2mshf179951f6fc0d97p1b476ejsndba62ed12b1d",
        'x-rapidapi-host': "nitroxenon-minecraft-forge-v1.p.rapidapi.com"
        }
    try:
        r = requests.get(url, headers=headers, timeout=5)
        data = json.loads(r.text)
        data = sorted(data, key=lambda i: (LooseVersion(i.get('mcversion'))),reverse=True)
        return data
    except requests.exceptions.Timeout:
        print("Connection Timeout! Retrying...")
        getversionlist()
