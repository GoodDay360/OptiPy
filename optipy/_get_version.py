from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import requests
from pprint import pprint

def start(mc_version):
    DATA = {}

    url = "https://www.optifine.net/downloads"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    h2 = soup.find("h2", string=f'Minecraft {mc_version}')
    if not h2: return None
    mc_version = f'{h2.text.replace("Minecraft ","")}'

    table_element = h2.find_next("table", {"class": "downloadTable"})
    
    if table_element:
        tr_elements = table_element.find_all("tr",{"class": "downloadLine"})
        if not tr_elements: return None
        item = []
        for tr in tr_elements:
            title = tr.find("td", class_="colFile").text
            date = tr.find("td", class_="colDate").text
            forge = tr.find("td", class_="colForge").text
            mirror = tr.find("td", class_="colMirror")
            mirror_link = mirror.find("a").get("href")
            parsed_link = urlparse(mirror_link)
            
            
            # Parse the query string into a dictionary
            args = parse_qs(parsed_link.query)

            # Get the value of 'f'
            f_value = args["f"][0]
            url = f"https://optifine.net/download?f={f_value}"
            item.append({
                "title": title,
                "date": date,
                "forge": forge,
                "url": url,
            })
        DATA[mc_version] = item
    return DATA

if __name__ == "__main__":
    DATA = start(mc_version="1.12.2")
    pprint(DATA, sort_dicts=False)
