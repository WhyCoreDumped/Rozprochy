import threading
import queue
import time

class BinarySemaphore:
    def __init__(self):
        self.channel = queue.Queue(maxsize=1)
        
        self.channel.put(True)

    def acquire(self):
        self.channel.get()

    def release(self):
        self.channel.put(True)

shared_account = 0
semaphor = BinarySemaphore()

def bankThread(thread_id):
    global shared_account
    
    print(f"Client {thread_id} try to get to bank system")
    
    semaphor.acquire()
    print(f"Client {thread_id} accquired token")
    
    shared_account_copy = shared_account
    
    time.sleep(2.0) 
    
    shared_account_copy += 100
    shared_account = shared_account_copy
    
    print(f"Client {thread_id} realese token. Shared account state: {shared_account} PLN")
    
    semaphor.release()



threads = []
    
for i in range(1, 6):
    w = threading.Thread(target=bankThread, args=(i,))
    threads.append(w)
    w.start()
        
for w in threads:
    w.join()
        
print(f"Final account state: {shared_account} PLN (Expected: 500 PLN)")