# Implementation Plan

## 1. Scope and status

This plan implements [the agreed specification](solar-system-specification.md).

The first deliverable is a small end-to-end slice. It is not a reduced definition of the finished product. Rings, comets, the 3D designer, and background editing remain release requirements.

Weather, seasons, climate, and character knowledge remain host-game or separate-module responsibilities.

No implementation or performance claims follow from this document. All milestones below are pending.

### Workspace inspection

At planning time:

- The workspace contains the specification and no application code.
- No Evennia game project or Git repository exists in the workspace.
- Python 3.11.2, Node 24.21.0, and npm 11.19.0 are available.
- Evennia, NumPy, pytest, and maturin are not installed in the inspected Python environment.

These are environment observations, not the selected support matrix. Do not upgrade system tools or install application dependencies globally.

## 2. Implementation direction

### 2.1 Deep modules

Organize behavior behind a few small interfaces. Keep orbit mathematics, cache coordination, and host-game details out of presentation callers.

| Module | Interface responsibility | Hidden implementation |
| --- | --- | --- |
| Astronomy | Evaluate a system at a timestamp and observe it from a location | Orbits, frames, rotation, illumination, shadows, visibility |
| Observation runtime | Obtain a live or preview observation with provenance | Clock reads, snapshot refresh, prewarming, cache ownership, request coalescing |
| Configuration | Validate drafts and publish complete revisions | Persistence, asset references, conflicts, atomic revision changes |
| Presentation | Produce permitted text or browser data from observations | Ranking, authored text composition, optional host filtering |
| Evennia integration | Connect host time, locations, identity, and commands | Version-specific framework behavior and host adapters |

Browser renderers consume presentation data. They do not own a second astronomical simulation.

The astronomy module must remain usable without Django, Evennia, a database, or a running web server. Start with Python and typed immutable records.

Do not introduce an abstract Rust backend before measurements justify a second implementation. Numeric arrays and serialization should remain separable from framework objects.

### 2.2 Proposed source layout

Use `evennia_sky` as a working package name. Confirm naming availability before distribution.

```text
pyproject.toml
src/evennia_sky/
    astronomy/       # Public calculation interface and private numerical code
    runtime/         # Live snapshots, local observations, prewarming
    configuration/   # Validation, revisions, persistence integration
    presentation/    # Text and filtered browser payloads
    integration/     # Evennia time, locations, commands, web, permissions
    static/          # Built browser assets for distribution
    templates/       # Embedded browser pages
frontend/
    viewer/
    designer/
    shared/
examples/
    system/          # Small, deterministic system definition
    host_game/       # Documented integration example, not a city framework
tests/
    astronomy/
    runtime/
    integration/
    browser/
    performance/
docs/
```

The tree is organizational guidance, not a requirement for one class or interface per file.

### 2.3 Calculation interface

Start with these three operations inside one public astronomy interface:

- `compile_system(definition)` validates supported numerical inputs and prepares reusable data.
- `evaluate_system(compiled_system, game_time)` returns an immutable system snapshot.
- `observe(snapshot, location)` returns immutable physical observations.

These names are proposals, not a frozen public interface.

Keep validation reports distinguishable from exceptions. Invalid definitions should return actionable field errors. Unexpected numerical failures must retain diagnostic context.

Do not silently drop a body after a failed orbit solution. Mark an unsupported local observation explicitly when intentionally overlapping geometry makes it undefined.

Tests should exercise this interface. Internal numerical tests may supplement it, but must not replace end-to-end astronomical reference cases.

## 3. Data and mathematical conventions

Resolve and document these conventions before persistent schemas or browser editing depend on them.

### 3.1 Proposed canonical representation

- Stable identifiers independent of display names.
- Versioned, serializable system definitions.
- Explicit reference epoch and game seconds relative to that epoch.
- Float64 numerical calculations within a tested time and parameter range.
- Canonical SI lengths and periods in seconds internally.
- Radians internally, with degrees and labelled units in authoring controls.
- A right-handed system frame with the star at the origin and a fixed reference plane.
- Parent-relative orbital positions, composed into the system frame.
- Body-fixed longitude, latitude, and altitude for observing locations.

Allow more convenient authoring units at input and display. Convert once at the interface rather than throughout the implementation.

Reject non-finite values. Specify behavior at circular orbits, zero inclination, poles, the longitude seam, and angular wraparound.

### 3.2 Orbits and rotation

Propose standard bound Keplerian elements, with explicit period rather than mass-derived motion:

