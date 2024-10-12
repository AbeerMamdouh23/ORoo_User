import logging
import os

class Logger:
    def __init__(self):
        # Create a logger object
        self.logger = None

    def get_logger(self):
        if not self.logger:
            # Set the name of the logger
            self.logger = logging.getLogger("test_logger")
            self.logger.setLevel(logging.DEBUG)

            # Create a logs directory if it doesn't exist
            log_directory = os.path.join(os.getcwd(), "logs")
            if not os.path.exists(log_directory):
                os.makedirs(log_directory)

            # Create a file handler for logging
            file_handler = logging.FileHandler(os.path.join(log_directory, "test_log.log"))
            file_handler.setLevel(logging.DEBUG)

            # Create a formatter and set it for the handler
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)

            # Add the handler to the logger
            self.logger.addHandler(file_handler)

        return self.logger
