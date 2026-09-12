# Evennia Solar System and Sky Extension

## 1. Purpose

Provide a configurable solar system whose geometry determines what observers see from locations on spherical planets and moons.

The same observations drive concise in-game descriptions and a browser sky map. A browser designer lets administrators create and preview the system.

This document records the agreed product scope. It does not select an Evennia version, rendering library, or final implementation API.

## 2. Design principles

1. Keep astronomical geometry consistent across all views.
2. Use prescribed motion instead of gravitational simulation.
3. Allow fictional systems without enforcing gravitational consistency or long-term stability.
4. Keep calculations independent of Evennia objects, persistence, and web requests.
5. Share calculations across observers and requests where possible.
6. Keep authored appearance separate from calculated physical conditions.
7. Let the host game own its locations, characters, permissions, knowledge, and primary clock.
8. Explain approximations in the editor and documentation.

Weather, seasons, and climate belong to separate modules. They are not deferred features of this extension.

## 3. Domain model

### 3.1 Solar system

The initial version supports one solar system with:

- One central star.
- Planets orbiting the star.
- Moons orbiting planets.
- Periodic comets orbiting the star.
- Rings attached to planets.
- A distant background sky.

Bodies follow prescribed, bound elliptical orbits. Their orbital periods are explicit, editable properties.

Mass does not determine orbital motion. The extension does not solve mutual gravitational interactions, barycentric motion, or orbital stability.

An orbit definition must contain enough information to reproduce position at any supported game timestamp. This includes orbital size, eccentricity, orientation, period, and phase at a reference epoch.

Exact field names and coordinate conventions remain implementation decisions. The designer must explain each field with units, plain-language help, and visual feedback.

### 3.2 Star

The central star remains at the system origin in the initial model.

Administrators configure its radius and temperature/colour through controls with useful presets. The extension derives luminosity from radius and temperature.

The temperature/colour control represents a coherent stellar temperature choice, not an unrelated RGB value. Preview exposure must remain separate from physical luminosity.

### 3.3 Planets and moons

Planets and moons have perfect spherical reference surfaces. Their properties include:

- Radius.
- Orbital definition and parent body.
- Rotation mode, period, direction, axis orientation, and reference phase.
- Base visual colour and albedo.
- Optional author-supplied surface texture.
- Atmosphere settings.
- Authored names and descriptions.

The module does not derive geography, composition, climate, or terrain from a texture or description.

Planetary moons can serve as observing worlds, using the same spherical location model as planets.

### 3.4 Rotation

Support two rotation modes:

- **Independent:** an editable rotation period and direction.
- **Synchronous:** one rotation per orbit around the parent.

Support retrograde rotation and configurable axial tilt.

Synchronous rotation is not an artificial constraint that fixes the parent at one sky position. Eccentric orbits can produce apparent back-and-forth motion.

### 3.5 Informational gravity guide

The designer provides a surface-gravity estimate using Earth-like mean density by default.

Under that assumption:

- Estimated mass scales with radius cubed.
- Estimated surface gravity scales with radius.

Label the density assumption and distinguish weight from mass. This guide does not affect orbits, rotation, illumination, or other simulation calculations.

Authors can use hollow or fractured planets as worldbuilding explanations. The initial geometry still treats these bodies as intact spheres.

## 4. Observing locations

### 4.1 Coordinates

An observing location consists of:

- Planetary body reference.
- Longitude.
- Latitude.
- Altitude above the body's reference sphere.

Use `[longitude, latitude]`, with east-positive longitude and north-positive latitude. Accept fractional degrees.

Whole-degree coordinates are a placement convenience, not a simulation grid. Do not create or continuously update a database object for every degree intersection.

The longitude seam represents one meridian. `-180°` and `+180°` do not identify distinct places. All longitudes at a given pole identify the same surface point.

Altitude defaults to zero. Elevated observers use the spherical horizon appropriate to their altitude. Terrain obstruction is not part of this calculation.

### 4.2 Host-game ownership

The host game owns cities, regions, areas, and their relationships to rooms.

Rooms do not receive planetary coordinates from this extension. The host game resolves a room or other context to its associated planetary location.

The integration must accept resolved coordinates without requiring a particular city or region typeclass.

### 4.3 Defaults and errors

Administrators must select a default observing planet during setup.

When observing coordinates are absent, use longitude `0°`, latitude `0°`, and altitude zero. When a planet assignment is absent, use the default planet.