- Semi-major axis and eccentricity.
- Inclination, ascending-node longitude, and periapsis argument.
- Mean anomaly at the reference epoch.
- Orbital period.

Use one documented reference plane for orbital orientations in the first version. Parent translation must not silently rotate a child's orbital frame.

Use a safeguarded eccentric-anomaly solver with an iteration limit and convergence checks. Test high eccentricity within the declared supported range.

Document the distinction between:

- **Rotation period:** one turn relative to the fixed system frame.
- **Solar day:** the interval between corresponding appearances of the star in the local sky.

The designer must not label these as interchangeable. A synchronous body can lack a conventional sunrise/sunset cycle.

Use a fixed spin axis and reference rotation phase initially. Defer precession and nutation.

Propose a ring plane that translates with its planet but does not rotate with surface longitude. Equatorial alignment derives from the spin axis. Manual tilt sets a fixed plane orientation without introducing daily ring precession.

Validate this convention in the 3D prototype before freezing the schema.

### 3.3 Observation records

A physical observation should carry:

- Configuration revision, snapshot identifier, and authoritative game timestamp.
- Normalized observing location and local coordinate transform.
- Source-star direction and direct illumination, including shadow transmission.
- Per-body directions, distances, angular extents, phase, and brightness estimates.
- Visibility and occlusion information with reasons.
- Ring and comet geometry required by renderers.
- Model quality flags and documented approximation identifiers.

Keep authored names and descriptions attached through stable identifiers. Do not require the numerical core to construct prose or inspect characters.

Distinguish direct stellar irradiance from projected incidence on the local horizontal surface. State units and meanings so other modules can consume them safely.

Do not derive climate or a seasonal label from either quantity.

### 3.4 Initial optical models

Prototype and document these proposed approximations:

- Stellar luminosity from radius and effective temperature.
- A declared albedo convention and a compatible diffuse reflected-light phase law.
- Direct star-to-body-to-observer reflection without recursive mutual illumination.
- Finite stellar-disc coverage for partial eclipses, not only point-source shadow tests.
- Ring transmission from optical depth and ray angle.
- Deterministic finite-source sampling for combined occluders where analytic overlap is insufficient.
- An empirical atmosphere/glare model with separately adjustable clarity and sky colour.
- A comet activity curve and anti-stellar stylized tail.

Do not double-count overlapping eclipse shadows. Preserve bounded transmission between zero and one.

For rings, handle rays parallel to the plane, coplanar observers, and zero optical depth explicitly. A nearly parallel ray is not evidence that it intersects the finite annulus.

Use physical coordinates for shadow masks. Apply designer size exaggeration only after physical calculations.

A scaled diagram may not show literal ray alignment. Label it accordingly and provide a true-scale or selected-body diagnostic view.

## 4. Runtime and host integration

### 4.1 Time adapter

Use a host-supplied game-time adapter. Verify the appropriate Evennia integration against the selected release.

Never reconstruct game time in the browser from the refresh interval. The interval schedules evaluation; it does not define simulation speed.

Test pauses, rate changes, backward jumps, forward jumps, and process restarts. A host notification can invalidate snapshots immediately. A periodic refresh must still recover when no notification is available.

### 4.2 Location adapter

Resolve a host context to a planetary location without adding room coordinates or defining city typeclasses.

Keep three states distinct:

1. No values supplied: apply the agreed defaults.
2. Valid supplied values: use them.
3. Invalid supplied values: report an error.

Normalize equivalent coordinates for cache identity without snapping fractional values to whole degrees.

At a pole, position is unique but local compass orientation needs a convention. Choose and test a deterministic local basis there.

### 4.3 Shared snapshots and caches

Use immutable snapshots, identified by configuration revision and generation.

The normal refresh path is:

1. Read the current published revision and authoritative game time.
2. Evaluate every body's state at that one timestamp.
3. Make the complete snapshot available atomically.
4. Refresh designated high-traffic local observations.
5. Let other locations populate the observation cache on demand.

Default the real-time interval to 10 seconds. Validate configurable intervals against operational safety limits established during testing.

A request must use one complete snapshot. It must never mix old orbits with a newly published background or atmosphere definition.

Publishing a new revision invalidates prior live keys. Slow work for an older revision may finish, but cannot overwrite the current snapshot.

Prewarming and requests for the same key share in-flight work. A failed calculation must release ownership so subsequent requests can retry.

Bound both cache entries and bytes. Give live requests priority over arbitrary-time previews and arbitrary-coordinate exploration.

