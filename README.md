# OptiPy
An API for getting Optifine VersionsList/Versions/Download-URL.
# Table of contents
- [Installation](#installation)
- [Get Versions List](#get-versions-list)
- [Get Specify Versions](#get-specify-versions)
# Installation
```
pip install optipy
```
# Get Versions List
This will get list of all Optifine versions.
- The output might not show all versions in console.
- Dump the list into file if you want to see all the versions.
```python
from optipy import getVersionList

DATA = getVersionList()
print(DATA)
```
# Get Specify Versions
This will get Optifine versions informations by just specify Minecraft Version.  
Arguments: 
- **[ Required ]** `mc_version` is for specify minecraft version.
```python
from optipy import getVersion

DATA = getVersion(mc_version="1.20.1")
print(DATA)
```