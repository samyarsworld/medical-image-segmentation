import os
import sys
import logging
from datetime import datetime

LOGGER_NAME = "text_summarizer"
LOG_DIR = "logs"
LOG_FORMAT = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_filepath = os.path.join(LOG_DIR, log_file)
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= LOG_FORMAT,
    handlers=[
        logging.FileHandler(log_filepath), # log to file
        logging.StreamHandler(sys.stdout) # log to terminal
    ]
)

logger = logging.getLogger(LOGGER_NAME)


