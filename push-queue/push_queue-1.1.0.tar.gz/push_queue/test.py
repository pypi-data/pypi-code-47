from push_queue import Queue

if __name__ == '__main__':
    c = Queue(100)
    from threading import Thread
    import time
    def cc():
        for i in range(10000):
            c.push(True)
            print(f'push to the queue')
            time.sleep(0.005)

    def ff():
        for i in range(10000):
            c.get(True)
            print(f'get to the queue')
            time.sleep(0.1)
    Thread(target=cc).start()
    ff()
