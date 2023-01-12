import re 
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')



class Coordinat:
  def __init__(self, x, y):
    self.x = x
    self.y = y


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


def draw_graphic2(first_objects, second_objects):

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



    # Plot Line2 (Right Y Axis)
    # ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    # ax2.plot(pd_x, pd_y2, color='tab:blue')

    # ax3 = ax1.twinx()
    # ax3.plot(pd_x, pd_y3, color='tab:green') 
    # Decorations
    # ax1 (left Y axis)
    ax1.set_xlabel('Длина волны в нм', fontsize=20)
    ax1.tick_params(axis='x', rotation=0, labelsize=8)

    ax1.set_ylabel('Интенсивности от максимального отражения',  fontsize=20)
    ax1.tick_params(axis='y', rotation=0)
    ax1.grid(alpha=.8)

    plt.show()



paths1 = [
    'data_sorted/V+/28DAYS/dis/4_week_all_vplus_dis_Reflection__14__12-21-39-258.txt',
    'data_sorted/V+/28DAYS/dis/4_week_all_vplus_dis_Reflection__19__12-22-51-351.txt',
    'data_sorted/V+/28DAYS/dis/4_week_all_vplus_dis_Reflection__13__12-21-25-959.txt',
    'data_sorted/V+/28DAYS/dis/4_week_all_vplus_dis_Reflection__20__12-23-03-950.txt',
    'data_sorted/V+/28DAYS/dis/4_week_all_vplus_dis_Reflection__0__12-18-00-527.txt',
    'data_sorted/V+/28DAYS/dis/4_week_all_vplus_dis_Reflection__1__12-18-30-974.txt',
    'data_sorted/V+/28DAYS/dis/4_week_all_vplus_dis_Reflection__2__12-18-42-174.txt',
    'data_sorted/V+/28DAYS/dis/4_week_all_vplus_dis_Reflection__3__12-18-54-772.txt'
]

paths2 = [
    'data_sorted/V+/28DAYS/health/4_week_all_vplus_health_Reflection__0__13-51-34-374.txt',
    'data_sorted/V+/28DAYS/health/4_week_all_vplus_health_Reflection__1__13-53-46-159.txt',
    'data_sorted/V+/28DAYS/health/4_week_all_vplus_health_Reflection__2__13-54-01-837.txt',
    'data_sorted/V+/28DAYS/health/4_week_all_vplus_health_Reflection__3__13-54-19-116.txt',
    'data_sorted/V+/28DAYS/health/4_week_all_vplus_health_Reflection__4__13-54-34-474.txt',
    'data_sorted/V+/28DAYS/health/4_week_all_vplus_health_Reflection__5__13-55-27-909.txt',
    'data_sorted/V+/28DAYS/health/4_week_all_vplus_health_Reflection__6__13-55-42-948.txt',
    'data_sorted/V+/28DAYS/health/4_week_all_vplus_health_Reflection__7__14-00-32-522.txt',
]

dis = packaging_coord(paths1)
health = packaging_coord(paths2)

draw_graphic2(dis, health)

# draw_graphic(res.x, res.y, res2.y, res3.y)