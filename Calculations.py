""" define a system of earth and sun """

import math
from ReadData import *

# want acceleration to be negative initially so must take distances such that


def distance(body_one):
    distances = []
    # create an array of all the distances between bodies in system
    for i in range(dimension):
        # print(i)
        if body_one != object_Positions[i]:

            distances += [[object_Positions[i][0] - body_one[0],
                           object_Positions[i][1] - body_one[1], object_Positions[i][2] - body_one[2]]]

    return distances


# print(distance(object_Positions[0]))


def magnitude(body_one):
    temp = []
    magnitude = []
    # create an array of the distances between each other planet and the one you want
    # for i in range(len(objects)-1):

    temp += distance(body_one)

    for _ in range(int(len(temp))):  # fixed to the number of pairs of distances

        # had to use this as it cannot iterate over the list###
        magnitude += [math.sqrt(temp[_][0]**2 + temp[_][1]**2 + temp[_][2]**2)]

    return magnitude


# print(magnitude(object_Positions[0]))


def other_Masses(body_one, objects):
    masses = []
    for i in range(len(objects)):

        if i != objects.index(body_one):

            masses.append(object_Masses[i])

    return masses


# print(other_Masses(object_Positions[1], object_Positions))

# print(len(distance(object_Positions[1], object_Positions)))


def dist_by_mag(body_one, objects):
    fraction = []
    x_fraction = 0
    y_fraction = 0
    z_fraction = 0
    for i in range(dimension-1):
        x_fraction += other_Masses(body_one, objects)[i]*distance(body_one)[
            i][0] / (magnitude(body_one)[i]**3)
        y_fraction += other_Masses(body_one, objects)[i]*distance(body_one)[
            i][1] / (magnitude(body_one)[i]**3)
        z_fraction += other_Masses(body_one, objects)[i]*distance(body_one)[
            i][2] / (magnitude(body_one)[i]**3)
        # print(x_fraction, y_fraction)
    fraction = [x_fraction, y_fraction, z_fraction]
    return fraction


#print(dist_by_mag(object_Positions[1], object_Positions))

# using the predefined calculation we dont need to worry about zero denominators


def acceleration(body_one, objects):
    acceleration = []
    # acceleration = G*Mass of distant object* distance between objects / magnitude of distance between objects^3
    temp = dist_by_mag(body_one, objects)
    acceleration = [G*temp[0], G*temp[1], G*temp[2]]

    return acceleration


#print(acceleration(object_Positions[1], object_Positions))


def iterate(item_one, item_two):
    iterated_variable = []
    for i in range(dimension):
        iterated_variable_x = item_one[0] + item_two[0]*dt
        iterated_variable_y = item_one[1] + item_two[1]*dt
        iterated_variable_z = item_one[2] + item_two[2]*dt
    iterated_variable = [iterated_variable_x,
                         iterated_variable_y, iterated_variable_z]

    return iterated_variable


"""
We want to create all the calculating functions such that they can be put into a class and called into use when needed
This will be done most efficiently by embedding them progressively within earlier functions

"""
