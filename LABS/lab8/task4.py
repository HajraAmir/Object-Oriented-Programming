class Queue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None

    def isEmpty(self):
        return len(self.items) == 0
import random

task_queue = Queue()


printer_busy = False
current_task = None
pages_remaining = 0
task_number = 0


for tick in range(random.randint(50, 250)):
   
    num = random.randint(1, 1000)
    if num % 5 == 0 or num % 13 == 0 or num % 67 == 0:
        pages = num % 61
        task_queue.insert(pages)
        task_number += 1
        print(f"At tick {tick}, task {task_number} of {pages} pages received for printing.")

    if not printer_busy:
        if not task_queue.isEmpty():
            pages_remaining = task_queue.remove()
            printer_busy = True
            print(f"At tick {tick}, task {task_number} starts printing.")
    else:
        pages_remaining -= 5
        if pages_remaining <= 0:
            printer_busy = False
            print(f"At tick {tick}, task {task_number} completed.")


if printer_busy:
    print(f"At tick {tick}, task {task_number} completed.")