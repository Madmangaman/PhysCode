import math
import time
from ReadData import *
from Calculations import *
from Approximations import *

#import matplotlib

# 1 T =  31557600s
# 1 au = 149597870.7 km
# Msun = 1.9891 x10^30 kg


def getData(choice):
    # This creates and opens a new text document for each planet/body
    with open("SunPositions"+str(choice)+".txt", "w") as File:
        # then labels the document "File"
        for n in range(0, len(Sun_list)):
            # Every value must be written in
            File.write(str(Sun_list[n][0]))  # The x value is added first
            # A white space is added so that data is split into two columns
            File.write("\t")
            # The y value is added next
            File.write(str(Sun_list[n][1]))
            # a new line is added so this may repeat for all programs
            File.write("\t")
            # The z value is added next
            File.write(str(Sun_list[n][2]))
            File.write("\n")

    with open("MercuryPositions"+str(choice)+".txt", "w") as File:
        for n in range(0, len(Mer_list)):
            File.write(str(Mer_list[n][0]))
            File.write("\t")
            File.write(str(Mer_list[n][1]))
            File.write("\t")
            File.write(str(Mer_list[n][2]))
            File.write("\n")

    with open("VenusPositions"+str(choice)+".txt", "w") as File:
        for n in range(0, len(Ven_list)):
            File.write(str(Ven_list[n][0]))
            File.write("\t")
            File.write(str(Ven_list[n][1]))
            File.write("\t")
            File.write(str(Ven_list[n][2]))
            File.write("\n")

    with open("EarthPositions"+str(choice)+".txt", "w") as File:
        for n in range(0, len(Ear_list)):
            File.write(str(Ear_list[n][0]))
            File.write("\t")
            File.write(str(Ear_list[n][1]))
            File.write("\t")
            File.write(str(Ear_list[n][2]))
            File.write("\n")

    with open("MarsPositions"+str(choice)+".txt", "w") as File:
        for n in range(0, len(Mar_list)):
            File.write(str(Mar_list[n][0]))
            File.write("\t")
            File.write(str(Mar_list[n][1]))
            File.write("\t")
            File.write(str(Mar_list[n][2]))
            File.write("\n")

    with open("JupiterPositions"+str(choice)+".txt", "w") as File:
        for n in range(0, len(Jup_list)):
            File.write(str(Jup_list[n][0]))
            File.write("\t")
            File.write(str(Jup_list[n][1]))
            File.write("\t")
            File.write(str(Jup_list[n][2]))
            File.write("\n")
            
    with open("SaturnPositions"+str(choice)+".txt", "w") as File:
        for n in range(0, len(Sat_list)):
            File.write(str(Sat_list[n][0]))
            File.write("\t")
            File.write(str(Sat_list[n][1]))
            File.write("\t")
            File.write(str(Sat_list[n][2]))
            File.write("\n")
            
    with open("UranusPositions"+str(choice)+".txt", "w") as File:
        for n in range(0, len(Ura_list)):
            File.write(str(Ura_list[n][0]))
            File.write("\t")
            File.write(str(Ura_list[n][1]))
            File.write("\t")
            File.write(str(Ura_list[n][2]))
            File.write("\n")

    with open("NeptunePositions"+str(choice)+".txt", "w") as File:
        for n in range(0, len(Nep_list)):

            File.write(str(Nep_list[n][0]))
            File.write("\t")
            File.write(str(Nep_list[n][1]))
            File.write("\t")
            File.write(str(Nep_list[n][2]))
            File.write("\n")

    with open("PlutoPositions"+str(choice)+".txt", "w") as File:
        for n in range(0, len(Plu_list)):
            File.write(str(Plu_list[n][0]))
            File.write("\t")
            File.write(str(Plu_list[n][1]))
            File.write("\t")
            File.write(str(Plu_list[n][2]))
            File.write("\n")

    with open("Object1Positions"+str(choice)+".txt", "w") as File:
        for n in range(0, len(ob1_list)):
            File.write(str(ob1_list[n][0]))
            File.write("\t")
            File.write(str(ob1_list[n][1]))
            File.write("\t")
            File.write(str(ob1_list[n][2]))
            File.write("\n")

    with open("Object2Positions"+str(choice)+".txt", "w") as File:
        for n in range(0, len(ob2_list)):
            File.write(str(ob2_list[n][0]))
            File.write("\t")
            File.write(str(ob2_list[n][1]))
            File.write("\t")
            File.write(str(ob2_list[n][2]))
            File.write("\n")
    return "complete"


"""Set an input for either Euler, Euler-Cramer approximations etc"""
# --- Request user input on which approximation to use --- #

print("For a complicated system of bodies orbiting the sun we can approximate the orbit \
in multiple ways")
print("\t")
print("This Model works for the 8 planets in the solar system, Pluto and two other bodies ")
print("\t")
print("The available Approximations are Euler and Euler-Cramer")
print("\t")
approximation = input(
    "Enter 1 for Euler, enter 2 for Euler-Cramer or 3 to close the program:  ")
print("\t")


"""
Once the approximation has been selected we have to make sure the program is able to run based on the input given.
This is done using a simple if comparison against their approximation number choice.
It must be such that if they haven't chosen an appropriate value that the program doesnt fail.

This is solved below by removing all forbidden values (i.e. anything that isnt numeric)


"""

# --- If condition to create text documents corresponding to chosen approximation --- #

translation_table = dict.fromkeys(
    map(ord, '¬^£%!@#$qwertyuiopasdfghjklzxcvbnm,.\/|#@[]{}+=-_)(*&'), None)
approximation = approximation.translate(translation_table)

choice = "blank"

if int(approximation) == 1:

    choice = "Euler"
    print("The Euler approximation will now run")
    print("\t")
    print(Euler())
    print("\t")
    print("A text file has been generated with the output values")
    print("\t")
    getData(choice)
    print("\t")
    print("Run the Plot.py program to decide how you want to manipulate the data")
    print("\t")
    input("Press any key to continue the program")

elif int(approximation) == 2:

    choice = "Euler-Cramer"
    print("The Euler-Cramer approximation will now run")
    print("\t")
    print(Euler_Cramer())
    print("\t")
    print("A text file has been generated with the output values")
    print("\t")
    getData(choice)
    print("\t")
    print("Run the Plot.py program to decide how you want to manipulate the data")
    print("\t")
    input("Press any key to close the program")

elif int(approximation) == 3:

    print("The program will now close")
    time.sleep(3)
else:
    print("This input is invalid, please restart the program to obtain a value")
    print("\t")
    approximation = input("Press any key to exit")
