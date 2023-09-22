"""
Cosmos Initialisation
======================

Let there be light!

This is where you can initialise your astronomical entities.
"""

# An example set of entities

from cosmos.entities import CelestialBody

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

sun.general_info['satellites'].extend([mercury, venus, earth, mars])