An explicitly supplied unknown planet is an error, not a reason to use the default. Invalid supplied coordinate values must not silently become valid fallback locations.

The host game controls whether a character has access to a view of the sky, including indoor restrictions.

## 5. Time and reproducibility

Evennia's primary game time is authoritative. This extension does not independently control time speed, pauses, or progression during downtime.

A time integration interface supplies a game timestamp suitable for orbital and rotational calculations.

For the same configuration, observing location, and game timestamp, the calculation core must return the same observations within documented numerical tolerances.

All bodies in a shared snapshot use the same timestamp. The browser and in-game descriptions must identify and use that snapshot consistently.

Preview queries accept a chosen game timestamp without changing the live game clock. Clock discontinuities must invalidate or bypass stale live observations.

## 6. Astronomical observations

### 6.1 Required calculations

Calculate observer-relative information sufficient for both text and graphics, including:

- Direction, including altitude and azimuth.
- Horizon relationship, including elevated observers.
- Distance and apparent angular size.
- Illumination and phase where applicable.
- Approximate apparent brightness.
- Occlusion by other bodies.
- Relevant eclipse, transit, and shadow state.
- Visibility under the configured atmosphere and daylight conditions.

Albedo, illumination geometry, and distance affect reflected-light brightness. Authored descriptive language does not override these calculations.

The implementation must document its photometric approximations and supported accuracy. Detailed radiative transfer is not required.

### 6.2 Eclipses, transits, and occultations

Include basic spherical geometry for:

- A moon or planet crossing the stellar disc.
- One body hiding another from an observer.
- A moon entering its planet's shadow.
- Partial and complete overlap where applicable.

The resulting state must agree across the local sky map and text. A shadow on an observing location must affect direct illumination there.

Atmospheric eclipse reddening and other detailed optical effects are outside the initial scope.

The initial version describes sampled sky states. It does not promise notifications for every event between snapshots.

### 6.3 Atmospheres

Provide airless and Earth-like presets, with basic atmospheric clarity and sky-colour controls.

Use a documented approximation for daylight glare, twilight, and visibility. An airless world must not inherit an Earth-like blue daytime sky or atmosphere-based visibility rules.

Do not calculate clouds, weather, detailed light scattering, or atmospheric refraction.

Default views show objects that pass the visibility model. An optional browser overlay shows astronomical positions even when glare hides those objects.

External modules may supply additional visibility conditions, such as cloud cover, through an integration hook.

## 7. Rings

Model a ring as a flat circular band with negligible vertical thickness, without individual particles.

Configurable properties include:

- Inner-edge distance from the planet.
- Continuous radial width.
- Orientation, with the equatorial plane as the default.
- Uniform optical depth.
- Authored appearance and inspection descriptions.

Width uses a slider with a corresponding numeric input. Express dimensions clearly relative to the planet's radius, with physical-unit equivalents where useful.

A transparent-to-opaque control sets optical depth. Light transmission depends on optical depth and the angle through the ring.

Include ring shadows on the planet and the planet's shadow on its rings. These effects must appear in the relevant previews and local observations.

The calculation design must handle edge-on geometry without numerical singularities. The numerical method and shadow sampling remain implementation decisions.

The initial optical model has no radial bands or gaps. Its interface should permit a future radial optical-depth function.

Authored descriptions can mention richer structure, such as braided dust ribbons. Such language does not imply simulated gaps, particles, or corresponding shadow detail.

## 8. Comets

Comets use prescribed, bound elliptical orbits around the star.

Support:

- Editable appearance colours, including tail colour.
- A simple, configurable activity and brightness model based on proximity to the star.
- A stylized tail directed away from the star.
- Authored appearance and inspection text.

Comet activity and appearance must use the same timestamp as other observations. Document that the tail is an approximation, not a detailed dust or plasma simulation.

Unbound visitors, fragmentation, and detailed comet dynamics are outside scope.

## 9. Background sky

### 9.1 Reference frame

Represent the distant sky as fixed directions in the solar system's reference frame.

The background is effectively infinitely distant. Travel within the solar system does not introduce background parallax.

Planetary rotation still makes background objects rise and set. Different observing latitudes and axes produce different local sky orientations.

### 9.2 Authored content

Support:

- Stars with direction, brightness, colour, and optional name.
- Constellation groupings with names and descriptions.
- Decorative image layers, such as nebulae or a galactic band.

Structured content supports both maps and text. Images alone do not automatically produce named objects or textual descriptions.

