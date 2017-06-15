import bpy
 
verts = [(0,0,0),(0,5,0),(5,5,0),(5,0,0),(2.5,2.5,4.5)]
faces = [(0,1,2,3), (0,4,1), (1,4,2), (2,4,3), (3,4,0)]
 

mesh = bpy.data.meshes.new("Pyramid")
object = bpy.data.objects.new("Pyramid", mesh)
 
object.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(object)
 
mesh.from_pydata(verts,[],faces)
mesh.update(calc_edges=True)