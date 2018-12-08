import math
import time
from Calculations import *
from ReadData import *
from Approximations import *

#import matplotlib

# 1 T =  31557600s
# 1 au = 149597870.7 km
# Msun = 1.9891 x10^30 kg


def getData(choice):

    with open("sunPositions"+str(choice)+".txt", "w") as File:
        # then labels the document "File"
        for n in range(0, len(s_list)):
            # Every value must be written in
            File.write(str(s_list[n][0]))  # The time value is added first
            # A white space is added so that data is split into two columns
            File.write("\t")
            # The position value is added next
            File.write(str(s_list[n][1]))
            # a new line is added so this may repeat for all programs
            File.write("\t")
            # The position value is added next
            File.write(str(s_list[n][2]))
            File.write("\n")
    # This creates and opens a new text document
    with open("earthPositions"+str(choice)+".txt", "w") as File:
        # then labels the document "File"
        for n in range(0, len(e_list)):
            # Every value must be written in
            File.write(str(e_list[n][0]))  # The time value is added first
            # A white space is added so that data is split into two columns
            File.write("\t")
            # The position value is added next
            File.write(str(e_list[n][1]))
            File.write("\t")
            # The position value is added next
            File.write(str(e_list[n][2]))
            # a new line is added so this may repeat for all programs
            File.write("\n")

    # This creates and opens a new text document
    with open("jupiterPositions"+str(choice)+".txt", "w") as File:
        # then labels the document "File"
        for n in range(0, len(j_list)):
            # Every value must be written in
            File.write(str(j_list[n][0]))  # The x value is added first
            # A white space is added so that data is split into two columns
            File.write("\t")
            # The y value is added next
            File.write(str(j_list[n][1]))
            File.write("\t")
            # The y value is added next
            File.write(str(j_list[n][2]))
            # a new line is added so this may repeat for all programs
            File.write("\n")

    with open("saturnPositions"+str(choice)+".txt", "w") as File:
        # then labels the document "File"
        for n in range(0, len(sat_list)):
            # Every value must be written in
            File.write(str(sat_list[n][0]))  # The x value is added first
            # A white space is added so that data is split into two columns
            File.write("\t")
            # The y value is added next
            File.write(str(sat_list[n][1]))
            File.write("\t")
            # The y value is added next
            File.write(str(sat_list[n][2]))
            # a new line is added so this may repeat for all programs
            File.write("\n")

    with open("marsPositions"+str(choice)+".txt", "w") as File:
        # then labels the document "File"
        for n in range(0, len(mars_list)):
            # Every value must be written in
            File.write(str(mars_list[n][0]))  # The x value is added first
            # A white space is added so that data is split into two columns
            File.write("\t")
            # The y value is added next
            File.write(str(mars_list[n][1]))
            File.write("\t")
            # The y value is added next
            File.write(str(mars_list[n][2]))
            # a new line is added so this may repeat for all programs
            File.write("\n")

    with open("neptunePositions"+str(choice)+".txt", "w") as File:
        # then labels the document "File"
        for n in range(0, len(nep_list)):
            # Every value must be written in
            File.write(str(nep_list[n][0]))  # The time value is added first
            # A white space is added so that data is split into two columns
            File.write("\t")
            # The position value is added next
            File.write(str(nep_list[n][1]))
            # a new line is added so this may repeat for all programs
            File.write("\t")
            # The position value is added next
            File.write(str(nep_list[n][2]))
            File.write("\n")

    return "complete"


"""Set an input for either Euler, Euler-Cramer approximations etc"""
# --- Request user input on which approximation to use --- #

print("For a complicated system of bodies orbiting the sun we can approximate the orbit in multiple ways")
print("\t")
print("The options of Approximation are Euler and Euler-Cramer")
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
    input("Press any key to continue the program")

elif int(approximation) == 3:

    print("The program will now close")
    time.sleep(3)

else:
    print("This input is invalid, please restart the program to obtain a value")
    print("\t")
    approximation = input("Press any key to exit")
