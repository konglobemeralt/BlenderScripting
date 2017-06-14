import bpy #Imports the Blender Python API
import mathutils #Imports Blender vector math utilities
import math #Imports the standard Python math library

for i in range(0, 5): 
    x = i * 3
    y = 3
    z = 1

    # Create a mesh cube in the scene
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))