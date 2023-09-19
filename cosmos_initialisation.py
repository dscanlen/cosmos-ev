"""
Placeholder docstring
"""

from typing import Dict


class CelestialBody:
    """
    A class representing a celestial body within a star system.
    """

    def __init__(self,
                 general_info: Dict[str, str],
                 orbital_mechanics: Dict[str, float],
                 physical_properties: Dict[str, float]) -> None:
        """
        Initialize a CelestialBody with general information, orbital mechanics,
        and physical properties.
        """
        self.general_info = {
            'name': general_info['name'],
            'description': general_info['description'],
            'body_type': general_info['body_type'],
            'parent': general_info['parent']
        }

        self.orbital_mechanics = {
            'apogee': orbital_mechanics['apogee'],
            'perigee': orbital_mechanics['perigee'],
            'orbit_period': orbital_mechanics['orbit_period'],
            'rotation_period': orbital_mechanics['rotation_period'],
            'inclination': orbital_mechanics['inclination']
        }

        self.physical_properties = {
            'radius': physical_properties['radius'],
            'axial_tilt': physical_properties['axial_tilt']
        }

    def get_name(self) -> str:
        """
        Returns the name of the celestial body.
        """
        return self.general_info['name']

    def get_description(self) -> str:
        """
        Returns the description of the celestial body.
        """
        return self.general_info['description']


# Usage:
# planet_info = {
#     "name": "Earth",
#     "description": "Our home planet.",
#     "body_type": "planet",
#     "parent": "Sun"
# }
# planet_orbit = {
#     "apogee": 1.017,
#     "perigee": 0.983,
#     "orbit_period": 365.25,
#     "rotation_period": 1.0,
#     "inclination": 23.5
# }
# planet_properties = {
#     "radius": 6371.0,
#     "axial_tilt": 23.44
# }
# earth = CelestialBody(planet_info, planet_orbit, planet_properties)
# print(earth)
