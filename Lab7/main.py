import threading
import math

def checkIfPrime(number):
    if number < 2:
        return
        
    limit = int(math.sqrt(number)) + 1
    for i in range(2, limit):
        if number % i == 0:
            return
            
    print(f"{threading.current_thread().name} found prime number: {number}")


def execute():
    print("How many numbers should I check?")
    limit = int(input())
    
    thread_list = []
    
    for number in range(2, limit + 1):
        thread = threading.Thread(target=checkIfPrime, args=(number,))
        
        thread_list.append(thread)
        thread.start()
        
    for thread in thread_list:
        thread.join()


execute()