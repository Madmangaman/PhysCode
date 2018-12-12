import math
import time as t
from Calculations import *
from ReadData import *

Sun_list, Ven_list, Mer_list, Ear_list = [], [], [], []

Mar_list, Jup_list, Sat_list, Ura_list = [], [], [], []

Nep_list, Plu_list, ob1_list, ob2_list = [], [], [], []


def Euler():
    time = 0
    object_Acceleration = [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [], [], []]
    for _ in range(int(maxnstep/dt)):
        for i in range(number_of_bodies):
            object_Acceleration[i] = acceleration(
                object_Positions[i], object_Positions)
            
            object_Positions[i] = iterate(
                object_Positions[i], object_Velocities[i])

            object_Velocities[i] = iterate(
                object_Velocities[i], object_Acceleration[i])
            if i == 0:
                Sun_list.append(object_Positions[i])
            elif i == 1:
                Ven_list.append(object_Positions[i])
            elif i == 2:
                Mer_list.append(object_Positions[i])
            elif i == 3:
                Ear_list.append(object_Positions[i])
            elif i == 4:
                Mar_list.append(object_Positions[i])
            elif i == 5:
                Jup_list.append(object_Positions[i])
            elif i == 6:
                Sat_list.append(object_Positions[i])
            elif i == 7:
                Ura_list.append(object_Positions[i])
            elif i == 8:
                Nep_list.append(object_Positions[i])
            elif i == 9:
                Plu_list.append(object_Positions[i])
            elif i == 10:
                ob1_list.append(object_Positions[i])
            elif i == 11:
                ob2_list.append(object_Positions[i])

    return object_Positions

def Euler_Cramer():
    time = 0
    object_Acceleration = [[0.0, 0.0, 0.0], [
        0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0], [], []]
    for _ in range(int(maxnstep/dt)):
        for i in range(number_of_bodies):

            object_Acceleration[i] = acceleration(
                object_Positions[i], object_Positions)

            object_Velocities[i] = iterate(
                object_Velocities[i], object_Acceleration[i])

            object_Positions[i] = iterate(
                object_Positions[i], object_Velocities[i])
            if i == 0:
                Sun_list.append(object_Positions[i])
            elif i == 1:
                Ven_list.append(object_Positions[i])
            elif i == 2:
                Mer_list.append(object_Positions[i])
            elif i == 3:
                Ear_list.append(object_Positions[i])
            elif i == 4:
                Mar_list.append(object_Positions[i])
            elif i == 5:
                Jup_list.append(object_Positions[i])
            elif i == 6:
                Sat_list.append(object_Positions[i])
            elif i == 7:
                Ura_list.append(object_Positions[i])
            elif i == 8:
                Nep_list.append(object_Positions[i])
            elif i == 9:
                Plu_list.append(object_Positions[i])
            elif i == 10:
                ob1_list.append(object_Positions[i])
            elif i == 11:
                ob2_list.append(object_Positions[i])

    return object_Positions

# print(t.process_time())
