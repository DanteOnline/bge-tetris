import bpy
from core import delete_all, select_by_names, deselect_by_names
from materials import makeMaterial, setMaterial
from meshes import create_simple_cube

#Создание 3-х кубов подряд
#count - количество кубов
#возвращаем список имен объектов
def create_cube_line(count, x=0,y=0,z=0,material=None):
    #шаг
    step = 2
    #делаем 4 куба
    name_list = []
    for i in range(count):
        cube = create_simple_cube((x+step*i,y,z))
        name_list.append(cube.name)
        setMaterial(cube, material)
    return name_list

#Создаем палку из 4-х кубиков
def create_line(x=0,y=0,z=0):
    #палка будет красной
    material = makeMaterial('Red', (1,0,0), (1,1,1), 1)
    name_list = create_cube_line(4,x,y,z,material)
    #снимаем отметку со всех элементов
    bpy.ops.object.select_all(action='TOGGLE')
    #выделяем нужные кубы по имени
    select_by_names(name_list)
    bpy.ops.object.join()
        
#создаем букву г
def create_g_r(x=0,y=0,z=0):
    #сначала создаем палку из 3-х кубов
    #желтая
    material = makeMaterial('Yellow', (1,1,0), (1,1,1), 1)
    name_list = create_cube_line(3,x,y,z,material)
    #добавляем куб слева
    cube = create_simple_cube((x,y+2,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    
    #снимаем отметку со всех элементов
    bpy.ops.object.select_all(action='TOGGLE')
    #выделяем нужные кубы по имени
    select_by_names(name_list)
    bpy.ops.object.join()
    
def create_g_l(x=0,y=0,z=0):
    #фиолетовая
    material = makeMaterial('Violet', (1,0,1), (1,1,1), 1)
    #сначала создаем палку из 3-х кубов
    name_list = create_cube_line(3,x,y,z,material)
    #добавляем куб слева
    cube = create_simple_cube((x,y-2,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    
    #снимаем отметку со всех элементов
    bpy.ops.object.select_all(action='TOGGLE')
    #выделяем нужные кубы по имени
    select_by_names(name_list)
    bpy.ops.object.join()
    
#создаем штуку с кубиком по середине (крест)
def create_cross(x=0,y=0,z=0):
    material = makeMaterial('Green', (0,1,0), (1,1,1), 1)
    #сначала создаем палку из 3-х кубов
    name_list = create_cube_line(3,x,y,z,material)
    #добавляем куб по середине
    cube = create_simple_cube((x+2,y-2,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    
    #снимаем отметку со всех элементов
    bpy.ops.object.select_all(action='TOGGLE')
    #выделяем нужные кубы по имени
    select_by_names(name_list)
    bpy.ops.object.join()
    
#создаем кубик
def create_cube4(x=0,y=0,z=0):
    name_list = []
    #фиолетовая
    material = makeMaterial('Blue', (0,0,1), (1,1,1), 1)
    cube = create_simple_cube((x,y,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    cube = create_simple_cube((x+2,y,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    cube = create_simple_cube((x,y+2,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    cube = create_simple_cube((x+2,y+2,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    #снимаем отметку со всех элементов
    bpy.ops.object.select_all(action='TOGGLE')
    #выделяем нужные кубы по имени
    select_by_names(name_list)
    bpy.ops.object.join()
    
#создаем буквы z
def create_z1(x=0,y=0,z=0):
    name_list = []
    #светло голубая
    material = makeMaterial('ligth blue', (0,1,1), (1,1,1), 1)
    cube = create_simple_cube((x,y,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    cube = create_simple_cube((x+2,y,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    cube = create_simple_cube((x+2,y+2,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    cube = create_simple_cube((x+4,y+2,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
     #снимаем отметку со всех элементов
    bpy.ops.object.select_all(action='TOGGLE')
    #выделяем нужные кубы по имени
    select_by_names(name_list)
    bpy.ops.object.join()
    
def create_z2(x=0,y=0,z=0):
    #светло голубая
    name_list = []
    material = makeMaterial('ligth blue2', (0,0.5,1), (1,1,1), 1)
    cube = create_simple_cube((x+2,y,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    cube = create_simple_cube((x+4,y,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    cube = create_simple_cube((x+2,y+2,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
    cube = create_simple_cube((x,y+2,z))
    name_list.append(cube.name)
    setMaterial(cube,material)
     #снимаем отметку со всех элементов
    bpy.ops.object.select_all(action='TOGGLE')
    #выделяем нужные кубы по имени
    select_by_names(name_list)
    bpy.ops.object.join()
        
if __name__ == '__main__':
    #удаляем все объекты
    delete_all()
    #создаем линию
    create_line()
    #создаем букву г
    create_g_r(z=3)
    #создаем другую букву г
    create_g_l(z=6)
    #зодаем крест
    create_cross(z=-3)
    #создаем кубик
    create_cube4(z=-6)
    #создаем букву z1
    create_z1(z=9)
    create_z2(z=12)