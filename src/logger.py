import logging
import os
from datetime import datetime

# Create a logger object
logger = logging.getLogger('project_logger')
logger.setLevel(logging.DEBUG)  # Set the logging level

# Create a folder for logs if it doesn't exist
log_directory = 'logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Create a file handler to log messages to a file
log_file = os.path.join(log_directory, f'{datetime.now().strftime("%Y-%m-%d")}.log')
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Create a console handler to log messages to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def get_logger():
    return logger
