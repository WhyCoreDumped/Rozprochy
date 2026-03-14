import threading
import time
import random

ITEM_TYPES = ["Laptops", "Phones", "Tablets"]

class Warehouse:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_amount = 0
        self.items = {item_type: 0 for item_type in ITEM_TYPES}

        self.condition = threading.Condition()

    def produce(self, producer_id, item_type, amount):
        with self.condition:
            while self.current_amount >= self.max_capacity:
                print(f"Producer {producer_id} Warehouse is full. Sleeping...")
                self.condition.wait()
            
            amount_to_add = min(amount, self.max_capacity - self.current_amount)
            
            self.items[item_type] += amount_to_add
            self.current_amount += amount_to_add
            
            print(f"Producer {producer_id} added {amount_to_add} {item_type} | Warehouse space: {self.current_amount}/{self.max_capacity}")
            
            self.condition.notify_all()

    def consume(self, consumer_id, item_type, desired_amount):
        with self.condition:
            while self.current_amount == 0:
                print(f"Consumer {consumer_id} Warehouse is empty. Sleeping...")
                self.condition.wait()

            available_amount = self.items[item_type]
            
            if available_amount > 0:
                amount_to_buy = min(desired_amount, available_amount)
                self.items[item_type] -= amount_to_buy
                self.current_amount -= amount_to_buy
                
                print(f"Consumer {consumer_id} bought {amount_to_buy} {item_type} (wanted {desired_amount}) | Warehous space: {self.current_amount}/{self.max_capacity}")
                
                self.condition.notify_all()
            else:
                print(f"Consumer {consumer_id} looked for {item_type}, but it's not in the warehouse.")

def producer_thread(producer_id, warehouse):
    while True:
        item_type = random.choice(ITEM_TYPES)
        amount = random.randint(1, 15)
        
        warehouse.produce(producer_id, item_type, amount)

        time.sleep(random.uniform(0.5, 3.0))

def consumer_thread(consumer_id, warehouse):
    while True:
        item_type = random.choice(ITEM_TYPES)
        desired_amount = random.randint(1, 10)
        
        warehouse.consume(consumer_id, item_type, desired_amount)

        time.sleep(random.uniform(0.5, 3.0))



shared_warehouse = Warehouse(max_capacity=50)
    
for i in range(1, 4):
    p = threading.Thread(target=producer_thread, args=(i, shared_warehouse), daemon=True)
    p.start()
        
for i in range(1, 5):
    c = threading.Thread(target=consumer_thread, args=(i, shared_warehouse), daemon=True)
    c.start()

while True:
        time.sleep(1)