import math
G = 4*math.pi**2
dt = 0.0005
maxnstep = 20
""" read positions and velocities into this file (masses will be generated in the calculations file)"""

# In solar masses
object_Masses = [
    1.0, 2.985*math.pow(10, -6), 9.49*math.pow(10, -4), 2.8417*math.pow(10, -4), 3.20855*math.pow(10, -7), 5.1*math.pow(10, -5)]


object_Positions = [[-5.53*math.pow(10, -4), 7.37*math.pow(10, -3), -6.252*math.pow(10, -5)], [0.278623, 0.9523992, -1.087035*math.pow(10, -4)], [
    -2.31, -4.825, 0.0717], [1.824, -9.8865, 0.0993], [1.27788494, 0.6363141635, -0.018253726], [28.9616675, -7.56068, -0.51175246]]  # test values currently put in


object_Velocities = [[-0.00282, 0.000794, 0.0000711], [
    -6.0955, 1.757, 1.21*math.pow(10, -4)], [2.45, -1.0585, -0.05037], [
        1.889, 0.3628, -0.0814], [-2.06, 5.01875, 0.1505163066], [
            0.281837, 1.115592474, -0.02935129]]
dimension = len(object_Positions[1])
