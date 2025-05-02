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


def phi7(x1,x2,x3,x4):
    return And(3*x1 + 2*x2 - 3*x3 + 4*x4 < 120, 3*x1 - 5*x4 > 12, 2*x1 - x3 + 2*x4 < 234, x3 + x4 - x1 + 2*x2 > 1024, 2*x1 - 4*x4 < 134)

def phi8(x1,x2,x3,x4,x5):
    return And(4*x1 + 5*x2 - 3*x3 - 4*x4 +10*x5 < 3062, 14*x1 - 8*x2 + 4*x3 + 2*x5 > 13,   2*x2 - 4*x3 - x4 - 6*x5 > 3)


# the condition for the "t1" transition
def phi1(x):
    return x < 4

# the condition for the "t2" transition
def phi2(x1, x2):
    return x1 + x2 > 9

# the condition for the "t3" transition
def phi3(x1, x2):
    return And(x2 == x1 + 1, x1 > 3)

# the condition for the "t4" transition
def phi4(x):
    return x < 7

# the condition for the "t5" transition
def phi6(x1,x2,x3):
    return And(2*x1 - 3*x2 + x3 > 143, 2*x2 + 5*x3 < 345, x1 - 2*x3 > 13)

# the condition for the "t6" transition
def phi5(x):
    return True


# define the variables
x11, x12, x1, x2, x3, x4, x5, x6 = Ints('x11 x12 x1 x2 x3 x4 x5 x6')

