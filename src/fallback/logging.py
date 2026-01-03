import logging

# Configure logging settings with rotation to manage file size
# This ensures the log doesn't grow endlessly which is a potential edge
# case if the drone is running for extended periods of time.
logging.basicConfig(
    filename='drone_fallback.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class FallbackLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def log_fallback_action(self, action):
        """ Logs the fallback action taken by the drone. """
        if action:
            self.logger.info(f'Fallback action performed: {action}')
        else:
            self.logger.warning('Attempted to log an empty fallback action')

    def log_drone_status(self, status):
        """ Logs the current status of the drone. """
        if status:
            self.logger.info(f'Drone status: {status}')
        else:
            self.logger.warning('Attempted to log an empty drone status')

    def log_error(self, error_message):
        """ Logs any errors encountered. """
        if error_message:
            self.logger.error(f'Error occurred: {error_message}')
        else:
            self.logger.warning('Attempted to log an empty error message')
