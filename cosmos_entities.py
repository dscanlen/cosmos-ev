"""
Space Simulation Entities Module
================================

This module provides a set of classes representing various celestial and
astronomical entities for a space simulation or astronomical modeling tool. The
primary entities captured in this module include:

- CelestialBody: Represents individual celestial objects such as stars,
    planets, moons, and comets. Each object carries general information,
    orbital mechanics data, and physical properties.

- Constellation: Denotes a group of stars forming a recognizable pattern,
    traditionally named after its apparent form or identified with a
    mythological figure. This class captures the name, description, and
    location of each constellation.

- StarSystem: Represents an entire star system which may include one or more
    stars, planets, moons, etc. Objects that orbit the star system's barycenter
    should be part of this system.

- Skybox: Models the celestial sphere that forms the backdrop for the star
    systems and constellations. It's essentially the canvas upon which all
    other celestial objects are drawn or positioned.

- StarCluster: While not representing a scientific star cluster in the strict
    sense, this class captures the concept of a community or grouping of star
    systems. Each cluster has its own skybox and can comprise multiple star
    systems.

Each of the above entities is designed with modularity and extensibility in
mind, making it easy to expand or adapt them to specific requirements or to
integrate them into larger space simulation frameworks or tools.

Usage:
------
To use any of the classes, create an instance and provide the required
parameters. For example, to create a new star:

sun_info={'name': 'Sun',
          'description': 'A G-type main-sequence star',
          'body_type': 'star',
          'parent': None}

sun_mechanics={'apogee': 0,
               'perigee': 0, 'orbit_period': 0,
               'rotation_period': 25.05,
               'inclination': 0}

sun_properties={'radius': 696340,
                'axial_tilt': 7.25}


>>> star = CelestialBody(general_info=sun_info},
...                      orbital_mechanics=sun_mechanics,
...                      physical_properties=sun_properties)

For more complex entities like star systems or clusters, you might need to
create multiple celestial bodies or systems first before aggregating them.

Notes:
------
- Ensure that the data provided to each class is accurate and consistent with
    the domain's requirements.
- Expand and refine classes based on specific requirements or to add more
    detailed simulation capabilities.
"""

from typing import Dict, List, Optional


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


class Constellation:
    """
    A class to represent a constellation.
    """

    def __init__(self,
                 name: str,
                 description: str,
                 location: List[float]) -> None:
        """
        Constructs all the necessary attributes for the Constellation object.

        Parameters:
        name (str): the name of the constellation.
        description (str): a brief description of the constellation
        lat (float): latitude of the constellation on the skybox (-90 to 90)
        long (float): longitude of the constellation on the skybox(-180 to 180)
        """
        self.name = name
        self.description = description
        self.location = location

    def get_name(self) -> str:
        """
        Returns the name of the constellation.
        """
        return self.name

    def get_description(self) -> str:
        """
        Returns the description of the constellation.
        """
        return self.description


class StarSystem:
    """
    A class to represent a star system. Only objects that orbit the star system
    barycenter should be included.
    """

    def __init__(self,
                 name: str,
                 location: List[float],
                 bodies: Optional[List[CelestialBody]] = None) -> None:
        """
        Constructs all the necessary attributes for the StarSystem object.

        Parameters:
        name (str): the name of the star system
        location (list): a list mapping star system x, y, z coordinates
        bodies (list): a list of celestial bodies orbiting this barycenter.
        Default is None.
        """
        self.name = name
        self.location = location
        self.bodies = bodies or []


class Skybox:
    """
    A class to represent the skybox as a sphere surrounding the star scape.
    """

    def __init__(self,
                 radius: float,
                 constellations: List[Constellation] | None = None) -> None:
        """
        Constructs all the necessary attributes for the Skybox object.

        Parameters:
        radius (float): the radius of the sphere.
        constellations (dict): a dictionary mapping star names to Constellation
        Objects. Default is an empty dict.
        """
        self.radius = radius
        self.constellations = constellations or []


class StarCluster:
    """
    A class to represent a cluster of star systems.
    Note: This doesn't represent a scientific star cluster but is used to
    capture the idea of a community of star systems.
    """

    def __init__(self,
                 name: str,
                 skybox: Skybox,
                 star_systems: Optional[List[StarSystem]] = None) -> None:
        """
        Constructs all the necessary attributes for the StarCluster object.

        Parameters:
        name (str): the name of the star_cluster object
        skybox (Skybox): The surrounding skybox.
        star_systems (list): a list of star_system objects. Default is None.
        """
        self.name = name
        self.skybox = skybox
        self.star_systems = star_systems or []