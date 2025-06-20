
import bpy
import math

# Clear existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Create a sphere representing a planet
bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 0), radius=1)
planet = bpy.context.active_object
planet.name = "Planet"

# Add sinusoidal displacement using a displacement modifier
displace = planet.modifiers.new(name="SinePerturbation", type='DISPLACE')
texture = bpy.data.textures.new("SineTexture", type='DISTORTED_NOISE')
texture.distortion = 5
texture.noise_scale = 0.5
displace.texture = texture
displace.strength = 0.1

# Animate sinusoidal perturbation
for frame in range(0, 250):
    displace.strength = 0.1 * math.sin(frame * 0.1)
    displace.keyframe_insert(data_path="strength", frame=frame)
