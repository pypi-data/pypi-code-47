'''
https://gist.github.com/0xpizza/dd5e005a0efeb1edfc939d3a409e22d9
'''
#!/usr/bin/python3.7

import asyncio
import ipaddress
import sys


MAX_NUMBER_WORKERS = 200


async def task_worker(task_queue, out_queue):
    '''pull connection information from queue and attempt connection'''
    while True:
        ip, port, timeout = (await task_queue.get())
        conn = asyncio.open_connection(ip, port)
        try:
            await asyncio.wait_for(conn, timeout)
        except asyncio.TimeoutError:
            pass
        else:
            out_queue.put_nowait((ip, port))
        finally:
            task_queue.task_done()
            

async def task_master(
    network: str, portrange: str, timeout: float, 
    task_queue: asyncio.Queue, scan_completed: asyncio.Event):
    '''add jobs to a queue, up to ``MAX_NUMBER_WORKERS'' at a time'''
    network = network.replace('/32', '')
    try:
        # check to see if we are scanning a single host...
        hosts = [str(ipaddress.ip_address(network)),]
    except ValueError:
        # ...or a CIDR subnet.
        hosts = map(str, ipaddress.ip_network(network).hosts())
    for ip in hosts:
        for port in portrange:
            await task_queue.put((ip, port, timeout))
    scan_completed.set()


async def main(network, ports=None, timeout=0.1, csv=False):
    '''
        main task coroutine which manages all the other functions
        if scanning over the internet, you might want to set the timeout
        to around 1 second, depending on internet speed.
    '''
    task_queue = asyncio.Queue(maxsize=MAX_NUMBER_WORKERS)
    out_queue = asyncio.Queue()
    scan_completed = asyncio.Event()
    scan_completed.clear()  # progress the main loop
        
    if ports is None:  # list of common-ass ports
        ports = ("9,20-23,25,37,41,42,53,67-70,79-82,88,101,102,107,109-111,"
        "113,115,117-119,123,135,137-139,143,152,153,156,158,161,162,170,179,"
        "194,201,209,213,218,220,259,264,311,318,323,383,366,369,371,384,387,"
        "389,401,411,427,443-445,464,465,500,512,512,513,513-515,517,518,520,"
        "513,524,525,530,531,532,533,540,542,543,544,546,547,548,550,554,556,"
        "560,561,563,587,591,593,604,631,636,639,646,647,648,652,654,665,666,"
        "674,691,692,695,698,699,700,701,702,706,711,712,720,749,750,782,829,"
        "860,873,901,902,911,981,989,990,991,992,993,995,8080,2222,4444,1234,"
        "12345,54321,2020,2121,2525,65535,666,1337,31337,8181,6969")
    
    # initialize task to add scan info to task queue
    tasks = [asyncio.create_task(
                task_master(network, ports, timeout, task_queue, scan_completed) 
             )]
    # initialize workers
    for _ in range(MAX_NUMBER_WORKERS):
        tasks.append(asyncio.create_task(task_worker(task_queue, out_queue)))
    
    await scan_completed.wait()  # wait until the task master coro is done
    await task_queue.join()      # wait for workers to finish
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)
    openports = []
    while out_queue.qsize():
        openports.append(out_queue.get_nowait())
    
if __name__ == '__main__':
    # import argparse?
    if len(sys.argv) < 2:
        print(
            'TCP Network scanner using asyncio module for Python 3.7+',
            "Scan ports in ``portstring'' or common ports if blank."
            'Port string syntax: port, port-range ...',
           f'Usage: {sys.argv[0]} network [portstring]',
            sep='\n'
        )
        raise SystemExit
    elif len(sys.argv) == 2:
        asyncio.run(main(sys.argv[1]))
    else:
        asyncio.run(main(sys.argv[1], ''.join(sys.argv[2:])))