# Optifine-API
An API for getting Optifine VersionsList/Versions/Download-URL.
# Table of contents
- [Get Versions List](#get-versions-list)
- [Get Specify Versions](#get-specify-versions)
- [Download Optifine](#download-optifine)
# Get Versions List
This will get list of all Optifine versions. The result is shuffled.
```python
import requests

url = "https://nitroxenon-minecraft-forge-v1.p.rapidapi.com/optifine/versionlist"

headers = {
    'x-rapidapi-key': "a6f51f9ea2mshf179951f6fc0d97p1b476ejsndba62ed12b1d",
    'x-rapidapi-host': "nitroxenon-minecraft-forge-v1.p.rapidapi.com"
    }
def request():
    try:
        r = requests.get(url, headers=headers, timeout=5)
        print(r.text)
    except requests.exceptions.Timeout:
        print("Connection Timeout! Retrying...")
        request()
request()
```
# Get Specify Versions
This will get Optifine versions informations by just specify Minecraft Version.
```python
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
```
# Download Optifine
This will get filename from version info and use different method to download it.  
💫 Method 1 is faster then Method 2 when it downloading. Why?  
Because method 1 use temporary url and method 2 use global url. (It just my guessed. But I already tested it.)
## 🔰 Download Method 1
```python
import requests, json
from requests_html import HTMLSession

mcversion = 1.18
url = f"https://nitroxenon-minecraft-forge-v1.p.rapidapi.com/optifine/{mcversion}"

headers = {
    'x-rapidapi-key': "a6f51f9ea2mshf179951f6fc0d97p1b476ejsndba62ed12b1d",
    'x-rapidapi-host': "nitroxenon-minecraft-forge-v1.p.rapidapi.com"
    }

def download(data):
    for info in data:
        session = HTMLSession()
        r = session.get(f'https://optifine.net/adloadx?f={info.get("filename")}')
        about = r.html.find('#Download', first=True)
        url = "".join(about.absolute_links)  #Optifine Download Link
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
```
## 🔰 Download Method 2
```python
import requests, json

mcversion = 1.18
url = f"https://nitroxenon-minecraft-forge-v1.p.rapidapi.com/optifine/{mcversion}"

headers = {
    'x-rapidapi-key': "a6f51f9ea2mshf179951f6fc0d97p1b476ejsndba62ed12b1d",
    'x-rapidapi-host': "nitroxenon-minecraft-forge-v1.p.rapidapi.com"
    }

def download(data):
    for info in data:
        url = f'https://optifine.net/download?f={info.get("filename")}'
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
```
