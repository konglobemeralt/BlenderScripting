import bpy
 
verts = [(0,0,0),(0,5,0),(5,5,0),(5,0,0),(0,0,5),(0,5,5),(5,5,5),(5,0,5)]
faces = [(0,1,2,3), (4,5,6,7), (0,4,5,1), (1,5,6,2), (2,6,7,3), (3,7,4,0)]
 
mesh = bpy.data.meshes.new("Cube")
object = bpy.data.objects.new("Cube", mesh)
 
object.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(object)
 
mesh.from_pydata(verts,[],faces)
mesh.update(calc_edges=True)