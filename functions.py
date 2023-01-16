import re 
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
from file_search import GetDirsNames


class Coordinat:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class ObjectsPack:
    def __init__(self, object, color):
        self.object = object
        self.color = color

def get_coordinats(source_path):
    with open(source_path, 'r') as file:
        data = file.read().rstrip()

    for m in re.finditer(r'>>>>>Begin Spectral Data<<<<<', data): 
        print('строка[', m[0], ']заканчивается с позиции', m.end())

    print(str(m.end()) + " " + str(len(data)))

    str_result = ""

    for index in range(m.end(), len(data)):
        str_result += data[index]

    print(str(str_result))

    result_x = []
    result_y = []

    reg_result = re.split(r'(\d{0,6}\.?\d{0,6})(\s{0,6})(\-?\d{0,6}\.?\d{0,6})', str_result)

    reg_result_updated = [value for value in reg_result if value != "\t" and value != "\n" and value != '']


    skip = False
    for i in range(0, len(reg_result_updated)):
        if(skip == False):
            value = float(reg_result_updated[i])
            if i % 2 == 0:
                if(value >= 400.0 and value <= 900.0):
                    result_x.append(value)
                else:
                    skip = True
            else:
                if(value > 120):
                    value = 120
                if(value < 0):
                    value = 0
                result_y.append(value)
        else:
            skip = False
            
    assert(len(result_x) == len(result_y))

    return Coordinat(result_x, result_y)


def packaging_coord(paths):
    pack = []
    for i in range(0, len(paths)):
        temp = get_coordinats(paths[i])
        pack.append(temp)
    return pack


def draw_graphic(result_x, result_y, res_y2, res_y3):
    pd_x = pd.array(result_x)
    pd_y = pd.array(result_y)

    pd_y2 = pd.array(res_y2)
    pd_y3 = pd.array(res_y3)

    # Plot Line1 (Left Y Axis)
    fig, ax1 = plt.subplots(1,1,figsize=(16,9), dpi= 100)
    ax1.plot(pd_x, pd_y, color='tab:red')

    # Plot Line2 (Right Y Axis)
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.plot(pd_x, pd_y2, color='tab:blue')

    ax3 = ax1.twinx()
    ax3.plot(pd_x, pd_y3, color='tab:green') 
    # Decorations
    # ax1 (left Y axis)
    ax1.set_xlabel('Длина волны в нм', fontsize=20)
    ax1.tick_params(axis='x', rotation=0, labelsize=8)

    ax1.set_ylabel('Интенсивности от максимального отражения',  fontsize=20)
    ax1.tick_params(axis='y', rotation=0)
    ax1.grid(alpha=.8)

    plt.show()


def draw_graphic2(first_objects, second_objects, pack_objects = None):

    pd_x = pd.array(first_objects[0].x)
    pd_y = pd.array(first_objects[0].y)

    pd_y_second = []

    for i in range(len(second_objects)):
        pd_y_second.append(pd.array(second_objects[i].y))

    # Plot Line1 (Left Y Axis)
    fig, ax1 = plt.subplots(1,1,figsize=(16,9), dpi= 100)
    ax1.plot(pd_x, pd_y, color='tab:red')

    collect1 = []
    collect2 = []

    for i, j in zip(range(1, len(first_objects)), range(0, len(first_objects)-1)):
       collect1.append(0)
       collect1[j] = ax1.twinx()
       collect1[j].plot(pd_x, pd.array(first_objects[i].y), color='tab:red') 


    for i in range(0, len(second_objects)):
       collect2.append(0)
       collect2[i] = ax1.twinx()
       collect2[i].plot(pd_x, pd.array(second_objects[i].y), color='tab:green') 


    if(pack_objects != None):
        for j in range(0, len(pack_objects)):
            collect = []
            for i in range(0, len(pack_objects)):
                collect.append(0)
                collect[i] = ax1.twinx()
                collect[i].plot(pd_x, pd.array(pack_objects[j].object[i].y), color=pack_objects[j].color) 


    ax1.set_xlabel('Длина волны в нм', fontsize=20)
    ax1.tick_params(axis='x', rotation=0, labelsize=8)

    ax1.set_ylabel('Интенсивности от максимального отражения',  fontsize=20)
    ax1.tick_params(axis='y', rotation=0)
    ax1.grid(alpha=.8)

    plt.show()







# dis = packaging_coord(GetDirsNames("data_sorted/V+/28DAYS/dis/"))
# health = packaging_coord(GetDirsNames("data_sorted/V+/28DAYS/health/"))


# tree = []
# tree.append(ObjectsPack(packaging_coord(GetDirsNames("data_sorted/Mothers/_date/V_plus/healthy/")), 'tab:green'))
# tree.append(ObjectsPack(packaging_coord(GetDirsNames("data_sorted/Mothers/_date/V_plus/stress/")), 'tab:blue'))

# draw_graphic2(dis, health, tree)
