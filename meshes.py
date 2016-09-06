import bpy
from core import delete_all
from materials import makeMaterial, setMaterial

def create_simple_cube(location, material=None):
    bpy.ops.mesh.primitive_cube_add(location=location)
    if material != None:
        setMaterial(bpy.context.object, material)
    
if __name__ == '__main__':
    delete_all()
    create_simple_cube((0,0,0))
    red = makeMaterial('Red', (1,0,0), (1,1,1), 1)
    create_simple_cube((3,3,0),red)