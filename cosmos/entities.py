"""
Cosmos Simulation Entities Module
================================

This module provides a set of classes representing various celestial and
astronomical entities for afantastical space simulation or astronomical
modeling tool. The primary entities captured in this module include:

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

from typing import Dict, Tuple, List, Optional


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
            'parent': general_info['parent'],
            'satellites': []
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

    @property
    def name(self) -> str:
        """
        Return the celestial body's name.
        """
        return self.general_info['name']

    @property
    def description(self) -> str:
        """
        Return the celestial body's description.
        """
        return self.general_info['description']

    @property
    def body_type(self) -> str:
        """
        Return the type of celestial body (e.g. star, planet, moon).
        """
        return self.general_info['body_type']

    @property
    def parent(self) -> 'CelestialBody':
        """
        Return the name of the parent body.
        """
        return self.general_info['parent']

    @property
    def satellites(self) -> List['CelestialBody']:
        """
        Return a list of satellites (if any).
        """
        return self.general_info['satellites']

    @property
    def apogee(self) -> float:
        """
        Return the apogee of the celestial body.
        """
        return self.orbital_mechanics['apogee']

    @property
    def perigee(self) -> float:
        """
        Return the perigee of the celestial body.
        """
        return self.orbital_mechanics['perigee']

    @property
    def orbit_period(self) -> float:
        """
        Return the orbit period of the celestial body.
        """
        return self.orbital_mechanics['orbit_period']

    @property
    def rotation_period(self) -> float:
        """
        Return the rotation period of the celestial body.
        """
        return self.orbital_mechanics['rotation_period']

    @property
    def inclination(self) -> float:
        """
        Return the inclination of the celestial body.
        """
        return self.orbital_mechanics['inclination']

    @property
    def radius(self) -> float:
        """
        Return the radius of the celestial body.
        """
        return self.physical_properties['radius']

    @property
    def axial_tilt(self) -> float:
        """
        Return the axial tilt of the celestial body.
        """
        return self.physical_properties['axial_tilt']


class Constellation:
    """
    A class to represent a constellation.
    """

    def __init__(self,
                 name: str,
                 description: str,
                 location: Tuple[float]) -> None:
        """
        Constructs all the necessary attributes for the Constellation object.

        Parameters:
        name (str): the name of the constellation.
        description (str): a brief description of the constellation
        location (list): lat, long coordinates of the onjects on the skybox
        """
        self._name = name
        self._description = description
        self._location = location

    @property
    def name(self) -> str:
        """
        Returns the name of the constellation.
        """
        return self.name

    @property
    def description(self) -> str:
        """
        Returns the description of the constellation.
        """
        return self.description

    @property
    def location(self) -> tuple:
        """
        Returns the description of the constellation.
        """
        return self.location


class StarSystem:
    """
    A class to represent a star system. Only objects that orbit the star system
    barycenter should be included.
    """

    def __init__(self,
                 name: str,
                 location: Tuple[float],
                 bodies: Optional[List[CelestialBody]] = None) -> None:
        """
        Constructs all the necessary attributes for the StarSystem object.

        Parameters:
        name (str): the name of the star system
        location (list): a list mapping star system x, y, z coordinates
        bodies (list): a list of celestial bodies orbiting this barycenter.
        Default is None.
        """
        self._name = name
        self._location = location
        self._bodies = bodies or []

        self._generate_satellite_list()

    def _generate_satellite_list(self) -> None:
        """
        Updates the satellites list for each celestial body based on the parent
        attribute of other celestial bodies in the system.
        """
        for body in self._bodies:
            for potential_satellite in self._bodies:
                if potential_satellite.parent == body.name:
                    body.satellites.append(potential_satellite)

    @property
    def name(self) -> str:
        """
        Returns the name of the star system.
        """
        return self.name

    @property
    def location(self) -> tuple:
        """
        Returns the description of the star system.
        """
        return self.location

    @property
    def bodies(self) -> str:
        """
        Returns the bodies of the star system.
        """
        return self.bodies


class Skybox:
    """
    A class to represent the skybox as a sphere surrounding the star scape.
    """

    def __init__(self,
                 radius: int,
                 constellations: List[Constellation] | None = None) -> None:
        """
        Constructs all the necessary attributes for the Skybox object.

        Parameters:
        radius (float): the radius of the sphere.
        constellations (dict): a dictionary mapping star names to Constellation
        Objects. Default is an empty dict.
        """
        self._radius = radius
        self._constellations = constellations or []

    @property
    def radius(self) -> str:
        """
        Returns the name of the star system.
        """
        return self.radius

    @property
    def constellations(self) -> List[Constellation]:
        """
        Returns the description of the star system.
        """
        return self.constellations


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
        star_systems (List[StarSystem]): a list of star_system objects. Default
        is None.
        """
        self._name = name
        self.skybox = skybox
        self._star_systems = star_systems or []

    @property
    def name(self) -> str:
        """
        Returns the name of the StarCluster.
        """
        return self._name

    @property
    def star_systems(self) -> List[StarSystem]:
        """
        Returns the StarSystems within the StarCluster.
        """
        return self._star_systems
