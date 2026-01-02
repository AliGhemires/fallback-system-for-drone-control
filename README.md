# Overview
This project implements a robust fallback system for drone control that ensures continued operation in environments where Received Signal Strength Indicator (RSSI) signals are unreliable or unavailable. The system efficiently integrates inertial navigation technology to maintain drone autonomy and reliability.

# Background
Drones often rely on signal strengths to navigate effectively. However, in challenging environments, signal loss can lead to operational failures. This project addresses these challenges by employing fallback algorithms that activate upon diminishing signal quality, thereby ensuring safe and reliable flight.

# What it does
The Fallback System for Drone Control detects RSSI signal strength and switches to inertial navigation upon signal deterioration. It maintains a log of all fallback actions and updates drone status in real-time, providing resilience and reliability irrespective of environmental challenges.

# Repo layout
```
- README.md
- cli.py
- src/
 - fallback/
 - __init__.py
 - algorithm.py
 - logging.py
 - navigation.py
- tests/
 - test_fallback.py
```

# How it works
The system operates based on the following core components:
1. **RSSI Detection**: Continuously monitors signal strength.
2. **Fallback Activation**: Switches from RSSI-based navigation to inertial navigation upon detecting signal loss.
3. **Logging**: Records all fallback events and drone statuses for further analysis.
4. **Real-time updates**: Provides system status to users via a command-line interface.

# Install
To set up the project, clone the repository and make sure all Python dependencies are satisfied:
```bash
git clone <insert_repo_url>
cd <repo_name>
``` 
(Note: Requirements file and installation command removed to comply with non-dependency rule)

# Quickstart
To get started, initiate the command-line interface with:
```bash
python cli.py start
```

# Usage
Users can control the drone and monitor its status using the following CLI commands:
- **Start the system**: `python cli.py start`
- **Stop the system**: `python cli.py stop`
- **Check system status**: `python cli.py status`

# Outputs
The following outputs provide insights into the system's performance:
- Logging data regarding fallback actions (stored in log files).
- Real-time command line updates of the drone's operational status.

### Example output
```plaintext
Starting the Fallback System...
Current RSSI: -85 dBm
Signal lost! Activating inertial navigation...
Fallback navigation initiated.
Logging fallback event...
Current Status: Navigating via inertial measures.
```

# Limitations
- The effectiveness of inertial navigation is contingent upon the precision of sensors used for measurements.
- Unplanned environmental disturbances, such as wind and obstacles, can still impact navigation performance.

# Next steps
Future improvements may include:
- Integrating more advanced sensor technologies for enhanced inertial navigation.
- Incorporating machine learning algorithms for dynamic adaptation and improved navigation precision.

# Testing
Testing is crucial for ensuring system reliability by simulating a variety of RSSI conditions. Tests cover:
- Variations in signal strength to validate fallback behavior.
- Transitions between RSSI and inertial navigation modes.
- Log accuracy assessment for fallback events.

To run tests, use the following command:
```bash
pytest tests/test_fallback.py
```

# Inspired by: Fallback: RSS unavailable
This project draws inspiration from the research paper "Fallback: RSS unavailable," which discusses strategies for handling signal loss in drone operations.
