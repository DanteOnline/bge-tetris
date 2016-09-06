#import bpy
from core import delete_all
from materials import makeMaterial, setMaterial
from meshes import create_simple_cube

#Создание 3-х кубов подряд
#count - количество кубов
def create_cube_line(count, x=0,y=0,z=0,material=None):
    #шаг
    step = 2
    #делаем 4 куба
    for i in range(count):
        create_simple_cube((x+step*i,y,z),material)

#Создаем палку из 4-х кубиков
def create_line(x=0,y=0,z=0):
    #палка будет красной
    red = makeMaterial('Red', (1,0,0), (1,1,1), 1)
    create_cube_line(4,x,y,z,red)
        
#создаем букву г
def create_g_r(x=0,y=0,z=0):
    #сначала создаем палку из 3-х кубов
    #желтая
    material = makeMaterial('Yellow', (1,1,0), (1,1,1), 1)
    create_cube_line(3,x,y,z,material)
    #добавляем куб слева
    create_simple_cube((x,y+2,z),material)
    
def create_g_l(x=0,y=0,z=0):
    #фиолетовая
    material = makeMaterial('Violet', (1,0,1), (1,1,1), 1)
    #сначала создаем палку из 3-х кубов
    create_cube_line(3,x,y,z,material)
    #добавляем куб слева
    create_simple_cube((x,y-2,z),material)
    
#создаем штуку с кубиком по середине (крест)
def create_cross(x=0,y=0,z=0):
    material = makeMaterial('Green', (0,1,0), (1,1,1), 1)
    #сначала создаем палку из 3-х кубов
    create_cube_line(3,x,y,z,material)
    #добавляем куб по середине
    create_simple_cube((x+2,y-2,z),material)
    
#создаем кубик
def create_cube4(x=0,y=0,z=0):
    #фиолетовая
    material = makeMaterial('Blue', (0,0,1), (1,1,1), 1)
    create_simple_cube((x,y,z),material)
    create_simple_cube((x+2,y,z),material)
    create_simple_cube((x,y+2,z),material)
    create_simple_cube((x+2,y+2,z),material)
    
#создаем буквы z
def create_z1(x=0,y=0,z=0):
    #светло голубая
    material = makeMaterial('ligth blue', (0,1,1), (1,1,1), 1)
    create_simple_cube((x,y,z),material)
    create_simple_cube((x+2,y,z),material)
    create_simple_cube((x+2,y+2,z),material)
    create_simple_cube((x+4,y+2,z),material)
    
def create_z2(x=0,y=0,z=0):
    #светло голубая
    material = makeMaterial('ligth blue2', (0,0.5,1), (1,1,1), 1)
    create_simple_cube((x+2,y,z),material)
    create_simple_cube((x+4,y,z),material)
    create_simple_cube((x+2,y+2,z),material)
    create_simple_cube((x,y+2,z),material)
        
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