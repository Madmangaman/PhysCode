import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import math
import time
from get_plotData import *


print("Choose whether you want a 2D or a 3D plot, enter 1 for 2D and 2 for 3D")
print("\t")
dimensions = int(input())
print("\t")
print("Which model would you like to use, Enter 1 for Euler and 2 for Euler-Cramer")
print("\t")
approximation = input()
print("\t")
print("Which Planets would you like to plot?  ")
print("\t")
print("Please refer to the names given on the text files e.g. for EarthPositionsEuler, \
type Earth (case sensistve)")
print("\t")
how_many = input()


translation_table = dict.fromkeys(
    map(ord, '¬^£%!@#$qwertyuiopasdfghjklzxcvbnm,.\/|#@[]{}+=-_)(*&'), None)
approximation = approximation.translate(translation_table)

choice = "blank"

if int(approximation) == 1:

    choice = "Euler"
    print("The Euler approximation data is being imported into the program")
    print("\t")
    generate_data(choice, how_many)
    print("\t")
    input("Press any key to continue the program")
    print("\t")

elif int(approximation) == 2:

    choice = "Euler-Cramer"
    print("The Euler-Cramer approximation data is being imported")
    print("\t")
    generate_data(choice, how_many)
    print("\t")
    input("Press any key to continue the program")
    print("\t")

elif int(approximation) == 3:

    print("\t")
    print("The program will now close")
    time.sleep(3)
else:
    print("\t")
    print("This input is invalid, please restart the program to obtain a value")
    print("\t")
    approximation = input("Press any key to exit")


"""
The for loop below takes the points given in each function and reduces this number roughly 100 times
This is to reduce the strain on the computer when rendering all the planets/bodies
This reduces the accuracy but the individual points themselves remain correct
"""
k = 3
for i in range(3*k+3):
    del Sun_list[k-1::k]
    del Mer_list[k-1::k]
    del Ven_list[k-1::k]
    del Ear_list[k-1::k]
    del Mar_list[k-1::k]
    del Jup_list[k-1::k]
    del Sat_list[k-1::k]
    del Ura_list[k-1::k]
    del Nep_list[k-1::k]
    del Plu_list[k-1::k]
    del Ob1_list[k-1::k]
    del Ob2_list[k-1::k]

# Now I create two distinct plots of all the data chosen
# print(dimensions)
if dimensions == 1:
    plt.figure(figsize=(100, 100))
    """asun, amer, aven = fig.gca(projection='2d'), fig.gca(
        projection='2d'), fig.gca(projection='2d')
    aear, amar, ajup = fig.gca(projection='2d'), fig.gca(
        projection='2d'), fig.gca(projection='2d')
    asat, aura, anep = fig.gca(projection='2d'), fig.gca(
        projection='2d'), fig.gca(projection='2d')
    aplu, aob1, aob2 = fig.gca(projection='2d'), fig.gca(
        projection='2d'), fig.gca(projection='2d')"""
    x1, y1, x2, y2 = [], [], [], []
    x3, y3, x4, y4 = [], [], [], []
    x5, y5, x6, y6 = [], [], [], []
    x7, y7, x8, y8 = [], [], [], []
    x9, y9, x10, y10 = [], [], [], []
    x11, y11, x12, y12 = [], [], [], []
    # print(full_list[0])
    """for i in range(len(full_list)):"""
    # print(len(full_list))
    # print(full_list[0][1])
    for _ in range(len(full_list)):
        print(_)
        x1.append(full_list[0][_][0])
        y1.append(full_list[0][_][1])
        if len(full_list) == 2:
            x2.append(full_list[1][_][0])
            y2.append(full_list[1][_][1])
        if len(full_list) == 3:
            x3.append(full_list[2][_][0])
            y3.append(full_list[2][_][1])
        if len(full_list) == 4:
            x4.append(full_list[3][_][0])
            y4.append(full_list[3][_][1])
        if len(full_list) == 5:
            x5.append(full_list[4][_][0])
            y5.append(full_list[4][_][1])
        if len(full_list) == 6:
            x6.append(full_list[5][_][0])
            y6.append(full_list[5][_][1])
        if len(full_list) == 7:
            x7.append(full_list[6][_][0])
            y7.append(full_list[6][_][1])
        if len(full_list) == 8:
            x8.append(full_list[7][_][0])
            y8.append(full_list[7][_][1])
        if len(full_list[0]) == 9:
            x9.append(full_list[8][_][0])
            y9.append(full_list[8][_][1])
        if len(full_list[0]) == 10:
            x10.append(full_list[9][_][0])
            y10.append(full_list[9][_][1])
        if len(full_list[0]) == 11:
            x11.append(full_list[9][_][0])
            y11.append(full_list[1][_][1])
        if len(full_list[0]) == 12:
            x12.append(full_list[11][_][0])
            y12.append(full_list[11][_][1])
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.plot(x3, y3)
    plt.plot(x4, y4)
    plt.plot(x5, y5)
    plt.plot(x6, y6)
    plt.plot(x7, y7)
    plt.plot(x8, y8)
    plt.plot(x9, y9)
    plt.plot(x10, y10)
    plt.plot(x11, y11)
    plt.plot(x12, y12)
    plt.title('2-Dimensional orbits')
    plt.show()

