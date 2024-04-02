from itertools import chain, combinations
from z3 import *
import sys

Max_Domain = sys.maxsize
# domain function for the first parameter
def domain1(x):
    return And(x > 0, x < Max_Domain)

# domain function for the second parameter
def domain2(x):
    return And(x > 0, x < Max_Domain)

# observation function for the parameter
def theta(x):
    return x >= 5

# the condition for the "t1" transition
def phi1(x):
    return x < 4

# the condition for the "t2" transition
def phi2(x, y):
    return x + y > 9

# the condition for the "t3" transition
def phi3(x, y):
    return And(y == x + 1, x > 3)

# the condition for the "t4" transition
def phi4(x):
    return x < 7

# the condition for the "t5" transition
def phi5(x):
    return True

# the condition for the "t6" transition
def phi6(x):
    return True

# define the variables
x11, x12, x1, x2 = Ints('x11 x12 x1 x2')

# the observable transition set for "t1" - "t6", "t7" denotes the silent transition
T1 = []
T2 = []
T3 = []
T4 = []
T5 = []
T6 = []
T7 = [True]
T = list()

# function for construct the EFA model in Example 2
def construct_EFA():
    f10 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi1(x1)))
    f11 = And(theta(x1), domain1(x1), phi1(x1))
    T1.append(f10)
    T1.append(f11)

    f200 = Exists([x11, x12], And(Not(theta(x12)), Not(theta(x11)), domain1(x11), domain2(x12), phi2(x11, x12)))
    f201 = Exists(x11, And(Not(theta(x11)), theta(x1), domain1(x11), domain2(x1), phi2(x11, x1)))
    f210 = Exists(x12, And(Not(theta(x12)), theta(x1), domain1(x1), domain2(x12), phi2(x1, x12)))
    f211 = And(theta(x2), theta(x1), domain1(x1), domain2(x2), phi2(x1, x2))
    T2.append(f200)
    T2.append(Or(f201, f210))
    T2.append(f211)

    f300 = Exists([x11, x12], And(Not(theta(x12)), Not(theta(x11)), domain1(x11), domain2(x12), phi3(x11, x12)))
    f301 = Exists(x11, And(Not(theta(x11)), theta(x1), domain1(x11), domain2(x1), phi3(x11, x1)))
    f310 = Exists(x12, And(Not(theta(x12)), theta(x1), domain1(x1), domain2(x12), phi3(x1, x12)))
    f311 = And(theta(x2), theta(x1), domain1(x1), domain2(x2), phi3(x1, x2))
    T3.append(f300)
    T3.append(Or(f301, f310))
    T3.append(f311)

    f40 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi4(x1)))
    f41 = And(theta(x1), domain1(x1), phi4(x1))
    T4.append(f40)
    T4.append(f41)

    f50 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi5(x1)))
    f51 = And(theta(x1), domain1(x1), phi5(x1))
    T5.append(f50)
    T5.append(f51)

    f60 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi5(x1)))
    f61 = And(theta(x1), domain1(x1), phi5(x1))
    T6.append(f60)
    T6.append(f61)

    T.extend([T1, T2, T3, T4, T5, T6, T7])



# initial state set
q_0 = set({"q0"})

# secret state set and non-secret state set for current state opacity
Q_s  = set({"q2"})
Q_ns = set({"q0", "q1", "q3", "q4"})

# secret state set and non-secret state set for infinite step opacity
Q_s_infinite  = set({"q3"})
Q_ns_infinite = set({"q4"})

# define the source and destination states for transitions
src = {"q0": [1, 2], "q1": [3], "q3": [4], "q2": [5], "q4": [6]}
des = {1: "q1", 2: "q3", 3: "q2", 4: "q4", 5: "q2", 6: "q4"}