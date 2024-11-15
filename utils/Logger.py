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
            script_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            log_dir = os.path.join(script_dir,  "test-output", "logs")
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
        return self.logger