elif dimensions == 2:

    fig = plt.figure(figsize=(100, 100))
    asun, amer, aven = fig.gca(projection='3d'), fig.gca(
        projection='3d'), fig.gca(projection='3d')
    aear, amar, ajup = fig.gca(projection='3d'), fig.gca(
        projection='3d'), fig.gca(projection='3d')
    asat, aura, anep = fig.gca(projection='3d'), fig.gca(
        projection='3d'), fig.gca(projection='3d')
    aplu, aob1, aob2 = fig.gca(projection='3d'), fig.gca(
        projection='3d'), fig.gca(projection='3d')
# create a list for of all the data points
    x1, y1, z1, x2, y2, z2 = [], [], [], [], [], []
    x3, y3, z3, x4, y4, z4 = [], [], [], [], [], []
    x5, y5, z5, x6, y6, z6 = [], [], [], [], [], []
    x7, y7, z7, x8, y8, z8 = [], [], [], [], [], []
    x9, y9, z9, x10, y10, z10 = [], [], [], [], [], []
    x11, y11, z11, x12, y12, z12 = [], [], [], [], [], []
    """for i in range(len(full_list)):"""
    # print(len(full_list[0]))
    # print(len(full_list[0][1]))
    for _ in range(len(full_list[0])):
        print(_)
        x1.append(full_list[0][_][0])
        y1.append(full_list[0][_][1])
        z1.append(full_list[0][_][2])
        if len(full_list[0]) == 2:
            x2.append(full_list[1][_][0])
            y2.append(full_list[1][_][1])
            z2.append(full_list[1][_][2])
        if len(full_list[0]) == 3:
            x3.append(full_list[2][_][0])
            y3.append(full_list[2][_][1])
            z3.append(full_list[2][_][2])
        if len(full_list[0]) == 4:
            x4.append(full_list[3][_][0])
            y4.append(full_list[3][_][1])
            z4.append(full_list[3][_][2])
        if len(full_list[0]) == 5:
            x5.append(full_list[4][_][0])
            y5.append(full_list[4][_][1])
            z5.append(full_list[4][_][2])
        if len(full_list[0]) == 6:
            x6.append(full_list[5][_][0])
            y6.append(full_list[5][_][1])
            z6.append(full_list[5][_][2])
        if len(full_list[0]) == 7:
            x7.append(full_list[6][_][0])
            y7.append(full_list[6][_][1])
            z7.append(full_list[6][_][2])
        if len(full_list[0]) == 8:
            x8.append(full_list[7][_][0])
            y8.append(full_list[7][_][1])
            z8.append(full_list[7][_][2])
        if len(full_list[0]) == 9:
            x9.append(full_list[8][_][0])
            y9.append(full_list[8][_][1])
            z9.append(full_list[8][_][2])
        if len(full_list[0]) == 10:
            x10.append(full_list[9][_][0])
            y10.append(full_list[9][_][1])
            z10.append(full_list[9][_][2])
        if len(full_list[0]) == 11:
            x11.append(full_list[9][_][0])
            y11.append(full_list[1][_][1])
            z11.append(full_list[10][_][2])
        if len(full_list[0]) == 11:
            x12.append(full_list[11][_][0])
            y12.append(full_list[11][_][1])
            z12.append(full_list[11][_][2])

    mpl.rcParams['legend.fontsize'] = 10

    asun.plot(x1, y1, z1, label='Sun orbit')
    aven.plot(x2, y2, z2, label='Mercury orbit')
    amer.plot(x3, y3, z3, label='Venus orbit')
    aear.plot(x4, y4, z4, label='Earth orbit')
    amar.plot(x5, y5, z5, label='Mars orbit')
    ajup.plot(x6, y6, z6, label='Jupiter orbit')
    asat.plot(x7, y7, z7, label='Saturn orbit')
    aura.plot(x8, y8, z8, label='Uranus orbit')
    anep.plot(x9, y9, z9, label='Neptune orbit')
    aplu.plot(x10, y10, z10, label='Pluto orbit')
    aob1.plot(x11, y11, z11, label='Object1 orbit')
    aob2.plot(x12, y12, z12, label='Object2 orbit')

    asun.legend()
    aven.legend()
    amer.legend()
    aear.legend()
    amar.legend()
    ajup.legend()
    asat.legend()
    aura.legend()
    anep.legend()
    aplu.legend()
    aob1.legend()
    aob2.legend()
    plt.show()

else:
    print("Invalid input, please restart the program to continue")


print(input("Press any key to exit after viewing the data"))
