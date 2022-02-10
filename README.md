# Optifine-API
An API for getting Optifine VersionsList/Versions/Download-URL.
# Table of contents
- [Installation](#installation)
- [Get Versions List](#get-versions-list)
- [Get Specify Versions](#get-specify-versions)
- [Get Optifine Download URL](#get-optifine-download-url)
# Installation
```
pip install optipy
```
# Get Versions List
This will get list of all Optifine versions.
- The output might not show all versions in console.
- Dump the list into file if you want to see all the versions.
```python
from optipy import getversionlist

print(getversionlist())
```
# Get Specify Versions
This will get Optifine versions informations by just specify Minecraft Version.  
Arguments: 
- **[ Required ]** `mcversion` is for specify minecraft version.
- **[ Optional ]** `single` use to return only one optifine version. (Default: False)  
```python
from optipy import getversion

print(getversion(mcversion='1.18', single=True))
```
# Get Optifine Download URL
This will get filename from version info and use different method to download it.  
💫 Method 2 is faster then Method 1 when it downloading, but request will take a while. Why?  
- Because method 2 use temporary url and method 1 use global url. (It just my guessed. But I already tested it.)
## 🔰 Get Download URL Method 1
Arguments: 
- **[ Required ]** `mcversion` is for specify minecraft version.
- **[ Optional ]** `single` use to return only one optifine version url. (Default: False)  
```python
from optipy import geturl

print(geturl(mcversion='1.18', single=True))
```
## 🔰 Get Download URL Method 2
Arguments: 
- **[ Required ]** `mcversion` is for specify minecraft version.
- **[ Optional ]** `single` use to return only one optifine version url. (Default: False)  
```python
from optipy import geturl2

print(geturl2(mcversion='1.18', single=True))
```
