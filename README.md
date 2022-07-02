# OptiPy
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
Arguments: 
- **[ Optional ]** `timeout` use for how long can request take before it cancel. (Default: 30)  
```python
from optipy import getVersionList

while True:
    data = getVersionList(timeout=15)
    if "408" not in data:
        print(data)
        break
```
# Get Specify Versions
This will get Optifine versions informations by just specify Minecraft Version.  
Arguments: 
- **[ Required ]** `mcversion` is for specify minecraft version.
- **[ Optional ]** `single` use to return only one optifine version. (Default: False)  
- **[ Optional ]** `timeout` use for how long can request take before it cancel. (Default: 30)  
```python
from optipy import getVersion

while True:
    data = getVersion(mcversion="1.18", single=True, timeout=15)
    if "408" not in data:
        print(data)
        break
```
# Get Optifine Download URL
This will get filename from version info and use different method to download it.  
Arguments: 
- **[ Required ]** `mcversion` is for specify minecraft version.
- **[ Optional ]** `single` use to return only one optifine version url. (Default: False)  
- **[ Optional ]** `timeout` use for how long can request take before it cancel. (Default: 30)  
```python
from optipy import getUrl

while True:
    data = getUrl(mcversion="1.18", single=True, timeout=15)
    if "408" not in data:
        print(data)
        break
```