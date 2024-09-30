import logging
import schedule as schedule
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from fetcher import fetch_data

def scheduled_task():
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
    ]
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_to_url = {executor.submit(fetch_data, url): url for url in urls}
        
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                logging.info(f"Fetched data from {url}: {data}")
            except Exception as exc:
                logging.error(f"{url} generated an exception: {exc}")

def start_scheduler():
    schedule.every(1).hours.do(scheduled_task)

    while True:
        schedule.run_pending()
        time.sleep(1)
