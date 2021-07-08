import time
from GetPrice import get_price
from plotter import plotting
import threading

if __name__ == "__main__":

    t1 = threading.Thread(target=get_price)
    t2 = threading.Thread(target=plotting)

    t1.start()
    time.sleep(720)
    t2.start()
