import requests
import json
import pyfiglet

def getLocation(id: str):
    return json.loads(requests.get("https://assetdelivery.roblox.com/v2/asset/?ID=" + id, headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Accept": "",
        "Accept-Language": "en-US",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://create.roblox.com/",
        "Content-Type": "application/json",
        "Roblox-Place-Id": "0",
        "Roblox-Browser-Asset-Request": "true",
        "x-csrf-token": "C+M6drN813Ra",
        "Origin": "https://create.roblox.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "cross-site",
        "TE": "trailers",
    }).text)["locations"][0]["location"]

def downloadAudio(url: str):
    data = requests.get(url, headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
        "Accept": "",
        "Accept-Language": "en-US",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://create.roblox.com/",
        "Content-Type": "application/json",
        "Roblox-Place-Id": "0",
        "Roblox-Browser-Asset-Request": "true",
        "x-csrf-token": "C+M6drN813Ra",
        "Origin": "https://create.roblox.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "cross-site",
        "TE": "trailers",
    })

    file = open("haiii.ogg", "wb")
    file.write(data.content)
    file.close()

if __name__ == "__main__":
    print(pyfiglet.figlet_format("audio stuff", "big"))
    id = input("id: ")
    location = str(getLocation(id))
    downloadAudio(location)
    print("downloaded :3")