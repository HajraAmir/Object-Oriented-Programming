import logging
import time

if __name__ == "__main__":
    fmat = "%(levelname)s ==> %(asctime)s: %(message)s"
    logging.basicConfig(filename='app.log', filemode='a', format=fmat, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Start: %d.", 2022)
    time.sleep(3)
    logging.warning("Finish: %d.", 2023)
