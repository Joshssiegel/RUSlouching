import TestGUI as tg
from threading import Thread
from time import sleep

isSlouching = 0

def slouching():
    while True:
        tg.slouching(isSlouching)

if __name__ == "__main__":
    thread = Thread(target = slouching, args = ())
    print("setting slouching to 1")
    thread.start()
    sleep(5)
    isSlouching = 1
    print("DONE_SLOUCHING")
    thread.join()
    print "thread finished...exiting"
