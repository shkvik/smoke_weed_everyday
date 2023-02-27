from functions import *


print("Введите путь папки 1 категории [красный цвет]", end=": ")
obj1 = input()

print(obj1)

print("Введите путь папки 2 категории [зеленый цвет]", end=": ")
obj2 = input()

print("У вас есть ещё объекты?", end=": ")
request = input()

class Pack:
    def __init__(self, dir, color):
        self.dir = dir
        self.color = color

obj3_count = None
if(request == "Да" or request == "да"):
    obj3_paths = []
    print("Введите количество", end=": ")
    obj3_count = input()
    for i in range(0, int(obj3_count)):
        print("Введите директорию для категории " + str(i), end=": ")
        dir = input()

        print("Введите цвет графика объекта в HEX (образец: #FFFF99) " + str(i), end=": ")
        color = input()

        obj3_paths.append(Pack(dir, color))

pack1 = packaging_coord(GetDirsNames(obj1))
pack2 = packaging_coord(GetDirsNames(obj2))

obj3_pack = None
if(obj3_count != None):
    obj3_pack = []
    for i in range(0, int(obj3_count)): 
        obj3_pack.append(ObjectsPack(packaging_coord(GetDirsNames(obj3_paths[i].dir)), color))


draw_graphic2(pack1, pack2, obj3_pack)