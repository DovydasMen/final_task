import logging
from logging import Formatter, StreamHandler

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.INFO

console_logger = logging.getLogger("Console Logger")
console_logger.setLevel(LOG_LEVEL)
console_file_handler = StreamHandler()
console_formatter = Formatter(LOG_FORMAT)
console_file_handler.setFormatter(console_formatter)
console_logger.addHandler(console_file_handler)

if __name__ == "__main__":
    console_logger.info("fatality")