### 9.3 Seeded generation

Administrators can generate a starting sky instead of placing individual stars.

Generation controls include:

- Seed.
- Star count or density.
- Brightness distribution.
- Colour distribution.
- An optional galactic band and its appearance settings.

Generation should produce an artistic starfield with plausible defaults, not a physical galaxy simulation.

Save the generated catalogue so requests and restarts do not create a new sky. Administrators can edit the result before publication.

## 10. Player presentation

### 10.1 Text levels

Provide three levels of output:

1. **Ambient summary:** a short phrase or sentence, such as “Two crescent moons hang in the night sky.”
2. **Explicit sky view:** a selective, more descriptive summary of prominent sights.
3. **Object inspection:** focused detail, such as `look sky comet`.

The exact Evennia command integration remains configurable. These examples describe the intended interaction, not a requirement to replace a game's existing `look` command.

Prioritize significant visible phenomena rather than listing every object. Relevant examples include eclipses, conspicuous comets, moons, and bright planets.

Do not describe weather as a calculated astronomical fact. For example, “clear sky” requires external visibility information rather than an assumption of no clouds.

### 10.2 Authored and calculated content

Bodies and rings support:

- A short appearance phrase.
- A longer inspection description.
- Separate calculated observational facts.

The module combines authored appearance with current conditions. It does not generate surface geography or require an authored paragraph for every possible phase.

Descriptions and textures are author-supplied. An untextured body uses its configured base colour.

### 10.3 Knowledge hooks

The module exposes observations and optional presentation hooks. The host game decides which names and facts a character can access.

Do not define an astronomy skill, knowledge model, or character progression system here.

Character-specific presentation must remain separate from shared physical caches. Both browser and text integrations must permit the host game's filtering rules.

## 11. Browser viewer

The initial player viewer is a whole-sky dome chart:

- Zenith at the centre.
- Horizon around the edge.
- Compass direction labels.
- Selectable objects with descriptions.
- Visibility-filtered display by default.
- An optional astronomical-position overlay.

Use calculated angular sizes. Clearly distinguish optional selection markers from physical object discs.

Support both a restricted current-character view and exploration of other locations or timestamps. The host game's access policy controls availability.

The browser renders the scene. It does not independently advance the authoritative game clock.

## 12. Browser designer

### 12.1 System editing

Provide a basic interactive 3D system designer in the initial version.

Show selected orbits, orbital planes, and rotation axes. Changes to inclination and tilt must provide immediate visual feedback.

New bodies receive randomized, editable starting values appropriate to their type and parent. These values are suggestions, not orbital stability guarantees.

Provide a working example system. Full procedural solar-system generation is outside the initial scope.

### 12.2 Scale and preview

Default to a labelled diagram view:

- Keep orbital distances proportional.
- Apply one adjustable visual size multiplier to all bodies, preserving relative radii.
- Keep labels and selection markers distinct from scaled physical surfaces.
- Permit closer inspection of a planet and its moons.
- Provide a true-scale comparison mode.

Visual scaling must not change physical parameters or calculations. Shadow calculations use physical geometry, not enlarged diagram geometry.

Provide a time scrubber that affects only the preview.

### 12.3 Validation and publication

Use a draft → preview → publish workflow for system and background edits.

Publishing applies one complete configuration revision and invalidates affected live caches. Warn that changed physical parameters can cause a discontinuity in the live sky.

Reject unsupported or mathematically invalid inputs, including nonpositive radii, invalid parent relationships, and unbound orbits.

Warn about questionable configurations, such as overlapping bodies or potentially intersecting orbits. Allow publication where the model can still evaluate them safely.

Do not claim that warnings constitute a gravitational stability analysis.

## 13. Evennia integration and boundaries

Deliver the browser tools through Evennia's existing web application. Do not require separate user accounts or a separate astronomy network service.

Use existing identity and permission mechanisms. Administrators control access to viewing, unrestricted exploration, editing, and publication.

Define narrow integration interfaces for:

- Authoritative game time.
- Host-game location resolution.
- Access policy and optional character-specific presentation.
- Optional external visibility conditions.
- Structured astronomical data for other modules.

Keep the calculation core independent of these adapters. Python is the initial implementation direction, subject to measurement.

A compiled implementation, including Rust, can replace expensive calculations behind this boundary if profiling justifies it. No language choice removes the need for request limits and caching.

