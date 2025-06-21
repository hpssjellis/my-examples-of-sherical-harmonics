import bpy
import bmesh
import math
import cmath
import numpy as np
from mathutils import Vector
from scipy.special import sph_harm

# Parameters
l = 3  # Degree
m = 2  # Order
radius = 1
resolution = 100  # Grid resolution

# Cleanup existing object (optional)
for obj in bpy.context.scene.objects:
    if obj.type == 'MESH' and obj.name.startswith("SphericalHarmonic"):
        bpy.data.objects.remove(obj, do_unlink=True)

# Generate spherical grid
theta = np.linspace(0, np.pi, resolution)
phi = np.linspace(0, 2 * np.pi, resolution)
theta, phi = np.meshgrid(theta, phi)

# Compute spherical harmonic values (complex)
Y_lm = sph_harm(m, l, phi, theta)
Y_magnitude = np.abs(Y_lm)

# Convert spherical to Cartesian coordinates
x = radius * Y_magnitude * np.sin(theta) * np.cos(phi)
y = radius * Y_magnitude * np.sin(theta) * np.sin(phi)
z = radius * Y_magnitude * np.cos(theta)

# Flatten arrays for mesh creation
vertices = [Vector((float(x[i][j]), float(y[i][j]), float(z[i][j])))
            for i in range(resolution) for j in range(resolution)]

# Generate face indices
faces = []
for i in range(resolution - 1):
    for j in range(resolution - 1):
        v1 = i * resolution + j
        v2 = v1 + 1
        v3 = v1 + resolution + 1
        v4 = v1 + resolution
        faces.append([v1, v2, v3, v4])

# Create mesh and object
mesh = bpy.data.meshes.new("SphericalHarmonicMesh")
mesh.from_pydata(vertices, [], faces)
mesh.update()

obj = bpy.data.objects.new("SphericalHarmonic", mesh)
bpy.context.collection.objects.link(obj)

# Smooth shading
mesh.polygons.foreach_set("use_smooth", [True] * len(mesh.polygons))
