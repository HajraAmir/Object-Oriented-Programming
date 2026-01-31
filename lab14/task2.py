import random
import threading
import time
import math

def print_random_numbers(min_range, max_range):
    for i in range(20):
        print(random.randint(min_range, max_range))
        time.sleep(3)
def main():
    min_range = int(input("Enter the minimum range: "))
    max_range = int(input("Enter the maximum range: "))

  
    random_thread = threading.Thread(target=print_random_numbers, args=(min_range, max_range))
    random_thread.start()

    for _ in range(20):
        angle = float(input("Enter an angle in degrees: "))
        radians = math.radians(angle)
        print(f"sin({angle}) = {math.sin(radians)}")
        print(f"cos({angle}) = {math.cos(radians)}")

    random_thread.join()


main()
