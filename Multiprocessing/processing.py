import threading
import logging
import time

def thread_function(name):
    logging.info(f'thread {name} starting')
    time.sleep(3)
    logging.info(f'thread {name} finished')

if __name__=='__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info('main : before running thread')
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()
    logging.info('main : wait for thread to finish')
    x.join()
    logging.info('main : all done')
