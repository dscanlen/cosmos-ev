# cosmos-ev
A third party cosmology modelling module for the MUD framework Evennia.
This is a sandbox for people to break the laws of physics and abstract away some complexity to create a fantasy star system!
## Features:
 * Create massive multi-star systems environments
 * Populate star systems with all kinds of celestial object
 * Accurately portray distances  at both the intra-system (AU scale) and extra-system (light-year scale) level
 * Simplified barycenter of up to two objects at the center of a star system
 * Simplified orbital mechanics to allow for fantastical situations (black holes orbiting pluto? Sure!)
 * Build a skybox of distant stars and constellations beyond your multi-system environment
 * View the sky: calculate what celestial and skybox objects and are in the sky from characters location on a planet!
 * Day/Night cycle based on celestial bodies
 * Moon Cycles
 * Celestial events (eclipses, alignments, etc)
 * Planets with rings!
 * Run as an API either on your MUD server, a seperate compute server or even cloud-based serverless processes (such as AWS Lambda)
 * Non-gemometric bodies (want an astroid to hit your planet but don't want to figure out two intersecting elipses? Me either)

## What this is not:
This is not an accurate model of a solar system it is completely static.
 * There is no gravity, positions are computed geometrically
 * Celestial bodies will transit through each other with no interaction
