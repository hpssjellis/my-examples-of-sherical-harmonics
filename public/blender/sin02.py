import bpy, numpy as np
from scipy.special import sph_harm, spherical_jn
from mathutils import Vector
import math

# Parameters
l, m = 3, 2
radius = 1.0
radial_modes = [1, 2]  # number of radial peaks
steps = 64
frames = 120

# Create base sphere
bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, radius=radius)
obj = bpy.context.active_object
obj.name = f"SH_l{l}_m{m}"

# Add base shape key
obj.shape_key_add(name="Basis", from_mix=False)

# Create shape keys for each radial mode
theta_phi = []
for vert in obj.data.vertices:
    x, y, z = vert.co
    r = math.sqrt(x*x + y*y + z*z)
    theta = math.acos(z/r)
    phi = math.atan2(y, x)
    theta_phi.append((r, theta, phi))

for n in radial_modes:
    key = obj.shape_key_add(name=f"mode_n{n}", from_mix=False)
    for i, vert in enumerate(obj.data.vertices):
        r0, θ, φ = theta_phi[i]
        Y = sph_harm(m, l, φ, θ).real
        R = spherical_jn(n, math.pi*r0/radius)
        disp = Y * R * 0.3
        new_r = r0 + disp
        key.data[i].co = Vector((new_r*math.sin(θ)*math.cos(φ),
                                 new_r*math.sin(θ)*math.sin(φ),
                                 new_r*math.cos(θ)))

# Animate shape key mixing
for frame in range(frames):
    t = frame / frames * 2 * math.pi
    bpy.context.scene.frame_set(frame)
    for idx, n in enumerate(radial_modes, start=1):
        val = 0.5 + 0.5 * math.sin(n * t + m * math.pi / 4)
        obj.data.shape_keys.key_blocks[idx].value = val
        obj.data.shape_keys.key_blocks[idx].keyframe_insert("value")

