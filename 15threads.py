import logging
import threading

def thread_function(name):
    logging.info("Thread %s: starting", name)
    for _ in range(50, 56):
        logging.info("Thread %s: running "+str(_), name)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("=======> Main started.")

    threads = list()
    for index in range(10):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    #for index, thread in enumerate(threads):
        #logging.info("Main    : before joining thread %d.", index)
        #thread.join()
        #logging.info("Main    : thread %d done", index)

    #threads[8].join()
    logging.info("=======> Main finished.")