### 4.4 Multi-process integration gate

Do not assume the game server and website share Python memory, a clock instance, or a scheduler.

Milestone 0 must establish:

- Which process owns live refreshes and prewarming.
- How web workers read the authoritative game timestamp and published snapshot.
- How duplicate schedulers are prevented.
- Which cache data is shared across processes.
- Whether request coalescing is global or process-local.
- How a dead owner is detected and replaced.

Prefer facilities available in the supported Evennia deployment. Do not add Redis or a separate network service as a hidden installation requirement.

If the default deployment permits process-local observation caches, document bounded duplicate work across processes. Do not claim global single-flight without a shared ownership mechanism.

Test actual process separation before building the full editor.

### 4.5 Permissions and assets

Enforce permissions on the server, not only through hidden browser controls.

Separate the ability to view a current sky, explore other locations or times, edit drafts, and publish. Resolve the selected character through the host game, not a trusted browser-supplied identifier.

Apply knowledge and visibility filtering before serialization. A hidden label in a client payload is still disclosed information.

Use existing session authentication and the framework's request protections. Mutation requests require appropriate anti-forgery protection.

Bound uploaded asset size, decoded dimensions, and accepted formats. Escape authored text. Reject executable uploads and avoid arbitrary server-side URL fetching.

## 5. Delivery milestones

### M0 — Bootstrap and integration proof

**Goal:** establish a reproducible development environment and verify the framework seams.

Work:

- Create isolated Python and frontend development environments.
- Choose an actively supported Evennia release and compatible Python version from official documentation.
- Record exact versions and dependency constraints.
- Create package metadata and a disposable example game.
- Prove game-time access, authenticated web access, host location resolution, and command extension behavior.
- Prove the game/web snapshot handoff in separate processes.
- Select a minimal persistence and cache coordination approach.
- Add test and lint commands suitable for CI.

Primary documentation to verify includes Evennia's game time, web customization, commands, permissions, scheduling, and deployment documentation.

Do not copy an unverified dotted import path into the public integration guide.

**Exit gate:** a clean setup can run an import smoke test, an authenticated web smoke test, and the cross-process time/snapshot proof.

**Artifact:** `docs/development.md` with exact setup commands and an integration decision record.

### M1 — First playable vertical slice

**Goal:** demonstrate one physical observation through both Evennia and the browser.

Use a deterministic fixture with one star, one planet, one moon, and a small authored background catalogue.

Work:

- Add immutable definitions and validation.
- Implement circular-orbit cases, body rotation, and local coordinates first.
- Add the default planet and `[0, 0]` coordinate fallback, with zero altitude, through a host adapter.
- Return directions, angular sizes, moon phase, and basic horizon visibility.
- Use an airless preset for this slice to isolate geometry.
- Add the runtime snapshot and on-demand observation paths.
- Expose a concise sky command and object inspection through optional command integration.
- Render a selectable whole-sky chart from the same observation.
- Add basic identity checks and a server-side access policy from the start.

**Exit gate:** at a fixed game timestamp, text and browser identify the same moon, phase, location, and snapshot.

Repeated requests must not trigger repeated system evaluation. A second observing location must produce the expected different sky.

**Artifact:** a runnable demonstration and automated end-to-end tests. This is an internal slice, not the feature-complete release.

### M2 — Complete motion and observer geometry

**Goal:** cover the agreed orbital and surface model.

Work:

- Add eccentric and inclined orbits with parent composition.
- Add independent, retrograde, and synchronous rotation.
- Add stable axial orientation and epoch handling.
- Support fractional locations, both poles, the seam, and elevated observers.
- Add star and body angular extents rather than relying only on centre positions.
- Support observations from moons.
- Keep below-horizon objects available only through explicitly permitted astronomical inspection data.

**Exit gate:** analytic fixtures verify circular motion, eccentric periapsis/apoapsis, local noon, opposite longitudes, and synchronous libration.

An elevated observer must see the correct depressed horizon. The chart must not incorrectly discard all negative-altitude objects.

### M3 — Authoring foundation and 3D designer

**Goal:** let non-astronomers configure and understand the working model.

Work:

- Add versioned persisted definitions and immutable published revisions.
- Add draft editing, isolated preview time, validation, and atomic publication.
- Add conflict detection for concurrent draft edits and publication.
- Build body forms with units, plain-language help, and randomized starting values.
- Add a 3D orbit/axis preview, body selection, zoom, and time scrubbing.
- Implement the shared visual size multiplier and true-scale comparison.
- Add temperature/radius luminosity controls and the informational gravity guide.
- Add author-supplied appearance text, inspection text, and surface textures.
- Add server-side editor and publisher permissions and upload validation.

