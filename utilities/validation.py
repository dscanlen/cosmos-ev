"""
Validation docstring
"""

from cosmos.entities import CelestialBody

class CelestialBodyValidation:
    """
    This class contains validation methods for the CelestialBody class.
    """

    @staticmethod
    def validate_general_info(general_info: dict) -> None:
        """
        PLACEHOLDER
        """
        required_keys = ['name', 'description', 'body_type', 'parent', 'satellites']
        for key in required_keys:
            if key not in general_info:
                raise ValueError(f"'{key}' is missing in general_info")

        if not isinstance(general_info['name'], str):
            raise ValueError("'name' should be of type str")

        if not isinstance(general_info['description'], str):
            raise ValueError("'description' should be of type str")

        if not isinstance(general_info['body_type'], str):
            raise ValueError("'body_type' should be of type str")

        if general_info['parent'] is not None and not isinstance(general_info['parent'], CelestialBody):
            raise ValueError("'parent' should be either None or an instance of CelestialBody")

        if not isinstance(general_info['satellites'], list):
            raise ValueError("'satellites' should be a list")
        for satellite in general_info['satellites']:
            if not isinstance(satellite, CelestialBody):
                raise ValueError("'satellites' list should only contain instances of CelestialBody")

    @staticmethod
    def validate_orbital_mechanics(orbital_mechanics: dict) -> None:
        """
        PLACEHOLDER
        """
        required_keys = ['apogee', 'perigee', 'orbit_period', 'rotation_period', 'inclination']
        for key in required_keys:
            if key not in orbital_mechanics:
                raise ValueError(f"'{key}' is missing in orbital_mechanics")

        if not isinstance(orbital_mechanics['apogee'], (int, float)) or orbital_mechanics['apogee'] < 0:
            raise ValueError("'apogee' should be a positive number")

        if not isinstance(orbital_mechanics['perigee'], (int, float)) or orbital_mechanics['perigee'] < 0:
            raise ValueError("'perigee' should be a positive number")

        if not isinstance(orbital_mechanics['orbit_period'], (int, float)) or orbital_mechanics['orbit_period'] < 0:
            raise ValueError("'orbit_period' should be a positive number")

        if not isinstance(orbital_mechanics['rotation_period'], (int, float)) or orbital_mechanics['rotation_period'] < 0:
            raise ValueError("'rotation_period' should be a positive number")

        if not isinstance(orbital_mechanics['inclination'], (int, float)):
            raise ValueError("'inclination' should be a number")

    @staticmethod
    def validate_physical_properties(physical_properties: dict) -> None:
        """
        PLACEHOLDER
        """
        required_keys = ['radius', 'axial_tilt']
        for key in required_keys:
            if key not in physical_properties:
                raise ValueError(f"'{key}' is missing in physical_properties")

        if not isinstance(physical_properties['radius'], (int, float)) or physical_properties['radius'] <= 0:
            raise ValueError("'radius' should be a positive number")

        if not isinstance(physical_properties['axial_tilt'], (int, float)):
            raise ValueError("'axial_tilt' should be a number")
