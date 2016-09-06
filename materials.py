import bpy
 
def makeMaterial(name, diffuse, specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = 'LAMBERT' 
    mat.diffuse_intensity = 1.0 
    mat.specular_color = specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.5
    mat.alpha = alpha
    mat.ambient = 1
    return mat
 
def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)
 
def run(origin):
    # Создание двух материалов
    red = makeMaterial('Red', (1,0,0), (1,1,1), 1)
    blue = makeMaterial('BlueSemi', (0,0,1), (0.5,0.5,0), 0.5)
 
    # Создание синего куба
    bpy.ops.mesh.primitive_cube_add(location=origin)
    setMaterial(bpy.context.object, red)
    # и красной сферы
    bpy.ops.mesh.primitive_uv_sphere_add(location=origin)
    bpy.ops.transform.translate(value=(1,0,0))
    setMaterial(bpy.context.object, blue)
 
if __name__ == "__main__":
    run((0,0,0))