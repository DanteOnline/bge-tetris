import bpy
from core import delete_all

def create_simple_cube(location):
    bpy.ops.mesh.primitive_cube_add(location=location)
    return bpy.context.object

def create_simple_plane(location):
    bpy.ops.mesh.primitive_plane_add(location=location)
    plane = bpy.context.object
   
    return plane
    
if __name__ == '__main__':
    delete_all()
    create_simple_cube((0,0,0))
    create_simple_plane((1,1,1))