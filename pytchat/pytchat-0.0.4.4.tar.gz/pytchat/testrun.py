from pytchat import LiveChat, LiveChatAsync, CompatibleProcessor, ReplayChat,  ReplayChatAsync
from pytchat.core_multithread.replaychat import ReplayChat
import pytchat
import asyncio
import time
import concurrent.futures
from .processors.jsonfile_archive_processor import JsonfileArchiveProcessor
from .processors.default.processor import DefaultProcessor
#video_id ="7IXS9ZBeM7s"
video_id = "hOleS05Au9c" #live
#video_id ="OIvJv6n-9Ro" #チャット無効
#video_id = "ptKbyJf17lI" #チャット有効
#video_id = "ew0rBDYLxLc" #チャット無効ライブ
def sync_api():
    print("sync_api")
    chat = LiveChat(video_id, 
        processor = CompatibleProcessor() )

    while chat.is_alive():
        chatlist = chat.get()
        polling = chatlist["pollingIntervalMillis"]/1000
        for c in chatlist["items"]:
            if c.get("snippet"):
                print(f"[{c['authorDetails']['displayName']}]"
                        f"-{c['snippet']['displayMessage']}")
                time.sleep(polling/len(chatlist["items"]))

async def async_api():
    print("async_api")
    chat = LiveChatAsync(video_id,
        processor = pytchat.CompatibleProcessor())

    chatlist = await chat.get()
    polling = chatlist["pollingIntervalMillis"]/1000
    for c in chatlist["items"]:
        if c.get("snippet"):
            print(f"[{c['authorDetails']['displayName']}]-{c['snippet']['displayMessage']}")
            await asyncio.sleep(polling/len(chatlist["items"]))

def sync_def():
    print("sync_def")
    chat = LiveChat(video_id)
    while chat.is_alive():
        data = chat.get()
        for c in data.items:
            print(f"<{c.datetime}>[{c.author.name}]-{c.message}")
            data.tick()
                
async def savefunc(chatobj):
    pass

from .processors.speed_calculator import SpeedCalculator
async def async_def():
    print("async_def")
    chat = LiveChatAsync(video_id)
    counter =0
    wait = 0
    while chat.is_alive():
        print("counter",counter)
        # speed = await chat.get()
        # print(speed)
        # await asyncio.sleep(3)
        counter += 1

        data = await chat.get()
        for c in data.items:
            print(f"<{c.datetime}>[{c.author.name}]-{c.message} {c.amountString}")
            await data.tick_async()

        if counter ==2:
            chat.pause()
            print("paused")
            wait = 3
        if counter ==12:
            chat.resume()
            print("resumed")
            wait = 0
        print("sleep",wait)
        await asyncio.sleep(wait)
    #chat.terminate()


def sync_def_callback():
    print("sync_def_callback")
    chat = LiveChat(video_id, callback= func,
        direct_mode = True,seektime = -1,
        #force_replay=True
        )
    counter =0
    
    while chat.is_alive():
        counter +=1
        print("Replay=",chat.is_replay())
        print(counter)
        if counter ==3:
            #chat.pause()
            #print("paused")
            pass
        # if counter ==9:
        #     chat.resume()
        #     print("resumed")
        #print("sleep",wait)
        time.sleep(5)   

def func(data):
        for c in data.items:
            print(f"{c.elapsedTime}<{c.datetime}> [{c.author.name}]-{c.message}")
            data.tick()
    

async def async_def_callback():
    print("async_def_callback")
    chat = LiveChatAsync(video_id, callback=proc_a,
        direct_mode = True,seektime = 1000,
        force_replay=True
        )
    counter =0
    print("Replay=",chat.is_replay())
    while chat.is_alive():
        
        counter +=1
        print(counter)
        if counter ==20:
            #chat.pause()
            #print("paused")
            pass
        if counter ==90:
            #chat.resume()
            print("resumed")

        #print("sleep",wait)
        await asyncio.sleep(5)        
 
async def proc_a(chat):
    for c in chat.items:
        print(f"{c.elapsedTime.rjust(8)} <{c.datetime}> [{c.author.name}]-{c.message}")
        await chat.tick_async()

    #chat.terminate()