Propose TypeScript and Three.js for the 3D renderer. Select the dome renderer after testing label clarity and the 10,000-star workload.

Bundle production assets with the extension so game administrators do not need a frontend development server.

**Exit gate:** an administrator can create and preview a changed system without affecting players, then publish one consistent revision.

Changing diagram scale must not change any physical observation or relative body-radius ratio.

### M4 — Light, atmosphere, eclipses, and presentation

**Goal:** turn geometry into useful visible-sky observations.

Work:

- Implement the declared stellar and reflected-light models.
- Add albedo controls and presets without inventing surface descriptions.
- Add airless and Earth-like visibility, twilight, clarity, and sky-colour controls.
- Add partial/full eclipses, transits, occultations, and planetary shadows on moons.
- Add stable ranked summaries and focused inspection with ambiguity handling.
- Add host-defined knowledge and external visibility hooks.
- Support restricted and exploratory browser modes and the astronomical overlay.

**Exit gate:** a deterministic set of reference scenes produces consistent text, visibility decisions, shadow states, and browser data.

A denied name or detail must be absent from serialized browser data, not merely hidden visually.

### M5 — Rings and comets

**Goal:** deliver the prominent non-spherical sky features required for the initial release.

Work:

- Add ring inner edge, continuous width, orientation, optical depth, and authored descriptions.
- Add ring intersection and light-transmission calculations.
- Add ring shadows on planets and planetary shadows on rings.
- Render visible ring segments with horizon and body occlusion.
- Add periodic comets, activity controls, colours, and anti-stellar tails.
- Integrate these observations into rankings and object inspection.

**Exit gate:** transparent, opaque, tilted, and edge-on ring fixtures remain numerically stable and visually consistent with physical observations.

A ring-shadowed surface location must receive less direct starlight. Comet activity must reproduce at the same timestamp and configuration.

Start a focused ring-shadow feasibility test during M2. Do not postpone this numerical risk until the rest of the editor is complete.

### M6 — Background generation and editing

**Goal:** let administrators use either generated or fully authored background skies.

Work:

- Persist structured stars, constellations, and decorative layers.
- Implement deterministic generation with a versioned algorithm and explicit seed.
- Add density/count, brightness, colour, and galactic-band controls.
- Sample a sphere correctly rather than using uniformly sampled latitude.
- Save generated results before manual editing.
- Add browser placement, selection, grouping, naming, and description editing.
- Support safe image layers without assuming they contain identifiable celestial objects.
- Integrate background publication with the complete configuration revision.

**Exit gate:** a saved sky survives restarts unchanged, rotates correctly for local observers, and shows no translation-induced parallax.

Increasing the background catalogue must not force every star into the in-game summary.

### M7 — Load, failure recovery, packaging, and release

**Goal:** meet a measured operating target and ship a documented extension.

Work:

- Finish prewarming, cache limits, duplicate-request coalescing, and rate limits.
- Benchmark live viewing, text requests, cache misses, and preview abuse together.
- Test publication during active requests and snapshot-owner failure.
- Measure actual multi-process behavior, not only isolated function speed.
- Profile before introducing vectorization, compiled code, or new infrastructure.
- Package built browser assets and verify installation in a clean example game.
- Write administrator setup, authoring, host integration, approximation, and troubleshooting guides.
- Document extension points for external weather, climate, season, and knowledge modules.

**Exit gate:** all specification requirements have tests or documented manual acceptance checks. The agreed benchmark passes on recorded hardware.

Do not advertise support beyond the tested version matrix or call a benchmark result a universal capacity guarantee.

## 6. Verification strategy

### 6.1 Numerical evidence

Use analytic synthetic fixtures as the primary references. These systems allow deliberately independent masses, periods, and radii.

Use an independent implementation for selected orbit and frame checks where useful. Do not validate the implementation only against formulas copied from itself.

Proposed starting tolerances for ordinary, nondegenerate geometry:

- Kepler equation residual: at most `1e-12` radians.
- Relative orbital position error: at most `1e-9` of semi-major axis in reference cases.
- Direction agreement: at most `1e-7` radians where direction is defined.
- Analytic unobscured phase and overlap fractions: absolute error at most `1e-6` away from tangent boundaries.
- Sampled shadow transmission: convergence to within one percentage point on selected reference scenes.

