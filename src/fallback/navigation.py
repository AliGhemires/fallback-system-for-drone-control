import numpy as np

class InertialNavigation:
    def __init__(self, initial_position=(0.0, 0.0), initial_velocity=(0.0, 0.0), initial_orientation=0.0):
        self.position = np.array(initial_position, dtype=float)  # x, y
        self.velocity = np.array(initial_velocity, dtype=float)  # vx, vy
        self.orientation = initial_orientation  # angle in radians
        self.time_step = 0.1  # time step for updates in seconds
        self.acceleration = np.array([0.0, 0.0], dtype=float)  # ax, ay

    def update_orientation(self, angular_velocity):
        """Update the orientation based on angular velocity and ensure it stays within 0 to 2*pi range."""
        self.orientation += angular_velocity * self.time_step
        self.orientation %= (2 * np.pi)  # Wrap the orientation to remain within [0, 2*pi]

    def update_acceleration(self, acc_x, acc_y):
        """Set the current acceleration values with safety checks."""
        if not isinstance(acc_x, (int, float)) or not isinstance(acc_y, (int, float)):
            raise ValueError("Acceleration must be numeric.")
        self.acceleration = np.array([acc_x, acc_y], dtype=float)

    def update_navigation(self):
        """Update the position and velocity based on current acceleration and time step."""
        self.velocity += self.acceleration * self.time_step
        self.position += self.velocity * self.time_step

    def get_position(self):
        """Get the current position of the drone as a list."""
        return self.position.tolist()

    def get_velocity(self):
        """Get the current velocity of the drone as a list."""
        return self.velocity.tolist()

    def get_orientation(self):
        """Get the current orientation of the drone in radians."""
        return self.orientation

# Example usage (commented)
# if __name__ == '__main__':
#     nav = InertialNavigation()
#     nav.update_acceleration(0.1, 0.2)  # Simulate some acceleration
#     for _ in range(10):
#         nav.update_navigation()
#         print('Position:', nav.get_position())
#         print('Velocity:', nav.get_velocity())
#         print('Orientation:', nav.get_orientation())
