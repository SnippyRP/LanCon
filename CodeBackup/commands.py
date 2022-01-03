import requests
import json
import random
import pyperclip
import socket
import ipaddress

helpStr = "help [none] Get help!\nget [url] [JSON] Send a GET request with JSON data\npost [url] [JSON] Send a POST request with JSON data\nrobloxuserinfo [userid] Gets info about the given player\ncredits [none] Get credits list\nrobloxassetinfo [assetid] Gets info about the given asset\nrandomrobloxgame [none] Finds a random game (not saying it's good)\nbg/background [R] [G] [B] Sets terminal background\nfeedback [text] Sends feedback me me, the developer, to improve the console!\nupdate [update key] Updates to the latest version [BROKEN]\ngetnew [update key] Downloads the newest version of LanCON [BROKEN]\nipconfig Get IP information\nhostchat [PORT] Hosts a chatroom server via LanCON, users can join via the PORT\njoinchat [PORT] Joins a chatroom with the PORT"


def runCommand(keyList):
    if not keyList[0] == "":
        if str.lower(keyList[0]) == "help":
            return helpStr
        if str.lower(keyList[0]) == "get":
            try:
                r = requests.get(keyList[1],data=json.loads(keyList[2]))
                return r.content
            except:
                return "Invalid command data"
        if str.lower(keyList[0]) == "post":
            try:
                r = requests.post(keyList[1],data=json.loads(keyList[2]))
                return r.content
            except:
                return "Invalid command data"
        if str.lower(keyList[0]) == "robloxuserinfo":
            try:
                r = requests.get(f"https://users.roblox.com/v1/users/{str(keyList[1])}")
                return f"""
Created: {r.json()["created"]}
Username: {r.json()["name"]}
Displayname: {r.json()["displayName"]}
Banned: {r.json()["isBanned"]}
Description: {r.json()["description"]}

"""
            except:
                return "Invalid command data"
        if str.lower(keyList[0]) == "credits":
            try:
                return "Snippy#1118 - Literally Everything"
            except:
                return "Invalid command data"
        if str.lower(keyList[0]) == "robloxassetinfo":
            try:
                r = requests.get(f"https://api.roblox.com/Marketplace/ProductInfo?assetId={str(keyList[1])}")
                return f"""
Created: {r.json()["Created"]}
Name: {r.json()["Name"]}
Price: {r.json()["PriceInRobux"]}
Description: {r.json()["Description"]}
Creator: {r.json()["Creator"]["Name"]}

"""
            except:
                return "Invalid command data"
        if str.lower(keyList[0]) == "randomrobloxgame":
                try:
                    while True:
                        i = str(random.randint(1,421852462))
                        r = requests.get("https://api.roblox.com/Marketplace/ProductInfo?assetId="+i)
                        if r.json()["AssetTypeId"] == 9:
                            pyperclip.copy(f"https://www.roblox.com/games/{i}")
                            return f"[CLIPBOARD] https://www.roblox.com/games/{i}"
                except:
                    return "Invalid command data"
        if str.lower(keyList[0]) == "bg" or str.lower(keyList[0]) == "background":
                try:
                    return "[CODE] Setting background.."
                except:
                    return "Invalid command data"
        if str.lower(keyList[0]) == "feedback":
                try:
                    return "Thanks for your feedback! It will be reviewed later."
                except:
                    return "Invalid command data"
        if str.lower(keyList[0]) == "update":
                try:
                    return "..."
                except:
                    return "Invalid command data"
        if str.lower(keyList[0]) == "getnew":
                try:
                    return "..."
                except:
                    return "Invalid command data"
        if str.lower(keyList[0]) == "ipconfig":
                try:
                    request = requests.get("https://httpbin.org/ip")
                    return f"""
Wireless / Wi-Fi
    IPv4 .......... {str(socket.gethostbyname(socket.gethostname()))}
    IPv6 .......... {str(request.json()["origin"])}
"""
                except:
                    return "Invalid command data"
        if str.lower(keyList[0]) == "hostchat":
                try:
                    return "..."
                except:
                    return "Invalid command data"
        if str.lower(keyList[0]) == "joinchat":
                try:
                    return "..."
                except:
                    return "Invalid command data"
        else:
            return f"[ERROR] '{keyList[0]}' is not a valid command. Type 'help' for details"
