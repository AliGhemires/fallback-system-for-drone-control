# Fallback: Inertial Navigation-based Fallback System

class FallbackAlgorithm:
    def __init__(self):
        self.rssi_threshold = -90  # Threshold for switching to fallback
        self.inertial_navigation_active = False

    def check_rssi(self, rssi_value):
        """
        Checks if the RSSI value is above the threshold.
        Returns True if RSSI is strong, False otherwise.
        Handles edge cases where RSSI might be None.
        """
        if rssi_value is None:
            print("Warning: RSSI value is None.")
            return False
        return rssi_value >= self.rssi_threshold

    def activate_fallback(self):
        """
        Activate inertial navigation when signal is weak.
        """
        if not self.inertial_navigation_active:
            self.inertial_navigation_active = True
            print("Fallback activated: Switching to inertial navigation.")

    def deactivate_fallback(self):
        """
        Deactivate inertial navigation and restore normal operations.
        """
        if self.inertial_navigation_active:
            self.inertial_navigation_active = False
            print("Fallback deactivated: Restoring standard navigation.")

    def process_navigation(self, rssi_value):
        """
        Process the RSSI value to determine the correct navigation method.
        """
        if self.check_rssi(rssi_value):
            if self.inertial_navigation_active:
                self.deactivate_fallback()
                self.navigate_with_signal()
            else:
                self.navigate_with_signal()
        else:
            self.activate_fallback()
            self.navigate_inertially()

    def navigate_with_signal(self):
        """
        Placeholder for logic when navigating using sufficient RSSI.
        """
        print("Navigating using signal...")

    def navigate_inertially(self):
        """
        Placeholder for inertial navigation logic.
        """
        print("Navigating using inertial navigation...")

# Example usage:
if __name__ == '__main__':
    fallback_system = FallbackAlgorithm()
    # Simulate receiving RSSI signal
    test_rssi_values = [-85, -95, -80, -92, None, -70]
    for rssi in test_rssi_values:
        fallback_system.process_navigation(rssi)
