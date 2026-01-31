import random

class Queue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        if self.items:
            return self.items.pop(0)
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0


printer_queue=Queue()
ticks=random.randint(50,250)
printer_speed=5
printer_busy=False

for tick in range(1, ticks+1):
    random_number = random.randint(50, 250)
    if random_number % 5 == 0 or random_number % 13 == 0 or random_number % 67 == 0:
        pages = random_number % 61
        printer_queue.insert(pages)
        print(f"At tick {tick}, task {pages} pages received for printing.")

    if not printer_busy and not printer_queue.isEmpty():
        task_pages = printer_queue.remove()
        print(f"At tick {tick}, task {task_pages} starts printing.")
        printer_busy = True

    if printer_busy:
        printer_speed -= 1
        if printer_speed == 0:
            print(f"At tick {tick}, task {task_pages} completed.")
            printer_busy = False
            printer_speed = 5