These are engineering proposals. Validate them against supported parameter ranges before adopting them as release promises.

Separate numerical accuracy from model fidelity. A precisely computed empirical atmosphere is still an approximation.

### 6.2 Browser and integration evidence

- Assert shared identifiers, timestamps, and values between browser payloads and text input records.
- Use screenshot tests for stable reference scenes, not as the sole astronomy oracle.
- Test clock and publication changes during concurrent requests.
- Test anonymous, restricted-player, explorer, editor, and publisher access separately.
- Test character switching and stale browser tabs.
- Test malformed definitions, non-finite numbers, oversized uploads, and cache-flood attempts.
- Verify that external visibility and knowledge hooks cannot contaminate another character's shared result.

### 6.3 Proposed benchmark protocol

Retain the agreed target of 100 orbiting bodies, 10,000 background stars, and 150 browser viewers.

Propose this initial workload for calibration:

| Scenario | Workload |
| --- | --- |
| Steady browsers | 150 viewers refresh every 10 real seconds, with staggered requests |
| Synchronized refresh | All 150 viewers request immediately after a new snapshot |
| Shared city | 150 viewers request the same prewarmed location |
| Distinct locations | 150 viewers request distinct locations each snapshot |
| Game-command burst | 100 sky/inspection requests per second for 10 seconds, alongside browsers |
| Uncached exploration | Bounded unique-coordinate and arbitrary-time queries |
| Sustained run | At least 30 minutes with repeated refresh and publication cycles |

Proposed initial goals on a recorded reference machine:

- Warm observation-request p95 below 200 ms, excluding WAN delay and browser rendering.
- Cold observation-request p95 below 1 second under the agreed concurrent workload.
- System refresh plus configured prewarming completes before the next default refresh deadline.
- Resident memory remains bounded by configured caches and assets.
- One system evaluation per generation under the selected ownership model.
- Duplicate local work does not exceed the documented coalescing scope.
- Rate-limited requests receive controlled responses without disrupting permitted viewers.

These workload details and latency thresholds are proposals, not already proven capacity. Record hardware, process count, dependency versions, and measurement method with every result.

For browser tests, measure rendering and selection responsiveness separately from server latency. Track payload bytes and avoid repeatedly downloading an unchanged star catalogue.

## 7. Risk-driven sequencing

| Risk | Early proof | Response if the proof fails |
| --- | --- | --- |
| Game/web clock or cache divergence | M0 separate-process test | Change the ownership and handoff design before adding callers |
| Inconsistent orbital and texture frames | M1/M2 fixed reference scenes | Fix conventions before persisting author content |
| Ring shadows exceed the time budget | M2 numerical feasibility test | Tune deterministic sampling or optimize the measured hot path |
| Diagram scaling misleads authors | M3 true-scale comparison | Improve labels and diagnostics without changing physical geometry |
| Background data dominates requests | M1 payload measurement, M6 full catalogue | Reuse versioned static data and optimize batched transforms |
| Character information leaks through shared caches | M1 access tests, M4 filtering tests | Keep raw caches private and filter before serialization |
| Extreme fantasy inputs cause undefined math | M2 stress fixtures | Narrow documented ranges or report explicit unsupported observations |
| Python cannot meet measured load | M7 profiles, earlier microbenchmarks | Optimize specific calculations behind the astronomy interface |

Rings and the 3D designer must not silently disappear if they prove difficult. Any reduction in agreed release scope requires an explicit product decision.

## 8. First implementation work queue

Execute these in order:

- [ ] Verify a supported Evennia/Python combination and create isolated tooling.
- [ ] Bootstrap package metadata, test commands, and an example host game.
- [ ] Prove authoritative time and shared snapshot handoff across game and web processes.
- [ ] Record frames, units, epoch, rotation, and error conventions.
- [ ] Add a deterministic star/planet/moon fixture and immutable records.
- [ ] Implement and test the circular-orbit observation path.
- [ ] Add the host location adapter and fallback/error behavior.
- [ ] Add one live snapshot path and bounded on-demand observation cache.
- [ ] Expose one optional sky command and one authenticated observation endpoint.
- [ ] Render one selectable dome chart from the endpoint.
- [ ] Verify text/browser agreement and repeated-request reuse.
- [ ] Demonstrate the slice before expanding to the complete orbital model.

This queue starts implementation without committing the project to the full editor or a speculative compiled backend first.
