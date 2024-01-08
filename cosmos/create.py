"""
Cosmos Initialisation
======================

Let there be light!

This is where you can initialise your astronomical entities.
"""

# An example set of entities

from cosmos.entities import CelestialBody, StarSystem, StarCluster, Skybox

sun = CelestialBody(
    general_info={
        'name': 'Sun',
        'description': 'The star at the center of our solar system.',
        'parent': None,  # Sun doesn't orbit another celestial body.
        'satellites': []  # We'll add planets as satellites later.
    },
    orbital_parameters={
        'eccentricity': 0,
        'semi_major_axis': 0,  # It's at the center.
        'inclination': 0,  # Taking the Sun's equator as reference.
        'orbital_period': 0  # It doesn't orbit another body.
    },
    physical_properties={
        'mass': 1.989 * 10**30,  # in kg
        'radius': 696340,  # in km
        'body_type': 'star',
        'axial_tilt': 0,
        'rotation_period': 25  # in days, approximate.
    }
)

mercury = CelestialBody(
    general_info={
        'name': 'Mercury',
        'description': 'The closest planet to the Sun.',
        'parent': sun,
        'satellites': []  # Mercury has no moon.
    },
    orbital_parameters={
        'eccentricity': 0.2056,
        'semi_major_axis': 57909175,  # in km
        'inclination': 3.38,  # degrees to the solar equator.
        'orbital_period': 88  # in days.
    },
    physical_properties={
        'mass': 3.3011 * 10**23,  # in kg
        'radius': 2439.7,  # in km
        'body_type': 'planet',
        'axial_tilt': 0.034,  # in degrees.
        'rotation_period': 59.646  # in days.
    }
)

venus = CelestialBody(
    general_info={
        'name': 'Venus',
        'description': 'The second planet from the Sun.',
        'parent': sun,
        'satellites': []  # Venus has no moon.
    },
    orbital_parameters={
        'eccentricity': 0.0068,
        'semi_major_axis': 108208000,  # in km
        'inclination': 3.86,  # degrees to the solar equator.
        'orbital_period': 225  # in days.
    },
    physical_properties={
        'mass': 4.867 * 10**24,  # in kg
        'radius': 6051.8,  # in km
        'body_type': 'planet',
        'axial_tilt': 177.4,  # in degrees, it's retrograde.
        'rotation_period': 243.025  # in days, also retrograde.
    }
)

earth = CelestialBody(
    general_info={
        'name': 'Earth',
        'description': 'The third planet from the Sun and our home.',
        'parent': sun,
        'satellites': [],  # We'll add the Moon later if needed.
    },
    orbital_parameters={
        'eccentricity': 0.0167,
        'semi_major_axis': 149598262,  # in km
        'inclination': 7.155,  # degrees to the solar equator, approximate.
        'orbital_period': 365.256  # in days.
    },
    physical_properties={
        'mass': 5.97237 * 10**24,  # in kg
        'radius': 6371,  # in km
        'body_type': 'planet',
        'axial_tilt': 23.44,  # in degrees to its orbital plane.
        'rotation_period': 0.99726968  # in days, roughly 24 hours.
    }
)

earth_moon = CelestialBody(
    general_info={
        'name': 'Moon',
        'description': 'Earth\'s only natural satellite.',
        'parent': earth,  # Moon orbits Earth.
        'satellites': []  # The Moon itself doesn't have any satellites.
    },
    orbital_parameters={
        'eccentricity': 0.0549,
        'semi_major_axis': 384400,  # in km, average distance from Earth.
        'inclination': 5.145,  # degrees to Earth's equatorial plane.
        'orbital_period': 27.322  # in days.
    },
    physical_properties={
        'mass': 7.342 * 10**22,  # in kg.
        'radius': 1737.5,  # in km.
        'body_type': 'moon',
        'axial_tilt': 6.68,  # in degrees to its orbital plane.
        'rotation_period': 27.322  # in days, synchronous rotation.
    }
)

mars = CelestialBody(
    general_info={
        'name': 'Mars',
        'description': 'The fourth planet from the Sun.',
        'parent': sun,
        'satellites': [],  # Mars has two moons: Phobos and Deimos.
    },
    orbital_parameters={
        'eccentricity': 0.0935,
        'semi_major_axis': 227939100,  # in km
        'inclination': 5.65,  # degrees to the solar equator.
        'orbital_period': 687  # in days.
    },
    physical_properties={
        'mass': 6.4171 * 10**23,  # in kg
        'radius': 3389.5,  # in km
        'body_type': 'planet',
        'axial_tilt': 25.19,  # in degrees.
        'rotation_period': 1.025957  # in days, roughly 24.6 hours.
    }
)

mars_moon1 = CelestialBody(
    mars_moon1_info = {
        'name': 'Phobos',
        'description': 'Mars\'s larger moon.',
        'parent': mars, # Moon orbits Mars
        'satellites': [],
    },
    mars_moon1_mechanics = {
        'eccentricity': 0.0151,  # Example eccentricity for Phobos
        'semi_major_axis': 0.0001,  # Example semi-major axis for Phobos (in AU)
        'inclination': 1.093,  # Example inclination for Phobos (in degrees)
        'orbital_period': 0.32  # Example orbital period for Phobos (in days)
    },
    mars_moon1_properties = {
        'mass': 1.0659 * 10**16,  # Mass of Phobos in kg
        'radius': 11.1,  # Radius of Phobos in km
        'body_type': 'moon',
        'axial_tilt': 0.0,  # Axial tilt of Phobos (in degrees)
        'rotation_period': 0.32  # Rotation period of Phobos (in days)
    }
)

mars_moon2 = CelestialBody(
    mars_moon2_info = {
        'name': 'Deimos',
        'description': 'Mars\'s smaller moon.',
        'parent': mars , # Moon orbits Mars
        'satellites': []
    },
    mars_moon2_mechanics = {
        'eccentricity': 0.00033,  # Example eccentricity for Deimos
        'semi_major_axis': 0.0002,  # Example semi-major axis for Deimos (in AU)
        'inclination': 1.791,  # Example inclination for Deimos (in degrees)
        'orbital_period': 1.26  # Example orbital period for Deimos (in days)
    },
    mars_moon2_properties = {
        'mass': 1.4762 * 10**15,  # Mass of Deimos in kg
        'radius': 6.2,  # Radius of Deimos in km
        'body_type': 'moon',
        'axial_tilt': 0.0,  # Axial tilt of Deimos (in degrees)
        'rotation_period': 1.26  # Rotation period of Deimos (in days)
    }
)

# Create the Skybox
skybox = Skybox(radius=100)

# Create the StarSystem
solar_system = StarSystem(name='Solar System',
                          location=(0, 0, 0),  # You can adjust the location
                          bodies=[sun, earth])  # Add other planets and moons

# Create Constellations for the skybox (if needed)
# constellation1 = Constellation(name='Orion', description='The Orion constellation', location=(0, 0))
# Add more constellations if desired

# Add the StarSystem to the StarCluster
star_cluster = StarCluster(name='Local Star Cluster',
                            skybox=skybox,
                            star_systems=[solar_system])