import bpy
 
#Define vertices, faces, edges for a cube
verts = [(0,0,0),(0,5,0),(5,5,0),(5,0,0),(0,0,5),(0,5,5),(5,5,5),(5,0,5)]
faces = [(0,1,2,3), (7,6,5,4), (0,4,5,1), (1,5,6,2), (2,6,7,3), (3,7,4,0)]
 
#Define mesh and object bla bla bla
myMesh = bpy.data.meshes.new("Cube")
myObject = bpy.data.objects.new("Cube", myMesh)
 
#Set location and scene of the cube
myObject.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(myObject)
 
#Create the cube mesh
myMesh.from_pydata(verts,[],faces)
myMesh.update(calc_edges=True)

#subdiv modifier
myObject.modifiers.new("subd", type = 'SUBSURF')

#increase subdivisions 
myObject.modifiers['subd'].levels = 5

#smooth shading
myPolys = myMesh.polygons
for polygon in myPolys:
    polygon.use_smooth = True

