import math
import time as t
from Calculations import *
from ReadData import *

s_list = []
e_list = []
j_list = []
sat_list = []
mars_list = []
nep_list = []


def Euler():
    time = 0
    object_Acceleration = [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [], [], []]
    for _ in range(int(maxnstep/dt)):
        for i in range(6):
            object_Acceleration[i] = acceleration(
                object_Positions[i], object_Positions)
            # print(object_Acceleration[i])
            object_Positions[i] = iterate(
                object_Positions[i], object_Velocities[i])

            object_Velocities[i] = iterate(
                object_Velocities[i], object_Acceleration[i])
            if i == 0:
                # s_list.append(time)
                s_list.append(object_Positions[i])
            elif i == 1:
                # e_list.append(time)
                e_list.append(object_Positions[i])
            elif i == 2:
                # j_list.append(time)
                j_list.append(object_Positions[i])
            elif i == 3:
                sat_list.append(object_Positions[i])
            elif i == 4:
                mars_list.append(object_Positions[i])
            else:
                nep_list.append(object_Positions[i])
        time += dt
    return object_Positions
    # return object_Acceleration, object_Positions, object_Velocities
    # e_list.append([object_Positions[1], object_Velocities[1])


def Euler_Cramer():
    time = 0
    object_Acceleration = [[0.0, 0.0, 0.0], [
        0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0], [], []]
    for _ in range(int(maxnstep/dt)):
        for i in range(6):

            object_Acceleration[i] = acceleration(
                object_Positions[i], object_Positions)

            object_Velocities[i] = iterate(
                object_Velocities[i], object_Acceleration[i])

            object_Positions[i] = iterate(
                object_Positions[i], object_Velocities[i])
            if i == 0:
                # s_list.append(time)
                s_list.append(object_Positions[i])
            elif i == 1:
                # e_list.append(time)
                e_list.append(object_Positions[i])
            elif i == 2:
                # j_list.append(time)
                j_list.append(object_Positions[i])
            elif i == 3:
                sat_list.append(object_Positions[i])
            elif i == 4:
                mars_list.append(object_Positions[i])
            else:
                nep_list.append(object_Positions[i])
        time += dt
    return object_Positions
# return object_Acceleration, object_Positions, object_Velocities


# print(Euler_Cramer())
# print(t.process_time())
