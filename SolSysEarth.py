# Python Solar System Sim 2.0;
import math 
import cmath
import numpy as np
import time # used to adjust final output
import re # used to adjust user input
"""Import numpy to use vectors and create shorter code"""
# define key variables

""" Using standard units defined by
T = 31557600 # 1 year in seconds
au = 149597870.7 # 1 astronomical unit
Msun = 1.9891*math.pow(10, 30)
"""

# ------- Define all universal constants -------- #

Gval = 4*(math.pi)**2
Msun = 1
Mearth = 3.3*Msun*math.pow(10, -5)
dt = 0.001 # Set the time step each iteration undergoes
maxnsteps = 4

# --- Set the sun location to (0,0) --- #

sunPos = np.array([0,0])


# --- Give initial positions and velocities --- #
"""Consider making this user input later on"""
xval, yval = 1.0, 0.0
vxval, vyval = 0.0, 2*math.pi

dlist=[]


# --- define both Approximations --- #
"""Use vectors to define the orbit"""
def earthEuler():
    earthPos = np.array([xval, yval])
    time = 0
    accelerationVector = np.array([0.0,0.0])
    accelerationUnitVector = np.array([0.0,1.0])
    velocityVector = np.array([vxval, vyval])
    while time < maxnsteps:
        distance = math.sqrt(np.dot(sunPos-earthPos,sunPos-earthPos))
        #accelerationUnitVector = (sunPos-earthPos)/(np.dot(sunPos-earthPos,sunPos-earthPos))
        accelerationVector = np.array([-(Gval*Msun*earthPos[0])/(distance**3), -(Gval*Msun*earthPos[1])/(distance**3)])
        #print(sunPos-earthPos)
        #print(accelerationVector)
        #recreate the vector each time as this will make the step to multiple planets easier
        np.add(earthPos, velocityVector*dt, out=earthPos, casting='unsafe')
        np.add(velocityVector, accelerationVector*dt, out=velocityVector, casting='unsafe')
        #print(accelerationVector)
        #print(math.sqrt(np.dot(accelerationUnitVector, accelerationUnitVector)))
        dlist.append([time, earthPos[0], earthPos[1], velocityVector[0], velocityVector[1]])
        tval += dt
        
    return (sunPos-earthPos)
        #print(xval, yval)
        #E = 0.5*Mearth*(xval**2 + yval**2)
        #dlist.append([tval, xval, yval, vxval, vyval])
        #calculate the acceleration before any other value and in x-y parallel


def earthEulerCramer():
    earthPos = np.array([xval, yval])
    time = 0
    accelerationVector = np.array([0.0,0.0])
    accelerationUnitVector = np.array([0.0,1.0])
    velocityVector = np.array([vxval, vyval])
    while time < maxnsteps:
        distance = math.sqrt(np.dot(sunPos-earthPos,sunPos-earthPos))
        #accelerationUnitVector = (sunPos-earthPos)/(np.dot(sunPos-earthPos,sunPos-earthPos))
        accelerationVector = np.array([-(Gval*Msun*earthPos[0])/(distance**3), -(Gval*Msun*earthPos[1])/(distance**3)])
        #print(sunPos-earthPos)
        #print(accelerationVector)
        #recreate the vector each time as this will make the step to multiple planets easier
        np.add(velocityVector, accelerationVector*dt, out=velocityVector, casting='unsafe')
        np.add(earthPos, velocityVector*dt, out=earthPos, casting='unsafe')
        #print(accelerationVector)
        #print(math.sqrt(np.dot(accelerationUnitVector, accelerationUnitVector)))
        dlist.append([time, earthPos[0], earthPos[1], velocityVector[0], velocityVector[1]])
        time += dt
        
    return (sunPos-earthPos)




"""Set an input for either Euler, Euler-Cramer approximations etc"""
# --- Request user input on which approximation to use --- #

print("For a simple singlar body orbiting the sun we can approximate the orbit in multiple ways")
print("\t")
print("The options of Approximation are Euler and Euler-Cramer")
print("\t")
approximation = input("Enter 1 for Euler, enter 2 for Euler-Cramer or 3 to close the program:  ")


"""
Once the approximation has been selected we have to make sure the program is able to run based on the input given.
This is done using a simple if comparison against their approximation number choice.
It must be such that if they havent chosen an appropriate value that the program doesnt fail.




"""
choice = approximation.replace("!, 
    
if int(approximation) == 1:

        print("The Euler approximation will now run")
        print(earthEuler())
        print("A text file has been generated with the output values")
        input("Press any key to close the program")
      
elif int(approximation) == 2:

        print("The Euler-Cramer approximation will now run")
        print(earthEulerCramer())
        print("A text file has been generated with the output values from the approximation")
        input("Press any key to close the program")

elif int(approximation) == 3:

        print("The program will now close")
        time.sleep(3)




with open("orbitpoints2.txt", "w") as File: # This creates and opens a new text document
    #then labels the document "File"
    for n in range(0, len(dlist)):
        # Every value must be written in
        File.write(str(dlist[n][1])) # The time value is added first
        File.write("\t") # A white space is added so that data is split into two columns
        File.write(str(dlist[n][2])) # The acceleration value is added next
        File.write("\n") # a new line is added so this may repeat for all programs
