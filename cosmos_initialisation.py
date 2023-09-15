"""
Docstring placeholder
"""


class CelestialBody:
    """
    A class representing a celestial body within a star system.

    Attributes:
    -----------
    general_info: Dict[str, str or None]
        Contains general information about the celestial body:
            - name (str): The name of the celestial body.
            - description (str): A brief description of the celestial body.
            - body_type (str): The type of celestial body (e.g., 'star',
                        'planet', 'moon', 'comet').
            - parent (str or None): The parent celestial body that this body
                        orbits. None if this body is the central star.

    orbital_mechanics: Dict[str, float]
        Contains the celestial body's orbital parameters:
            - apogee (float): The farthest point to the parent body in
                        astronomical units (AU).
            - perigee (float): The closest point to the parent body in
                        astronomical units (AU).
            - orbit_period (float): Time taken for the celestial body to
                        complete one orbit around its parent body in Earth
                        days.
            - rotation_period (float): Time taken for the celestial body to
                        complete one rotation on its axis in Earth days.
            - inclination (float): The angle between the celestial body's
                        orbital plane and the reference plane (usually the
                        plane of the ecliptic) in degrees.

    physical_properties: Dict[str, float]
        Contains the physical attributes of the celestial body:
            - radius (float): Radius of the celestial body in kilometers.
            - axial_tilt (float): The angle between the celestial body's
                        rotation axis and a line
                        perpendicular to its orbital plane in degrees.

    Methods:
    --------

    """

    def __init__(self, general_info, orbital_mechanics, physical_properties):
        """
        Initialize a CelestialBody with general information, orbital mechanics, and physical
        properties.
        """
        self.general_info = {
            'name': general_info.get('name'),
            'description': general_info.get('description'),
            'body_type': general_info.get('body_type'),
            'parent': general_info.get('parent', None)
        }

        self.orbital_mechanics = {
            'apogee': orbital_mechanics.get('apogee'),
            'perigee': orbital_mechanics.get('perigee'),
            'orbit_period': orbital_mechanics.get('orbit_period'),
            'inclination': orbital_mechanics.get('inclination')
        }

        self.physical_properties = {
            'radius': physical_properties.get('radius'),
            'axial_tilt': physical_properties.get('axial_tilt'),
            'rotation_period': physical_properties.get('rotation_period')
        }

    def info(self, name, description, body_type, parent):
        """
        Defines the general information for a celestial body
        """
        general_info = {
            'name': name,
            'description': description,
            'body_type': body_type,
            'parent': parent
        }
        return general_info

    def mechanics(self, apogee, perigee, orbit_period, inclination):
        """
        Defines the orbital mechanics information for a celestial body
        """
        orbital_mechanics = {
            'apogee': apogee,
            'perigee': perigee,
            'orbit_period': orbit_period,
            'inclination': inclination
        }
        return orbital_mechanics

    def properties(self, radius, axial_tilt, rotation_period):
        """
        Defines the orbital mechanics information for a celestial body
        """
        physical_properties = {
            'radius': radius,
            'axial_tilt': axial_tilt,
            'rotation_period': rotation_period
        }
        return physical_properties


# Usage example:



earth = CelestialBody(earth_general_info, earth_orbital_mechanics, earth_physical_properties)

print(earth.general_info['name'])  # Accessing the name of the celestial body


def body_general_info(name, description, body_type, parent):
    general_info = {
        'name': name,
        'description': description,
        'body_type': body_type,
        'parent': parent
    }
    return general_info
