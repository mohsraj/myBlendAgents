import logging
import os

from dotenv import load_dotenv

# Load environment variables from .env in service root
load_dotenv(override=True)


def get_logger(name: str = "MyAppLogger", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        # Prevent adding multiple handlers if called multiple times
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


logger = get_logger(level=os.getenv("log_level", "INFO").upper())
