import requests

updateKey = "1234"

#--//REMOTE UPDATE (IMPORTANT)

def startUpdate():
    try:
        mainGet = requests.get("https://raw.github.com/SnippyRP/LanCon/main/CodeBackup/main.py",headers={'Content-Type':'text/plain; charset=utf-8'})
        open("main.py","wb").write(mainGet.content)
        mainGet = requests.get("https://raw.github.com/SnippyRP/LanCon/main/CodeBackup/commands.py",headers={'Content-Type':'text/plain; charset=utf-8'})
        open("commands.py","wb").write(mainGet.content)
        mainGet = requests.get("https://raw.github.com/SnippyRP/LanCon/main/CodeBackup/remoteUpdate.py",headers={'Content-Type':'text/plain; charset=utf-8'})
        open("remoteUpdate.py","wb").write(mainGet.content)
        return True
    except:
        return False
