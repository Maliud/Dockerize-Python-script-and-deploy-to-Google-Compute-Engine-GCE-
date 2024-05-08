import logging
import time
import google.cloud.logging
import os

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if int(os.environ.get("PRODUCTION", 0)) == 1:
        logging_client = google.cloud.logging.Client()
        logging_client.setup_logging()

    


    while True:
        logging.info("5 Saniye sonra uyluya geçilecek")
        time.sleep(5)