import bpy

#удалить все объекты
def delete_all():
    #на всякий случай делаем 2 раза чтобы точно удалить :)
    for i in range(2):
        bpy.ops.object.select_all(action='TOGGLE')
        bpy.ops.object.delete(use_global=False)