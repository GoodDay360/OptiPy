from optipy import _get_version_list, _get_version

def getVersionList():
    return _get_version_list.start()

def getVersion(mc_version:str=None):
    if not mc_version: raise Exception("'mc_version' is Required! Missing Minecraft Version.")
    return _get_version.start(mc_version)