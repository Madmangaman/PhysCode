import math
G = 4*math.pi**2
print("Please enter a timestep as a decimal of a year e.g. 0.01, \
to choose the accuracy of the approximation")
print("\t")
print("Recommended time steps between 0.1 and 0.0001 any smaller will \
run for a very long time")
print("\t")
dt = float(input())
print("\t")
print("How many years would you like the simulation to run for\
(recommend under 20 with lots of bodies)?")
maxnstep = float(input())
""" read positions and velocities into this file (masses will be generated in the calculations file)"""

planets = open("Planetdata.txt", "r")

temporary_data = []
object_Positions = []
object_Velocities = []
object_Masses = []

for line in planets.readlines():
    temporary_data.append([])
    for i in line.split():
        temporary_data[-1].append(float(i))


for j in range(len(temporary_data)):
    for k in range(4):
        if k == 1:
            object_Positions.append(
                [temporary_data[j][0], temporary_data[j][1], temporary_data[j][2]])
        elif k == 2:
            object_Velocities.append(
                [temporary_data[j][3]*365, temporary_data[j][4]*365, temporary_data[j][5]*365])
        elif k == 3:
            object_Masses.append(temporary_data[j][6]/(2*math.pow(10, 6)))

"""print(object_Masses)
print(object_Positions)
print(object_Velocities)"""
dimension = len(object_Masses)
number_of_bodies = len(object_Masses)
