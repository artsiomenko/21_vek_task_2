import logging
import threading
import time
from logger import setup_logging
from scheduler import start_scheduler

setup_logging()

def start_threaded_schedule():
    logging.info("Scheduler thread started")
    scheduler_thread = threading.Thread(target=start_scheduler)
    scheduler_thread.start()

if __name__ == "__main__":
    start_threaded_schedule()
    while True:
        time.sleep(1)
