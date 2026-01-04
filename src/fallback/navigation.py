class Navigation:
    """
    Handles navigation for the drone, including fallback to inertial navigation
    in the absence of RSSI signals.
    """

    def __init__(self):
        self.current_mode = 'normal'  # Modes: normal, fallback
        self.position = (0, 0)  # Drone's current position
        self.velocity = (0, 0)  # Drone's current velocity

    def update_position(self, delta_time):
        """
        Updates the drone's position based on current mode and velocity.
        :param delta_time: Time since last update in seconds.
        """
        if delta_time <= 0:
            raise ValueError("delta_time must be a positive number.")

        if self.current_mode == 'normal':
            # Normal navigation mode: Update position based on velocity
            self.position = (
                self.position[0] + self.velocity[0] * delta_time,
                self.position[1] + self.velocity[1] * delta_time
            )
        elif self.current_mode == 'fallback':
            # Inertial navigation: Implement fallback position update logic
            self.position = self.fallback_position_update(delta_time)

    def fallback_position_update(self, delta_time):
        """
        Calculates the new position based on inertial measurement
        during fallback navigation.
        :param delta_time: Time since last update in seconds.
        """
        if delta_time <= 0:
            raise ValueError("delta_time must be a positive number.")

        # Placeholder for actual inertial navigation algorithm
        # For now, we'll simulate some movement
        fallback_velocity = self.get_fallback_velocity()
        return (
            self.position[0] + fallback_velocity[0] * delta_time,
            self.position[1] + fallback_velocity[1] * delta_time
        )

    def get_fallback_velocity(self):
        """
        Provide logic for calculating fallback velocity. Can be replaced
        with more sophisticated algorithms in the future.
        """
        return (1, 1)  # Simulated constant fallback velocity

    def switch_to_fallback(self):
        """
        Switches the mode to fallback navigation.
        """
        self.current_mode = 'fallback'

    def switch_to_normal(self):
        """
        Switches the mode back to normal navigation.
        """
        self.current_mode = 'normal'

    def set_velocity(self, new_velocity):
        """
        Updates the drone's velocity.
        :param new_velocity: Tuple indicating new velocity (vx, vy).
        """
        if not isinstance(new_velocity, tuple) or len(new_velocity) != 2:
            raise ValueError("new_velocity must be a tuple with two elements.")

        self.velocity = new_velocity
