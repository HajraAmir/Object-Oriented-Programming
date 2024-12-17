from threading import Thread

def evens(count):
    print("-----Evens start")
    for e in range(count):
        print(2*e)
    print("-----Evens end")

def odds(count):
    print("-----Odds start")
    for o in range(count):
        print(2*o+1)
    print("-----Odds end")

if __name__ == "__main__":
    print("-----Main start")

    et = Thread(target=evens, args=(100,))
    ot = Thread(target=odds, args=(150,))

    et.start()
    ot.start()

    #et.join()
    #ot.join()
    print("-----Main end")
