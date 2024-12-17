import logging
import os
import sys

# Define log format
logging_str = "[%(asctime)s:%(levelname)s:%(module)s:%(lineno)s:%(message)s]"

# Log file path setup
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create logger
logger = logging.getLogger("Recommand_system_Logger")
