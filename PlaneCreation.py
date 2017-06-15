import bpy

#Define vertices, faces
#The vertex array contains 4 items with X, Y, and Z definitions
verts = [(0, 0, 0), (0, 5, 0), (5, 5, 0), (5, 0, 0)]

# the faces array contains 1 item.  
# The number sequence refers to the vertex array items.
# The order will determine how the face is constructed.
faces = [(0, 1, 2, 3)]

#define mesh and object
myMesh = bpy.data.meshes.new("Plane")

#the mesh variable is then referenced by the object variable
myObject = bpy.data.objects.new("Plane", myMesh)

#Set location and scene of object
myObject.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(myObject)

# Empty array could be list of edges.
myMesh.from_pydata(verts,[],faces)
myMesh.update(calc_edges = True)





