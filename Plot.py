import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math

e_list = []
j_list = []
sun_list = []
sat_list = []
nep_list = []
mars_list = []


# "velocitydata.txt" may be replaced by any similarly formatted input document for a similar
earth_data = open("earthPositionsEuler-Cramer.txt", "r")

for line in earth_data.readlines():
    # add a new sublist
    e_list.append([])
    # loop over the elements and consider the white space between
    for i in line.split():
        # convert each variable to a float and then append to the list
        e_list[-1].append(float(i))
earth_data.close()

# "velocitydata.txt" may be replaced by any similarly formatted input document for a similar
jupiter_data = open("jupiterPositionsEuler-Cramer.txt", "r")

for line in jupiter_data.readlines():
    # add a new sublist
    j_list.append([])
    # loop over the elements and consider the white space between
    for i in line.split():
        # convert each variable to a float and then append to the list
        j_list[-1].append(float(i))
jupiter_data.close()

# "velocitydata.txt" may be replaced by any similarly formatted input document for a similar
saturn_data = open("saturnPositionsEuler-Cramer.txt", "r")

for line in saturn_data.readlines():
    # add a new sublist
    sat_list.append([])
    # loop over the elements and consider the white space between
    for i in line.split():
        # convert each variable to a float and then append to the list
        sat_list[-1].append(float(i))
saturn_data.close()

# "velocitydata.txt" may be replaced by any similarly formatted input document for a similar
sun_data = open("sunPositionsEuler-Cramer.txt", "r")

for line in sun_data.readlines():
    # add a new sublist
    sun_list.append([])
    # loop over the elements and consider the white space between
    for i in line.split():
        # convert each variable to a float and then append to the list
        sun_list[-1].append(float(i))
sun_data.close()

# "velocitydata.txt" may be replaced by any similarly formatted input document for a similar
nep_data = open("neptunePositionsEuler-Cramer.txt", "r")

for line in nep_data.readlines():
    # add a new sublist
    nep_list.append([])
    # loop over the elements and consider the white space between
    for i in line.split():
        # convert each variable to a float and then append to the list
        nep_list[-1].append(float(i))
nep_data.close()

mars_data = open("marsPositionsEuler-Cramer.txt", "r")
for line in mars_data.readlines():
    # add a new sublist
    mars_list.append([])
    # loop over the elements and consider the white space between
    for i in line.split():
        # convert each variable to a float and then append to the list
        mars_list[-1].append(float(i))
mars_data.close()

k = 3
for i in range(3*k+2):
    del e_list[k-1::k]
    del j_list[k-1::k]
    del sat_list[k-1::k]
    del sun_list[k-1::k]
    del nep_list[k-1::k]
    del mars_list[k-1::k]
    # repeat for every other list

fig = plt.figure(figsize=(100, 100))
ae = fig.gca(projection='3d')
aj = fig.gca(projection='3d')
asun = fig.gca(projection='3d')
asat = fig.gca(projection='3d')
anep = fig.gca(projection='3d')
amars = fig.gca(projection='3d')

x6 = []
y6 = []
z6 = []

for i in range(len(nep_list)):
    x6.append(mars_list[i][0])
    y6.append(mars_list[i][1])
    z6.append(mars_list[i][2])


x5 = []
y5 = []
z5 = []

for i in range(len(nep_list)):
    x5.append(nep_list[i][0])
    y5.append(nep_list[i][1])
    z5.append(nep_list[i][2])

x2 = []
y2 = []
z2 = []

for i in range(len(j_list)):
    x2.append(j_list[i][0])
    y2.append(j_list[i][1])
    z2.append(j_list[i][2])

x4 = []
y4 = []
z4 = []
for i in range(len(sat_list)):
    x4.append(sat_list[i][0])
    y4.append(sat_list[i][1])
    z4.append(sat_list[i][2])

x3 = []
y3 = []
z3 = []

for i in range(len(sun_list)):
    x3.append(sun_list[i][0])
    y3.append(sun_list[i][1])
    z3.append(sun_list[i][2])

x1 = []
y1 = []
z1 = []

for i in range(len(e_list)):
    x1.append(e_list[i][0])
    y1.append(e_list[i][1])
    z1.append(e_list[i][2])


mpl.rcParams['legend.fontsize'] = 10


asat.plot(x3, y3, z3, label='sun orbit')
asat.legend()
asat.set_ylim3d(-32, 32)
asat.set_xlim3d(-32, 32)
asat.set_zlim3d(-1, 1)

anep.plot(x6, y6, z6, label='mars orbit')
anep.legend()

anep.plot(x5, y5, z5, label='neptune orbit')
anep.legend()

asun.plot(x4, y4, z4, label='saturn orbit')
asun.legend()


aj.plot(x2, y2, z2, label='jupiter orbit')
aj.legend()


ae.plot(x1, y1, z1, label='earth orbit')
ae.legend()
plt.show()
