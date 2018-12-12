"""import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt"""
import math

Sun_list, Ven_list, Mer_list, Ear_list = [], [], [], []

Mar_list, Jup_list, Sat_list, Ura_list = [], [], [], []

Nep_list, Plu_list, Ob1_list, Ob2_list = [], [], [], []

full_list = []


def generate_data(choice, planetcheck):
    number_of_bodies = 0
    if 'Sun' in planetcheck:
        number_of_bodies += 1
        sun_data = open("SunPositions" + str(choice)+".txt", "r")
        for line in sun_data.readlines():
            # add a new sublist
            Sun_list.append([])
        # loop over the elements and consider the white space between
            for i in line.split():
                # convert each variable to a float and then append to the list
                Sun_list[-1].append(float(i))
        # print(Sun_list)
        full_list.append(Sun_list)
        sun_data.close()

    if 'Mercury' in planetcheck:
        number_of_bodies += 1
        mer_data = open("MercuryPositions" + str(choice)+".txt", "r")
        for line in mer_data.readlines():
            Mer_list.append([])
            for i in line.split():
                Mer_list[-1].append(float(i))
        # print(Mer_list)
        full_list.append(Mer_list)
        mer_data.close()

    if 'Venus' in planetcheck:
        number_of_bodies += 1
        ven_data = open("VenusPositions" + str(choice)+".txt", "r")
        for line in ven_data.readlines():
            Ven_list.append([])
            for i in line.split():
                Ven_list[-1].append(float(i))
        full_list.append(Ven_list)
        ven_data.close()

    if 'Earth' in planetcheck:
        number_of_bodies += 1
        ear_data = open("EarthPositions" + str(choice)+".txt", "r")
        for line in ear_data.readlines():
            Ear_list.append([])
            for i in line.split():
                Ear_list[-1].append(float(i))
        full_list.append(Ear_list)
        ear_data.close()

    if 'Mars' in planetcheck:
        number_of_bodies += 1
        mar_data = open("MarsPositions" + str(choice)+".txt", "r")
        for line in mar_data.readlines():
            Mar_list.append([])
            for i in line.split():
                Mar_list[-1].append(float(i))
        full_list.append(Mar_list)
        mar_data.close()

    if 'Jupiter' in planetcheck:
        number_of_bodies += 1
        jup_data = open("JupiterPositions" + str(choice)+".txt", "r")
        for line in jup_data.readlines():
            Jup_list.append([])
            for i in line.split():
                Jup_list[-1].append(float(i))
        full_list.append(Jup_list)
        jup_data.close()

    if 'Saturn' in planetcheck:
        number_of_bodies += 1
        sat_data = open("SaturnPositions" + str(choice)+".txt", "r")
        for line in sat_data.readlines():
            Sat_list.append([])
            for i in line.split():
                Sat_list[-1].append(float(i))
        full_list.append(Sat_list)
        sat_data.close()

    if 'Uranus' in planetcheck:
        number_of_bodies += 1
        ura_data = open("UranusPositions" + str(choice)+".txt", "r")
        for line in ura_data.readlines():
            Ura_list.append([])
            for i in line.split():
                Ura_list[-1].append(float(i))
        full_list.append(Ura_list)
        ura_data.close()

    if 'Neptune' in planetcheck:
        number_of_bodies += 1
        nep_data = open("NeptunePositions" + str(choice)+".txt", "r")
        for line in nep_data.readlines():
            Nep_list.append([])
            for i in line.split():
                Nep_list[-1].append(float(i))
        full_list.append(Nep_list)
        nep_data.close()

    if 'Pluto' in planetcheck:
        number_of_bodies += 1
        plu_data = open("PlutoPositions" + str(choice)+".txt", "r")
        for line in plu_data.readlines():
            Plu_list.append([])
            for i in line.split():
                Plu_list[-1].append(float(i))
        full_list.append(Plu_list)
        plu_data.close()

    if 'Object1' in planetcheck:
        number_of_bodies += 1
        ob1_data = open("Object1Positions" + str(choice)+".txt", "r")
        for line in ob1_data.readlines():
            Ob1_list.append([])
            for i in line.split():
                Ob1_list[-1].append(float(i))
        full_list.append(Ob2_list)
        ob1_data.close()

    if 'Object2' in planetcheck:
        number_of_bodies += 1
        ob2_data = open("Object2Positions" + str(choice)+".txt", "r")
        for line in ob2_data.readlines():
            Ob2_list.append([])
            for i in line.split():
                Ob2_list[-1].append(float(i))
        full_list.append(Ob2_list)
        ob2_data.close()

    return "generating data plot now"
