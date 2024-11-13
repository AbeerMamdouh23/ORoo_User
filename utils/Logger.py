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
            log_directory = os.path.join(os.getcwd(),"..","test-output", "logs")
            if not os.path.exists(log_directory):
                os.makedirs(log_directory)
        return self.logger
