from datetime import datetime
import time
import logging

logger=logging.getLogger(__name__)

if __name__=="__main__":
    start_time=datetime.now()
    time.sleep(3)
    end_time=datetime.now()
    print(end_time-start_time)

    logging.info("hello")