Weather, seasons, and climate modules may consume timestamps, orbital state, illumination, daylight, eclipses, and local sky geometry. This module does not turn those inputs into climate or weather predictions.

## 14. Caching and load handling

### 14.1 Shared system snapshots

Use a configurable real-time refresh interval, defaulting to 10 seconds.

Each snapshot contains body positions, orientations, and other reusable system state at one authoritative game timestamp.

Do not calculate every possible surface location during a refresh.

### 14.2 Local observations

Calculate local observations on demand from a shared snapshot.

Cache keys must distinguish at least:

- Published configuration revision.
- Snapshot identity and game timestamp.
- Planetary body.
- Normalized longitude, latitude, and altitude.
- Any physical observation settings that change the result.

Administrators can designate high-traffic host-game locations for automatic cache refresh with each snapshot.

Repeated requests for one location reuse its physical observations. Character-specific access and prose filtering occur outside that shared cache.

### 14.3 Request safeguards

- Combine simultaneous requests for the same uncached observation into one calculation.
- Bound cache storage and evict inactive entries.
- Limit abusive request rates.
- Keep static background data loaded or otherwise reusable.
- Keep draft and arbitrary-time preview caches separate from live observations.
- Prevent arbitrary coordinate queries from creating unbounded memory use.

A slow refresh interval or fast game clock can cause visible jumps or miss brief events. Document this trade-off and expose the interval clearly.

Browser refreshes do not each require a new system calculation.

### 14.4 Initial benchmark target

Test with:

- 100 orbiting bodies.
- 10,000 background stars.
- 150 simultaneous browser viewers at potentially distinct observing locations.
- Bursty in-game sky and object-inspection requests alongside browser traffic.

These are benchmark targets, not proven capacity or product limits.

Test cold caches, warm caches, prewarmed locations, concurrent duplicate requests, and arbitrary-location traffic. Record latency, CPU, memory, cache hit rates, and duplicate calculation counts.

Request burst rates and acceptable latency thresholds must be set before the performance gate. They are not yet agreed.

## 15. Verification requirements

The implementation plan must include tests for:

- Reproducible body state at a given configuration and timestamp.
- Known orbital and rotational reference cases.
- Coordinate seams, poles, fractional positions, and elevated horizons.
- Independent, retrograde, and synchronous rotation.
- Observer-dependent phases, eclipses, transits, and occultations.
- Ring transmission and shadows, including edge-on cases.
- Airless versus atmospheric visibility.
- Seeded sky generation and persisted catalogue stability.
- Agreement between text and browser physical observations.
- Location fallback versus invalid explicit references.
- Preview isolation from live game time and configuration.
- Publication and clock-change cache invalidation.
- Permission enforcement without cross-character data leakage.
- Cache bounds, duplicate-request coalescing, and the stated benchmark workload.

Numerical tolerances and reference datasets belong in the implementation plan. Visual checks alone are not sufficient for astronomy correctness.

## 16. Scope exclusions

### Separate-module responsibilities

- Weather.
- Seasons and climate.
- Skills and knowledge.
- Host-game cities, regions, areas, and room relationships.

### Outside the initial version

- Multiple stars and barycentric arrangements.
- N-body gravity and long-term stability analysis.
- Terrain, biome, and topographic modelling.
- Irregular planetary silhouettes, actual fractured bodies, and particle dynamics.
- Moving spacecraft observers.
- Unbound visitors and comet fragmentation.
- Detailed scattering, refraction, and atmospheric eclipse reddening.
- Radial ring bands and gaps in the optical model.
- A physical galaxy simulation or mandatory real-world star catalogue.
- Full procedural solar-system generation.
- A first-person panoramic player viewer.

## 17. Technical decisions still to validate

Resolve these through repository inspection, prototypes, and implementation planning rather than treating them as agreed product requirements:

- Supported Evennia and Python versions, packaging, and web integration points.
- Game-time epoch, units, precision, and clock-change detection.
- Exact coordinate-frame and orbital-element conventions.
- Brightness, atmosphere, comet activity, and finite-source shadow approximations.
- Ring orientation behavior relative to the body and system frames.
- Renderer, texture projection, asset formats, and upload limits.
- Persistence, publication transactions, and multi-process cache coordination.
- Default description ranking and ambiguous object-selection behavior.
- Numerical tolerances, supported parameter ranges, and performance thresholds.

The next step is technical planning against an actual Evennia environment. This specification does not authorize additional product scope by implication.
