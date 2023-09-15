"""
Placeholder docstring
"""

from typing import Dict


class CelestialBody:
    """
    A class representing a celestial body within a star system.
    """

    VALID_BODY_TYPES = ['star', 'planet', 'moon', 'comet', 'asteroid']

    def __init__(self,
                 general_info: Dict[str, str],
                 orbital_mechanics: Dict[str, float],
                 physical_properties: Dict[str, float]) -> None:
        """
        Initialize a CelestialBody with general information, orbital mechanics, and physical
        properties.
        """
        self.general_info = {
            'name': general_info['name'],
            'description': general_info['description'],
            'body_type': self.validate_body_type(general_info['body_type']),
            'parent': general_info.get('parent')
        }

        self.orbital_mechanics = {
            'apogee': self.validate_positive_value(orbital_mechanics['apogee'], "Apogee"),
            'perigee': self.validate_positive_value(orbital_mechanics['perigee'], "Perigee"),
            'orbit_period': self.validate_positive_value(orbital_mechanics['orbit_period'], "Orbit Period"),
            'rotation_period': self.validate_positive_value(orbital_mechanics['rotation_period'], "Rotation Period"),
            'inclination': orbital_mechanics['inclination']
        }

        self.physical_properties = {
            'radius': self.validate_positive_value(physical_properties['radius'], "Radius"),
            'axial_tilt': physical_properties['axial_tilt']
        }

    def validate_body_type(self, body_type: str) -> str:
        """
        Validates the body type against a predefined list of acceptable body types.
        Raises ValueError if the body type is not recognized.
        """
        if body_type not in self.VALID_BODY_TYPES:
            raise ValueError(f"Unrecognized body type '{body_type}'. Valid types are: {', '.join(self.VALID_BODY_TYPES)}")
        return body_type

    def validate_positive_value(self, value: float, parameter_name: str) -> float:
        """
        Validates if a value is positive. Raises ValueError if it's not.
        """
        if value <= 0:
            raise ValueError(f"{parameter_name} must be a positive value.")
        return value

    def get_name(self) -> str:
        """
        Returns the name of the celestial body.
        """
        return self.general_info['name']

    def update_apogee(self, new_apogee: float) -> None:
        """
        Updates the apogee value of the celestial body.
        """
        self.orbital_mechanics['apogee'] = self.validate_positive_value(new_apogee, "Apogee")

    def __repr__(self) -> str:
        """
        Provides a textual representation of the celestial body object.
        """
        return f"<CelestialBody(name={self.get_name()}, body_type={self.general_info['body_type']})>"

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