def replay():
    chat = ReplayChat(video_id,callback=func,seektime= 60*60*1+60*29+30)
    while chat.is_alive():
        #chat.pause()
        #time.sleep(30)
        #chat.resume()

        time.sleep(3)


async def replay_async():
    chat = LiveChatAsync("ptKbyJf17lI",seektime= 60*60*1+60*29+30,callback=proc_a)
    counter = 0

    while chat.is_alive():
        
        counter +=1
        print(counter)
        if counter ==4:
            chat.pause()
            print("paused")

        if counter ==7:
            chat.resume()
            print("resumed")

        #print("sleep",wait)
        await asyncio.sleep(3)    


async def replay_async_speed():
    chat = ReplayChatAsync("mCVWJIqdZzA",seektime= 300,processor = SpeedCalculator(),
    callback = lambda speed : print(speed) )
    while chat.is_alive():
        await asyncio.sleep(3)

async def proc_s(speed):
    print(speed)



def simple_sync():
    print("simple_sync_callback")
    chat = LiveChat(video_id,
            processor = pytchat.SimpleDisplayProcessor(),
            callback   = testproc_m)
    while chat.is_alive():
        time.sleep(3)

def testproc_m(chatobj):
    timeout = chatobj.get("timeout",3)
    chatdata = chatobj.get("chatlist")

            
    for c in chatdata:
        if c:
            print(c)
            time.sleep(timeout/len(chatdata))

async def testproc(chatobj):

    timeout = chatobj.get("timeout",3)
    chatdata = chatobj.get("chatlist")
    if chatdata:
        for chat in chatdata:
            print(chat)
            time.sleep(timeout/len(chatdata))

async def jsondisp():
    from .processors.json_display_processor import JsonDisplayProcessor
    chat = LiveChatAsync("5l2gqQ8ZqQs", processor = JsonDisplayProcessor(),
        callback= disp)

    while chat.is_alive():
        await asyncio.sleep(1)

    async def disp(data):
        print(data)
    

async def main2():
    chat = ReplayChatAsync("G1w62uEMZ74", seektime = 100, callback = func2)
    while chat.is_alive():
        #other background operation here.
        await asyncio.sleep(3)

async def func2(data):
    for count in range(0,len(data.items)):
        c= data.items[count]
        if count!=len(data.items):
            tick=data.items[count+1].timestamp -data.items[count].timestamp
        else:
            tick=0
        print(f"<{c.elapsedTime}> [{c.author.name}]-{c.message} {c.amountString}")
        await asyncio.sleep(tick/1000)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main2())

async def combinator_test_async():
    chat = ReplayChatAsync("itNgeQEu7KI",  
        processor = ( DefaultProcessor(), SpeedCalculator() ))
    while chat.is_alive():
        data, speed = await chat.get()
        disp_combinated(data, speed)
        await asyncio.sleep(3)

def disp_combinated(data, speed):
    for c in data.items:
        print(f"{c.elapsedTime.rjust(8)} <{c.datetime}> [{c.author.name}]-{c.message}")

        data.tick()
    print(f"----------speed--------:{speed} it/m")

def combinator_test():
    chat = ReplayChat("itNgeQEu7KI",  
        processor = ( DefaultProcessor(), SpeedCalculator() ))
    while chat.is_alive():
        data, speed = chat.get()
        disp_combinated(data, speed)
        time.sleep(3)


if __name__ =='__main__':

    
    a=1

    if a==0:
        print("async")
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(async_def())
        except asyncio.CancelledError:
            print('Cancelled')

    elif a == 1:
        print("sync_def_callback")
        sync_def_callback()
    elif a == 2:
        print('replay')
        replay()
    elif a == 3:
        print('async_def_callback')

        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(async_def_callback())
        except asyncio.CancelledError:
            print('Cancelled')
    elif a==4:
        print("async_")
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(async_def_callback())
        except asyncio.CancelledError:
            print('Cancelled') 
    elif a==5:
        print("async_speed")
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(replay_async_speed())
        except asyncio.CancelledError:
            print('Cancelled') 

    elif a==6:
        print("replay_async")
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(replay_async())
        except asyncio.CancelledError:
            print('Cancelled')
    elif a==7:
        print("combinator_test")
        combinator_test()
        print('Cancelled')
   




