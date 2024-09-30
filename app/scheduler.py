import schedule
import time
from tasks import scheduled_task

def start_scheduler():
    schedule.every(1).hours.do(scheduled_task)

    while True:
        schedule.run_pending()
        time.sleep(1)
