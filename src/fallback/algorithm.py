class FallbackSystem:
    def __init__(self):
        self.rssi_threshold = -80  # Signal strength threshold for fallback
        self.navigation_mode = "Normal"  # Current navigation mode

    def check_rssi(self, rssi_value):
        """Check RSSI value to determine navigation mode."""
        try:
            if not isinstance(rssi_value, (int, float)):
                raise ValueError("RSSI value must be a number")
            if rssi_value < self.rssi_threshold:
                self.switch_to_fallback_mode()
            else:
                self.navigation_mode = "Normal"
        except ValueError as e:
            self.log_error(e)

    def switch_to_fallback_mode(self):
        """Switch to inertial navigation when RSS signal is lost."""
        if self.navigation_mode != "Inertial":
            self.navigation_mode = "Inertial"
            self.log_fallback_action()

    def log_fallback_action(self):
        """Log the fallback action for monitoring purposes."""
        with open('fallback_log.txt', 'a') as log_file:
            log_file.write('Fallback activated. Mode: Inertial\n')

    def log_error(self, error):
        """Log errors for debugging and monitoring purposes."""
        with open('fallback_log.txt', 'a') as log_file:
            log_file.write(f'Error: {str(error)}\n')

    def get_current_mode(self):
        """Return the current navigation mode."""
        return self.navigation_mode

# Example usage
if __name__ == "__main__":
    fallback_system = FallbackSystem()
    test_rssi_values = [-90, -70, None, -85, "bad input"]  # Simulated RSSI values

    for value in test_rssi_values:
        fallback_system.check_rssi(value)
        print(f'Signal: {value}, Mode: {fallback_system.get_current_mode()}')
