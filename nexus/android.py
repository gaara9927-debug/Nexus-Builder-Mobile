import platform
def status():
 return {"runtime":"ANDROID" if "android" in platform.platform().lower() else "NON_ANDROID","apk_build":"BLOCKED_UNTIL_ANDROID_PROJECT_AND_SDK","permissions":[]}
