
import bpy
import math

# Parameters
num_planets = 5
frames = 250
sun_radius = 1
orbit_base_radius = 3
orbit_gap = 2

# Clean up
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Add the sun
bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 0), radius=sun_radius)
sun = bpy.context.active_object
sun.name = "Sun"

# Add planets with sinusoidal orbits
for i in range(num_planets):
    planet_radius = 0.3
    phase = i * (math.pi / 4)
    base_radius = orbit_base_radius + i * orbit_gap

    bpy.ops.mesh.primitive_uv_sphere_add(radius=planet_radius, location=(base_radius, 0, 0))
    planet = bpy.context.active_object
    planet.name = f"Planet_{i}"

    # Animate orbit with sinusoidal radial perturbation
    for frame in range(frames):
        t = frame / 10.0
        r = base_radius + 0.4 * math.sin(t + phase)
        x = r * math.cos(t)
        y = r * math.sin(t)
        z = 0

        planet.location = (x, y, z)
        planet.keyframe_insert(data_path="location", frame=frame)
