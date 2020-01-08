from pytchat import ReplayChatAsync,JsonfileArchiveProcessor,ReplayChat,LiveChat,LiveChatAsync
from . processors.default.processor import DefaultProcessor
import asyncio
from concurrent.futures import CancelledError

# async def main():
#   chat = LiveChatAsync("JDJgU30QnqI") #rion"rJoy6e48MIo"
#   while chat.is_alive():
#     data = await chat.get()
#     for c in data.items:
#       print(f"{c.elapsedTime} [{c.author.name}]-{c.message} {c.amountString}")
#       await data.tick_async()

# if __name__=='__main__':
#   try:
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#   except CancelledError:
#     pass
   
# def main():
#   chat = ReplayChat("rJoy6e48MIo",seektime = 55) #rion"rJoy6e48MIo"JDJgU30QnqI
#   while chat.is_alive():
#     data = chat.get()
#     for c in data.items:
#       print(f"{c.elapsedTime} [{c.author.name}]-{c.message} {c.amountString}")
#       data.tick()

# if __name__=='__main__':
#   main()

from pytchat import ReplayChat

def main():
  chat = ReplayChat("WKbeRYSwYHA", seektime = 60*60*6+60*50)
  while chat.is_alive():
    data = chat.get()
    for c in data.items:
      print(f"{c.elapsedTime} [{c.author.name}]-{c.message} {c.amountString}")
      data.tick()

main()
  #other background operation.

# from pytchat import LiveChat

# chat = LiveChat("JDJgU30QnqI")
# while chat.is_alive():
#   data = chat.get()
#   for c in data.items:
#     print(f"{c.datetime} [{c.author.name}]-{c.message} {c.amountString}")
#     data.tick()