# the observable transition set for "t1" - "t6", "t7" denotes the silent transition
T1 = []
T2 = []
T3 = []
T4 = []
T5 = []
T6 = []
T7 = []
T8 = []
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




    # f60 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi5(x1)))
    # f61 = And(theta(x1), domain1(x1), phi5(x1))
    # T6.append(f60)
    # T6.append(f61)

    f6000 = Exists([x1, x2, x3], And(Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2), domain1(x3), phi6(x1, x2, x3)))
    f6001 = Exists([x2, x3], And((theta(x1)), Not(theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3),  phi6(x1, x2, x3)))
    f6010 = Exists([x1, x3], And((theta(x2)), Not(theta(x1)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3),  phi6(x1, x2, x3)))
    f6100 = Exists([x1, x2], And((theta(x3)), Not(theta(x1)), Not(theta(x2)), domain1(x1), domain2(x2),  domain1(x3),  phi6(x1, x2, x3)))
    f6011 = Exists([x3], And((theta(x1)), (theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), phi6(x1, x2, x3)))
    f6101 = Exists([x2], And((theta(x1)), (theta(x3)), Not(theta(x2)), domain1(x1), domain2(x2),  domain1(x3), phi6(x1, x2, x3)))
    f6110 = Exists([x1], And((theta(x2)), (theta(x3)), Not(theta(x1)), domain1(x1), domain2(x2),  domain1(x3), phi6(x1, x2, x3)))
    f6111 = And((theta(x1)), (theta(x2)), (theta(x3)), domain1(x1), domain2(x2),  domain1(x3),  phi6(x1, x2, x3))
    T6.extend([f6000, Or(f6100,f6001,f6010),Or(f6011,f6101,f6110),f6111])



    f70000 = Exists([x1, x2, x3, x4], And(Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f70001 = Exists([x2, x3, x4], And((theta(x1)), Not(theta(x2)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f70010 = Exists([x1, x3, x4], And((theta(x2)), Not(theta(x1)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f70100 = Exists([x1, x2, x4], And((theta(x3)), Not(theta(x1)), Not(theta(x2)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f71000 = Exists([x1, x2, x3], And((theta(x4)), Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f70011 = Exists([x3, x4], And((theta(x1)), (theta(x2)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f70101 = Exists([x2, x4], And((theta(x1)), (theta(x3)), Not(theta(x2)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f71001 = Exists([x2, x3], And((theta(x1)), (theta(x4)), Not(theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f70110 = Exists([x1, x4], And((theta(x2)), (theta(x3)), Not(theta(x1)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f71010 = Exists([x1, x3], And((theta(x2)), (theta(x4)), Not(theta(x1)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f71100 = Exists([x1, x2], And((theta(x3)), (theta(x4)), Not(theta(x1)), Not(theta(x2)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f70111 = Exists([x4],  And((theta(x1)), (theta(x2)), (theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f71011 = Exists([x3],  And((theta(x1)), (theta(x2)), (theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f71101 = Exists([x2],  And((theta(x1)), (theta(x2)), (theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f71110 = Exists([x1],  And((theta(x1)), (theta(x2)), (theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f71111 = And((theta(x1)), (theta(x2)), (theta(x3)), (theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4))
    T7.extend([f70000, Or(f70100,f70001,f70010,f70100, f71000),Or(f70011,f70101,f71001,f70110,f71010,f71100),Or(f70111,f71011,f71101,f71110),f71111])

    f800000 = Exists([x1, x2, x3, x4, x5], And(Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5),phi8(x1, x2, x3, x4, x5)))

    f800001 = Exists([x2, x3, x4, x5], And((theta(x1)), Not(theta(x2)), Not(theta(x3)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f800010 = Exists([x1, x3, x4, x5], And((theta(x2)), Not(theta(x1)), Not(theta(x3)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f800100 = Exists([x1, x2, x4, x5], And((theta(x3)), Not(theta(x1)), Not(theta(x2)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f801000 = Exists([x1, x2, x3, x5], And((theta(x4)), Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f810000 = Exists([x1, x2, x3, x4], And((theta(x5)), Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))

    f800011 = Exists([x3, x4, x5], And((theta(x1)), (theta(x2)), Not(theta(x3)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f800101 = Exists([x2, x4, x5], And((theta(x1)), (theta(x3)), Not(theta(x2)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f801001 = Exists([x2, x3, x5], And((theta(x1)), (theta(x4)), Not(theta(x2)), Not(theta(x3)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f800110 = Exists([x1, x4, x5], And((theta(x2)), (theta(x3)), Not(theta(x1)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f801010 = Exists([x1, x3, x5], And((theta(x2)), (theta(x4)), Not(theta(x1)), Not(theta(x3)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f801100 = Exists([x1, x2, x5], And((theta(x3)), (theta(x4)), Not(theta(x1)), Not(theta(x2)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f810001 = Exists([x2, x3, x4], And((theta(x1)), (theta(x5)), Not(theta(x2)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f810010 = Exists([x1, x3, x4], And((theta(x2)), (theta(x5)), Not(theta(x1)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f810100 = Exists([x1, x2, x4], And((theta(x3)), (theta(x5)), Not(theta(x1)), Not(theta(x2)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f811000 = Exists([x1, x2, x3], And((theta(x4)), (theta(x5)), Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))

    f800111 =  Exists([x4, x5],  And((theta(x1)), (theta(x2)), (theta(x3)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f801011 =  Exists([x3, x5],  And((theta(x1)), (theta(x2)), (theta(x4)), Not(theta(x3)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f801101 =  Exists([x2, x5],  And((theta(x1)), (theta(x3)), (theta(x4)), Not(theta(x2)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f801110 =  Exists([x1, x5],  And((theta(x2)), (theta(x3)), (theta(x4)), Not(theta(x1)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f810011 =  Exists([x3, x4],  And((theta(x1)), (theta(x2)), theta(x5),   Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f810101 =  Exists([x2, x4],  And((theta(x1)), (theta(x3)), theta(x5),   Not(theta(x2)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f811001 =  Exists([x2, x3],  And((theta(x1)), (theta(x4)), theta(x5),   Not(theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f810110 =  Exists([x1, x4],  And((theta(x2)), (theta(x3)), theta(x5),   Not(theta(x1)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f811010 =  Exists([x1, x3],  And((theta(x2)), (theta(x4)), theta(x5),   Not(theta(x1)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f811100 =  Exists([x1, x2],  And((theta(x3)), (theta(x4)), theta(x5),   Not(theta(x1)), Not(theta(x2)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))

    f801111 =  Exists([x5], And(theta(x1), (theta(x2)), (theta(x3)), (theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5),phi8(x1, x2, x3, x4, x5)))
    f810111 =  Exists([x4], And(theta(x1), (theta(x2)), (theta(x3)), Not(theta(x4)), (theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5),phi8(x1, x2, x3, x4, x5)))
    f811011 =  Exists([x3], And(theta(x1), (theta(x2)), Not(theta(x3)), (theta(x4)), (theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5),phi8(x1, x2, x3, x4, x5)))
    f811101 =  Exists([x2], And(theta(x1), Not(theta(x2)), (theta(x3)), (theta(x4)), (theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5),phi8(x1, x2, x3, x4, x5)))
    f811110 =  Exists([x1], And(Not(theta(x1)), (theta(x2)), (theta(x3)), (theta(x4)), (theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5),phi8(x1, x2, x3, x4, x5)))

    f811111 =  And((theta(x1)), (theta(x2)), (theta(x3)), (theta(x4)), (theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5))


    T8.extend([f800000, Or(f810000,f800001,f800010,f800100, f801000), Or(f800011,f800101,f801001,f800110,f801010,f801100,f810001, f810010, f810100, f811000),
    Or(f800111,f801011,f801101,f801110,f801111,f810011, f810101, f811001, f810110, f811010, f811100), Or(f801111,f810111,f811011,f811101, f811110), f811111])


    T.extend([T1, T2, T3, T4, T5, T6, T7, T8])


# initial state set
q_0 = set({"q0"})

# secret state set and non-secret state set for current state opacity
Q_s  = set({"q2"})
Q_ns = set({"q0", "q1", "q3", "q4"})

# secret state set and non-secret state set for infinite step opacity
Q_s_infinite  = set({"q3"})
Q_ns_infinite = set({"q4"})

# define the source and destination states for transitions
src = {"q0": [1, 2], "q1": [3], "q3": [4], "q2": [5, 8], "q4": [6, 7]}
des = {1: "q1", 2: "q3", 3: "q2", 4: "q4", 5: "q2", 6: "q4", 7: "q0", 8:"q0"}