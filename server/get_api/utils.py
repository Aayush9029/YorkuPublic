import logging
from enum import Enum
from os import rename, listdir, makedirs, path
from datetime import datetime


class ServiceEnums(Enum):
    REDDIT = "reddit"
    TWITTER = "twitter"
    GOOGLE = "google"


#  Move logs to logs/old_logs folder on startup (if any)
try:
    # if logs folder doesn't exist, create it
    if not path.exists("logs"):
        makedirs("logs")
    # if old_logs folder doesn't exist, create it
    if not path.exists("logs/old_logs"):
        makedirs("logs/old_logs")

    rename(
        "logs/log.log",
        f"logs/old/log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log",
    )
except Exception as e:
    print(e)
    pass

# Logging setup, enable file logging, email logging, and console logging

logging.basicConfig(
    filename="logs/log.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)
logging.info("Logging setup complete")

# Logger functions


def log_error(api: ServiceEnums, error):
    logging.info(f"[{api.value}]: {error}")


def log_warning(api: ServiceEnums, warning):
    logging.info(f"[{api.value}]: {warning}")


def log_info(api: ServiceEnums, info):
    logging.info(f"[{api.value}]: {info}")


def cleanup_string(string) -> str:
    return string.encode("ascii", errors="ignore").decode("utf-8")


#  OTHER UTLS:

# convert Unix timestamp to human readable time
def convert_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
