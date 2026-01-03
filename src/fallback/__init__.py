# fallback Package Initialization

"""This module initializes the fallback system for drone navigation when RSS signals are unavailable."""

# Import required modules
from .algorithm import FallbackAlgorithm
from .navigation import Navigation
from .logging import Logger

# Initialize components
fallback_algorithm = FallbackAlgorithm()
navigation_system = Navigation()
logger = Logger()

# Add method to start fallback system
def start_fallback_system():
    """Starts the fallback system for inertial navigation."""
    try:
        logger.log('Starting fallback system')
        navigation_system.initiate_navigation()
        logger.log('Fallback system initiated')
    except Exception as e:
        logger.log(f'Error starting fallback system: {e}')

# Add method to stop fallback system
def stop_fallback_system():
    """Stops the fallback system and logs current status."""
    try:
        logger.log('Stopping fallback system')
        navigation_system.terminate_navigation()
        logger.log('Fallback system stopped')
    except Exception as e:
        logger.log(f'Error stopping fallback system: {e}')

# Add method to get system status
def system_status():
    """Returns the status of the fallback system."""
    try:
        status = navigation_system.get_navigation_status()
        logger.log('Retrieving system status')
        return status
    except Exception as e:
        logger.log(f'Error retrieving system status: {e}')
        return 'Error: Unable to retrieve status'

# Ensure that the fallback system can be accessed easily
__all__ = [
    'start_fallback_system',
    'stop_fallback_system',
    'system_status',
    'fallback_algorithm',
    'navigation_system',
    'logger'
]
