import argparse
import time
from src.fallback import algorithm, logging


def start_drone():
    try:
        logging.log("Starting drone...")
        algorithm.initialize_drone()
        logging.log("Drone started successfully.")
        return True
    except Exception as e:
        logging.log(f"Failed to start drone: {e}")
        return False

def stop_drone():
    try:
        logging.log("Stopping drone...")
        algorithm.shutdown_drone()
        logging.log("Drone stopped successfully.")
        return True
    except Exception as e:
        logging.log(f"Failed to stop drone: {e}")
        return False

def get_status():
    try:
        status = algorithm.get_drone_status()
        logging.log(f"Drone status: {status}")
        return status
    except Exception as e:
        logging.log(f"Failed to retrieve drone status: {e}")
        return "Unknown"

def main():
    parser = argparse.ArgumentParser(description="Drone Control CLI")
    parser.add_argument('action', choices=['start', 'stop', 'status'], help="Action to perform on the drone.")
    args = parser.parse_args()

    success_messages = {
        'start': "Drone operation started successfully.",
        'stop': "Drone operation stopped successfully.",
        'status': "Drone status retrieved successfully."
    }

    if args.action == 'start':
        if start_drone():
            print(success_messages['start'])
    elif args.action == 'stop':
        if stop_drone():
            print(success_messages['stop'])
    elif args.action == 'status':
        status = get_status()
        print(f"Current Status: {status}")

if __name__ == '__main__':
    main()
