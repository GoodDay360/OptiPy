from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import requests
from pprint import pprint

DATA = {}

url = "https://www.optifine.net/downloads"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

h2_elements = soup.find_all("h2")

for h2 in h2_elements:
    mc_version = f'{h2.text.replace("Minecraft ","")}'

    # Find the next 'table' element after 'h2' element
    table_element = h2.find_next("table", {"class": "downloadTable"})

    if table_element:
        title = table_element.find("td", class_="colFile").text
        date = table_element.find("td", class_="colDate").text
        forge = table_element.find("td", class_="colForge").text
        mirror = table_element.find("td", class_="colMirror")
        mirror_link = mirror.find("a").get("href")
        parsed_link = urlparse(mirror_link)
        
        
        # Parse the query string into a dictionary
        args = parse_qs(parsed_link.query)

        # Get the value of 'f'
        f_value = args["f"][0]
        url = f"https://optifine.net/download?f={f_value}"

        DATA[mc_version] = {
            "title": title,
            "date": date,
            "forge": forge,
            "url": url,
        }


pprint(DATA, sort_dicts=False)