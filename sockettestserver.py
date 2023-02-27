import asyncio
import websockets
import sys
import json
import subprocess
from time import sleep

f=open('data.json') #Get this by using the drillster API (https://www.drillster.com/info/developers/api/2.1.1/endpoints/get-repertoire)

data = json.load(f)

links=[]
for i in data['drills']:
    print("Drill "+i['name']+" contains:")
    for i2 in i['drills']:
        print("    "+i2['name']+":    https://www.drillster.com/widgets/player/4/"+i2['id'])
        links.append("https://www.drillster.com/widgets/player/4/"+i2['id'])


async def message(websocket, path):
    for i in links:
        msg = await websocket.recv()
        print(msg)
        subprocess.Popen("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" % i)
        sleep(1)
        await websocket.send(i)

start_server = websockets.serve(message, "127.0.0.1", 43434)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()