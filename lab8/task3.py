class queue :
    def __init__(self):
        self.items=[]
        
    def isempty(self):
        len(self.items)==0 
        
    def  insert(self,item):
        self.items.append(item)
        
    def remove(self):
        if self.items:
            return self.items.pop(0)
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0
import random

printer_queue=queue()
ticks=100
printer_speed=5
printer_busy=False

for tick in range(1, ticks+1):
    random_number=random.randint(50, 250)
    if random_number % 5 == 0 or random_number % 13 == 0 or random_number % 67 == 0:
        pages = random_number % 61
        printer_queue.insert(pages)
        print(f"At tick {tick}, task {pages} pages received for printing.")      
for tick in range (1,tick+1)       
        