"""
Cosmos Entities
================

This module provides a set of classes representing various celestial and
astronomical entities for a fantastical space simulation or astronomical
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

# THIS IS OUT OF DATE - REPLACE
# Usage:
# ------
# To use any of the classes, create an instance and provide the required
# parameters. For example, to create a new planet:

# >>> earth_info = {
# ...     'name': 'Earth',
# ...     'description': 'A pale blue dot.',
# ...     'body_type': 'planet',
# ...     'parent': 'Sun'
# ... }

# >>> earth_mechanics = {
# ...     'apogee': 1.0167,  # in AU, approximate aphelion distance
# ...     'perigee': 0.9833,  # in AU, approximate perihelion distance
# ...     'orbit_period': 365.25,  # in days
# ...     'rotation_period': 0.997,  # in days, approximately 23.93 hours
# ...     'inclination': 23.44  # axial tilt to its orbital plane
# ... }

# >>> earth_properties = {
# ...     'radius': 6371,  # in km, approximate average radius
# ...     'axial_tilt': 23.44  # in degrees
# ... }

# >>> earth = CelestialBody(general_info=earth_info,
# ...                        orbital_parameters=earth_mechanics,
# ...                        physical_properties=earth_properties)

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

# View locations will be added and dropped from an active list to make
# calculations faster. View locations will be merged so body positions will
# only be computed once. This is for satellites mostly.


class CelestialBody:
    """
    A class representing a celestial body within a star system.
    """

    def __init__(self,
                 general_info: Dict,
                 orbital_parameters: Dict,
                 physical_properties: Dict) -> None:
        """
        Initialize a CelestialBody with general information, orbital mechanics,
        and physical properties.
        """
        self.general_info = {
            'name': general_info['name'],
            'description': general_info['description'],
            'parent': general_info['parent'],
            'satellites': []
        }

        self.orbital_parameters = {
            'eccentricity': orbital_parameters['eccentricity'],
            'semi_major_axis': orbital_parameters["semi_major_axis"],
            'inclination': orbital_parameters["inclination"],
            'orbital_period': orbital_parameters["orbital_period"]
        }

        self.physical_properties = {
            'mass': physical_properties['mass'],
            'radius': physical_properties['radius'],
            'body_type': physical_properties['body_type'],
            'axial_tilt': physical_properties['axial_tilt'],
            'rotation_period': physical_properties['rotation_period']
        }

    # General Info
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

    # Orbital Paramters
    @property
    def eccentricity(self) -> float:
        """
        Return the eccentricity of the celestial body.
        """
        return self.orbital_parameters['eccentricity']

    @property
    def perigee(self) -> float:
        """
        Return the perigee of the celestial body.
        """
        return self.orbital_parameters['perigee']

    @property
    def semi_major_axis(self) -> float:
        """
        Return the semi major axis of the celestial body.
        """
        return self.orbital_parameters['semi_major_axis']

    @property
    def inclination(self) -> float:
        """
        Return the inclination of the celestial body.
        """
        return self.orbital_parameters['inclination']

    @property
    def orbital_period(self) -> float:
        """
        Return the orbital period of the celestial body.
        """
        return self.orbital_parameters['orbital_period']

    # Physical Properties
    @property
    def mass(self) -> float:
        """
        Return the mass of the celestial body.
        """
        return self.physical_properties['mass']

    @property
    def radius(self) -> float:
        """
        Return the radius of the celestial body.
        """
        return self.physical_properties['radius']

    @property
    def body_type(self) -> str:
        """
        Return the type of celestial body (e.g. star, planet, moon).
        """
        return self.physical_properties['body_type']

    @property
    def axial_tilt(self) -> float:
        """
        Return the axial tilt of the celestial body.
        """
        return self.physical_properties['axial_tilt']

    @property
    def rotation_period(self) -> float:
        """
        Return the rotational period of the celestial body.
        """
        return self.physical_properties['rotation_period']


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
    def location(self) -> Tuple[float]:
        """
        Returns a x,y coordinate location of the constellation.
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
        location (tuple): a list mapping star system x, y, z coordinates
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
        Returns a x,y,z coordinate location of the star system.
        """
        return self.location

    @property
    def bodies(self) -> List[CelestialBody]:
        """
        Returns the a list of CelestialBody objects in the star system.
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
        radius (float): the radius of the sphere in lightyears.
        constellations (dict): a dictionary mapping star names to Constellation
        Objects. Default is an empty dict.
        """
        self._radius = radius
        self._constellations = constellations or []

    @property
    def radius(self) -> str:
        """
        Returns the radius of the skybox in lightyears.
        """
        return self.radius

    @property
    def constellations(self) -> List[Constellation]:
        """
        Returns a list of Constellation objects in the skybox
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
