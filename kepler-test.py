import math
import matplotlib.pyplot as plt
from typing import Dict

class CelestialBody:
    def __init__(self, name: str, mass: float, orbital_parameters: Dict[str, float]):
        self.name = name
        self.mass = mass
        self.eccentricity = orbital_parameters["eccentricity"]
        self.semi_major_axis = orbital_parameters["semi_major_axis"]
        self.inclination = orbital_parameters["inclination"]
        self.orbit_period = orbital_parameters["orbit_period"]

    def position_at_time(self, t: float):
        # Mean motion (n = 2π/T)
        n = 2 * math.pi / self.orbit_period

        # Mean anomaly (M = n(t - T₀))
        M = n * t  # Assuming T₀ = 0 for simplicity

        # Solving Kepler's Equation (E - e * sin(E) = M) iteratively using Newton's method.
        # Starting with an initial guess of E = M
        E = M
        for _ in range(10):  # usually converges quickly
            E = E - (E - self.eccentricity * math.sin(E) - M) / (1 - self.eccentricity * math.cos(E))

        # True anomaly (ν)
        v = 2 * math.atan(math.sqrt((1 + self.eccentricity) / (1 - self.eccentricity)) * math.tan(E / 2))

        # Radial distance (r)
        r = self.semi_major_axis * (1 - self.eccentricity * math.cos(E))

        # Using r and ν to get (x, y, z)
        x = r * (math.cos(v))
        y = r * (math.sin(v))
        z = r * (math.sin(v) * math.sin(self.inclination))

        return x, y, z


class StarSystem:
    def __init__(self, primary: CelestialBody, secondary: CelestialBody):
        self.primary = primary
        self.secondary = secondary

    def get_positions(self, t: float):
        x1, y1, z1 = self.primary.position_at_time(t)
        x2, y2, z2 = self.secondary.position_at_time(t)

        return (x1, y1, z1), (x2, y2, z2)


# Sample usage:

sun_parameters = {
    "eccentricity": 0,
    "semi_major_axis": 0,
    "inclination": 0,
    "orbit_period": 1  # arbitrary, as it doesn't move in this simple model
}

earth_parameters = {
    "eccentricity": 0.0167,
    "semi_major_axis": 1,  # 1 AU (distance from Earth to Sun)
    "inclination": 7.155,
    "orbit_period": 365.25  # in days
}

mars_parameters = {
    "eccentricity": 0.0934,
    "semi_major_axis": 1.52,  # 1 AU (distance from Earth to Sun)
    "inclination": 5.65,
    "orbit_period": 687  # in days
}

sun = CelestialBody("Sun", mass=1.989 * 10**30, orbital_parameters=sun_parameters)
earth = CelestialBody("Earth", mass=5.972 * 10**24, orbital_parameters=earth_parameters)
mars = CelestialBody("Earth", mass=5.972 * 10**24, orbital_parameters=mars_parameters)

earth_system = StarSystem(sun, earth)
mars_system = StarSystem(sun, mars)

earth_x_coords, earth_y_coords, earth_z_coords = [], [], []
mars_x_coords, mars_y_coords, mars_z_coords = [], [], []

for day in range(365):  # Looping through a year (365 days)
    _, earth_position = earth_system.get_positions(day)
    earth_x_coords.append(earth_position[0])
    earth_y_coords.append(earth_position[1])
    earth_z_coords.append(earth_position[2])

    _, mars_position = mars_system.get_positions(day)
    mars_x_coords.append(mars_position[0])
    mars_y_coords.append(mars_position[1])
    mars_z_coords.append(mars_position[2])

# Plotting Y against X
plt.figure(figsize=(10, 10))
plt.plot(earth_x_coords, earth_y_coords, label="Earth's Orbit", color='blue')
plt.plot(mars_x_coords, mars_y_coords, label="Mars' Orbit", color='red')
plt.scatter([0], [0], color='orange', s=200, label="Sun")  # Sun's position at the center
plt.title("Orbits Around the Sun (Y vs X)")
plt.xlabel('X (AU)')
plt.ylabel('Y (AU)')
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# Plotting Z against X
plt.figure(figsize=(10, 10))
plt.plot(earth_y_coords, earth_z_coords, label="Earth's Orbit", color='blue')
plt.plot(mars_y_coords, mars_z_coords, label="Mars' Orbit", color='red')
plt.scatter([0], [0], color='orange', s=200, label="Sun")  # Sun's position at the center
plt.title("Orbits Around the Sun (Z vs X)")
plt.xlabel('X (AU)')
plt.ylabel('Z (AU)')
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
