from itertools import chain, combinations
from z3 import *
import sys

Max_Domain = sys.maxsize

def domain1(x):
    return And(x > 0, x < Max_Domain)

# domain function for the second parameter
def domain2(x):
    return And(x > 0, x < Max_Domain)

# observation function for the parameter
def theta(x):
    return x >= 5



def phi7(x4,x3,x2,x1):
    return And(3*x1 + 2*x2 - 3*x3 + 4*x4 < 120, 3*x1 - 5*x4 > 12, 2*x1 - x3 + 2*x4 < 234, x3 + x4 - x1 + 2*x2 > 1024, 2*x1 - 4*x4 < 134)

def phi8(x5,x4,x3,x2,x1):
    return And(4*x1 + 5*x2 - 3*x3 - 4*x4 +10*x5 < 3062, 14*x1 - 8*x2 + 4*x3 + 2*x5 > 13,   2*x2 - 4*x3 - x4 - 6*x5 > 3)

# the condition for the "t1" transition
def phi1(x):
    return x < 4

# the condition for the "t2" transition
def phi2(y, x):
    return x + y > 9


# the condition for the "t3" transition
def phi3(y, x):
    return And(y == x + 1, x > 3)

# the condition for the "t4" transition
def phi4(x4,x3,x2,x1):
    return And(3*x1 + 2*x2 - 3*x3 + 4*x4 < 120, 3*x1 - 5*x4 > 12, 2*x1 - x3 + 2*x4 < 234, x3 + x4 - x1 + 2*x2 > 1024, 2*x1 - 4*x4 < 134)

def phi5(x5,x4,x3,x2,x1):
    return And(4*x1 + 5*x2 - 3*x3 - 4*x4 +10*x5 < 3062, 14*x1 - 8*x2 + 4*x3 + 2*x5 > 13,   2*x2 - 4*x3 - x4 - 6*x5 > 3)

# the condition for the "t6" transition
def phi6(x3,x2,x1):
    return And(2*x1 - 3*x2 + x3 > 143, 2*x2 + 5*x3 < 345, x1 - 2*x3 > 13)

# the condition for the "t1" transition
def phi11(x):
    return x < 4

# the condition for the "t2" transition
def phi21(x2, x1):
    return x1 + x2 > 9


# the condition for the "t3" transition
def phi31(x2, x1):
    return And(x2 == x1 + 1, x1 > 3)

# the condition for the "t4" transition
def phi41(x):
    return x < 7

# the condition for the "t5" transition
def phi51(x):
    return True

# the condition for the "t6" transition
def phi61(x):
    return True

# the condition for the "t1" transition
def phi12(x):
    return x < 4

# the condition for the "t2" transition
def phi22(x2, x1):
    return x1 + x2 > 9


# the condition for the "t3" transition
def phi32(x2, x1):
    return And(x2 == x1 + 1, x1 > 3)

# the condition for the "t4" transition
def phi42(x):
    return x < 7

# the condition for the "t5" transition
def phi52(x):
    return True

# the condition for the "t6" transition
def phi62(x):
    return True

# define the variables
x11, x12, x1, x2, x3, x4, x5, x6, x7, x8 = Ints('x11 x12 x1 x2 x3 x4 x5 x6 x7 x8')

# the observable transition set for "t1" - "t6", "t7" denotes the silent transition
T1 = []
T2 = []
T3 = []
T4 = []
T5 = []
T6 = []
T11 = []
T21 = []
T31 = []
T41 = []
T51 = []
T61 = []
T12 = []
T22 = []
T32 = []
T42 = []
T52 = []
T62 = []
T71 = []
T72 = []
T7 =  [True]
T = list()


# function for construct the EFA model in Examples 3 - 4
def construct_Reverse_EFA():
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
    T31.append(f300)
    T31.append(Or(f301, f310))
    T31.append(f311)

    # f40 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi4(x1)))
    # f41 = And(theta(x1), domain1(x1), phi4(x1))
    # T4.append(f40)
    # T4.append(f41)
    #
    # f50 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi5(x1)))
    # f51 = And(theta(x1), domain1(x1), phi5(x1))
    # T5.append(f50)
    # T5.append(f51)


    f40000 = Exists([x1, x2, x3, x4], And(Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f40001 = Exists([x2, x3, x4], And((theta(x1)), Not(theta(x2)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f40010 = Exists([x1, x3, x4], And((theta(x2)), Not(theta(x1)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f40100 = Exists([x1, x2, x4], And((theta(x3)), Not(theta(x1)), Not(theta(x2)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f41000 = Exists([x1, x2, x3], And((theta(x4)), Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f40011 = Exists([x3, x4], And((theta(x1)), (theta(x2)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f40101 = Exists([x2, x4], And((theta(x1)), (theta(x3)), Not(theta(x2)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f41001 = Exists([x2, x3], And((theta(x1)), (theta(x4)), Not(theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f40110 = Exists([x1, x4], And((theta(x2)), (theta(x3)), Not(theta(x1)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f41010 = Exists([x1, x3], And((theta(x2)), (theta(x4)), Not(theta(x1)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f41100 = Exists([x1, x2], And((theta(x3)), (theta(x4)), Not(theta(x1)), Not(theta(x2)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f40111 = Exists([x4],  And((theta(x1)), (theta(x2)), (theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f41011 = Exists([x3],  And((theta(x1)), (theta(x2)), (theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f41101 = Exists([x2],  And((theta(x1)), (theta(x2)), (theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f41110 = Exists([x1],  And((theta(x1)), (theta(x2)), (theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4)))
    f41111 = And((theta(x1)), (theta(x2)), (theta(x3)), (theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), phi7(x1, x2, x3, x4))
    T4.extend([f40000, Or(f40100,f40001,f40010,f40100, f41000),Or(f40011,f40101,f41001,f40110,f41010,f41100),Or(f40111,f41011,f41101,f41110),f41111])

    f500000 = Exists([x1, x2, x3, x4, x5], And(Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5),phi8(x1, x2, x3, x4, x5)))

    f500001 = Exists([x2, x3, x4, x5], And((theta(x1)), Not(theta(x2)), Not(theta(x3)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f500010 = Exists([x1, x3, x4, x5], And((theta(x2)), Not(theta(x1)), Not(theta(x3)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f500100 = Exists([x1, x2, x4, x5], And((theta(x3)), Not(theta(x1)), Not(theta(x2)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f501000 = Exists([x1, x2, x3, x5], And((theta(x4)), Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f510000 = Exists([x1, x2, x3, x4], And((theta(x5)), Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))

    f500011 = Exists([x3, x4, x5], And((theta(x1)), (theta(x2)), Not(theta(x3)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f500101 = Exists([x2, x4, x5], And((theta(x1)), (theta(x3)), Not(theta(x2)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f501001 = Exists([x2, x3, x5], And((theta(x1)), (theta(x4)), Not(theta(x2)), Not(theta(x3)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f500110 = Exists([x1, x4, x5], And((theta(x2)), (theta(x3)), Not(theta(x1)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f501010 = Exists([x1, x3, x5], And((theta(x2)), (theta(x4)), Not(theta(x1)), Not(theta(x3)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f501100 = Exists([x1, x2, x5], And((theta(x3)), (theta(x4)), Not(theta(x1)), Not(theta(x2)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f510001 = Exists([x2, x3, x4], And((theta(x1)), (theta(x5)), Not(theta(x2)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f510010 = Exists([x1, x3, x4], And((theta(x2)), (theta(x5)), Not(theta(x1)), Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f510100 = Exists([x1, x2, x4], And((theta(x3)), (theta(x5)), Not(theta(x1)), Not(theta(x2)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f511000 = Exists([x1, x2, x3], And((theta(x4)), (theta(x5)), Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))

    f500111 =  Exists([x4, x5],  And((theta(x1)), (theta(x2)), (theta(x3)), Not(theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f501011 =  Exists([x3, x5],  And((theta(x1)), (theta(x2)), (theta(x4)), Not(theta(x3)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f501101 =  Exists([x2, x5],  And((theta(x1)), (theta(x3)), (theta(x4)), Not(theta(x2)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f501110 =  Exists([x1, x5],  And((theta(x2)), (theta(x3)), (theta(x4)), Not(theta(x1)), Not(theta(x5)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f510011 =  Exists([x3, x4],  And((theta(x1)), (theta(x2)), theta(x5),   Not(theta(x3)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f510101 =  Exists([x2, x4],  And((theta(x1)), (theta(x3)), theta(x5),   Not(theta(x2)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f511001 =  Exists([x2, x3],  And((theta(x1)), (theta(x4)), theta(x5),   Not(theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f510110 =  Exists([x1, x4],  And((theta(x2)), (theta(x3)), theta(x5),   Not(theta(x1)), Not(theta(x4)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f511010 =  Exists([x1, x3],  And((theta(x2)), (theta(x4)), theta(x5),   Not(theta(x1)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))
    f511100 =  Exists([x1, x2],  And((theta(x3)), (theta(x4)), theta(x5),   Not(theta(x1)), Not(theta(x2)), domain1(x1), domain2(x2),  domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5)))

    f501111 =  Exists([x5], And(theta(x1), (theta(x2)), (theta(x3)), (theta(x4)), Not(theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5),phi8(x1, x2, x3, x4, x5)))
    f510111 =  Exists([x4], And(theta(x1), (theta(x2)), (theta(x3)), Not(theta(x4)), (theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5),phi8(x1, x2, x3, x4, x5)))
    f511011 =  Exists([x3], And(theta(x1), (theta(x2)), Not(theta(x3)), (theta(x4)), (theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5),phi8(x1, x2, x3, x4, x5)))
    f511101 =  Exists([x2], And(theta(x1), Not(theta(x2)), (theta(x3)), (theta(x4)), (theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5),phi8(x1, x2, x3, x4, x5)))
    f511110 =  Exists([x1], And(Not(theta(x1)), (theta(x2)), (theta(x3)), (theta(x4)), (theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5),phi8(x1, x2, x3, x4, x5)))

    f511111 =  And((theta(x1)), (theta(x2)), (theta(x3)), (theta(x4)), (theta(x5)), domain1(x1), domain2(x2), domain1(x3), domain2(x4), domain2(x5), phi8(x1, x2, x3, x4, x5))


    T5.extend([f500000, Or(f510000,f500001,f500010,f500100, f501000), Or(f500011,f500101,f501001,f500110,f501010,f501100,f510001, f510010, f510100, f511000),
    Or(f500111,f501011,f501101,f501110,f501111,f510011, f510101, f511001, f510110, f511010, f511100), Or(f501111,f510111,f511011,f511101, f511110), f511111])



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

    g10 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi1(x1)))
    g11 = And(theta(x1), domain1(x1), phi1(x1))
    T11.append(g10)
    T11.append(g11)

    g200 = Exists([x11, x12], And(Not(theta(x12)), Not(theta(x11)), domain1(x11), domain2(x12), phi2(x11, x12)))
    g201 = Exists(x11, And(Not(theta(x11)), theta(x1), domain1(x11), domain2(x1), phi2(x11, x1)))
    g210 = Exists(x12, And(Not(theta(x12)), theta(x1), domain1(x1), domain2(x12), phi2(x1, x12)))
    g211 = And(theta(x2), theta(x1), domain1(x1), domain2(x2), phi2(x1, x2))
    T21.append(g200)
    T21.append(Or(g201, g210))
    T21.append(g211)

    # g300 = Exists([x11, x12], And(Not(theta(x12)), Not(theta(x11)), domain1(x11), domain2(x12), phi3(x11, x12)))
    # g301 = Exists(x11, And(Not(theta(x11)), theta(x1), domain1(x11), domain2(x1), phi3(x11, x1)))
    # g310 = Exists(x12, And(Not(theta(x12)), theta(x1), domain1(x1), domain2(x12), phi3(x1, x12)))
    # g311 = And(theta(x2), theta(x1), domain1(x1), domain2(x2), phi3(x1, x2))
    # T31.append(g300)
    # T31.append(Or(g301, g310))
    # T31.append(g311)

    g3000 = Exists([x1, x2, x3], And(Not(theta(x1)), Not(theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2), domain1(x3), phi6(x1, x2, x3)))
    g3001 = Exists([x2, x3], And((theta(x1)), Not(theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3),  phi6(x1, x2, x3)))
    g3010 = Exists([x1, x3], And((theta(x2)), Not(theta(x1)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3),  phi6(x1, x2, x3)))
    g3100 = Exists([x1, x2], And((theta(x3)), Not(theta(x1)), Not(theta(x2)), domain1(x1), domain2(x2),  domain1(x3),  phi6(x1, x2, x3)))
    g3011 = Exists([x3], And((theta(x1)), (theta(x2)), Not(theta(x3)), domain1(x1), domain2(x2),  domain1(x3), phi6(x1, x2, x3)))
    g3101 = Exists([x2], And((theta(x1)), (theta(x3)), Not(theta(x2)), domain1(x1), domain2(x2),  domain1(x3), phi6(x1, x2, x3)))
    g3110 = Exists([x1], And((theta(x2)), (theta(x3)), Not(theta(x1)), domain1(x1), domain2(x2),  domain1(x3), phi6(x1, x2, x3)))
    g3111 = And((theta(x1)), (theta(x2)), (theta(x3)), domain1(x1), domain2(x2),  domain1(x3),  phi6(x1, x2, x3))
    T3.extend([g3000, Or(g3100,g3001,g3010),Or(g3011,g3101,g3110),g3111])

    g40 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi42(x1)))
    g41 = And(theta(x1), domain1(x1), phi42(x1))
    T41.append(g40)
    T41.append(g41)

    g50 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi52(x1)))
    g51 = And(theta(x1), domain1(x1), phi52(x1))
    T51.append(g50)
    T51.append(g51)

    g60 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi62(x1)))
    g61 = And(theta(x1), domain1(x1), phi62(x1))
    T61.append(g60)
    T61.append(g61)


    k10 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi1(x1)))
    k11 = And(theta(x1), domain1(x1), phi1(x1))
    T12.append(k10)
    T12.append(k11)

    k200 = Exists([x11, x12], And(Not(theta(x12)), Not(theta(x11)), domain1(x11), domain2(x12), phi2(x11, x12)))
    k201 = Exists(x11, And(Not(theta(x11)), theta(x1), domain1(x11), domain2(x1), phi2(x11, x1)))
    k210 = Exists(x12, And(Not(theta(x12)), theta(x1), domain1(x1), domain2(x12), phi2(x1, x12)))
    k211 = And(theta(x2), theta(x1), domain1(x1), domain2(x2), phi2(x1, x2))
    T22.append(k200)
    T22.append(Or(k201, k210))
    T22.append(k211)

    k300 = Exists([x11, x12], And(Not(theta(x12)), Not(theta(x11)), domain1(x11), domain2(x12), phi3(x11, x12)))
    k301 = Exists(x11, And(Not(theta(x11)), theta(x1), domain1(x11), domain2(x1), phi3(x11, x1)))
    k310 = Exists(x12, And(Not(theta(x12)), theta(x1), domain1(x1), domain2(x12), phi3(x1, x12)))
    k311 = And(theta(x2), theta(x1), domain1(x1), domain2(x2), phi3(x1, x2))
    T32.append(k300)
    T32.append(Or(k301, k310))
    T32.append(k311)

    k40 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi42(x1)))
    k41 = And(theta(x1), domain1(x1), phi42(x1))
    T42.append(k40)
    T42.append(k41)

    k50 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi52(x1)))
    k51 = And(theta(x1), domain1(x1), phi52(x1))
    T52.append(k50)
    T52.append(k51)

    k60 = Exists(x1, And(Not(theta(x1)), domain1(x1), phi62(x1)))
    k61 = And(theta(x1), domain1(x1), phi62(x1))
    T62.append(k60)
    T62.append(k61)

    T71.append(k300)
    T71.append(Or(k301, k310))
    T71.append(k311)
    T72.append(k300)
    T72.append(Or(k301, k310))
    T72.append(k311)

    #T11 --> T61: 7-->12    T12-->T62:  13--->18   T71-->T72: 19 20
    T.extend([T1, T2, T3, T4, T5, T6, T11, T21, T31, T41, T51, T61, T12, T22, T32, T42, T52, T62, T71, T72, T7])

# initial state set, secret state set and non-secret state set for initial state opacity
q_0  = set({"q0", "q1", "q2", "q3","q4", "q01", "q11", "q21", "q31","q41", "q02", "q12", "q22", "q32","q42"})
Q_s_initial  = set({"q2"})
Q_ns_initial = set({"q0","q1"})



# src = {"q0": [1, 2, 71, 72], "q1": [3], "q3": [4], "q2": [5], "q4": [6],
#        "q01": [11, 21], "q11": [31], "q31": [41], "q21": [51], "q41": [61],
#        "q02": [12, 22], "q12": [32], "q32": [42], "q23": [52], "q42": [62]}
# des = {1: "q1", 2: "q3", 3: "q2", 4: "q4", 5: "q2", 6: "q4",
#         11: "q11", 21: "q31", 31: "q21", 41: "q41", 51: "q21", 61: "q41",
#         12: "q12", 22: "q32", 32: "q22", 42: "q42", 52: "q22", 62: "q42",
#         71: "q01", 72:"q02"
#        }

# T11 --> T61: 7-->12    T12-->T62:  13--->18   T71-->T72: 19 20

# define the source and destination states for transitions
src = { "q0": [21], "q1": [1], "q3": [2], "q2": [3,5], "q4": [4,6],
        "q01": [19], "q11": [7], "q31": [8], "q21": [9,11], "q41": [10,7],
        "q02": [20], "q12": [13], "q32": [14], "q22": [15,17], "q42": [16,18]
       }
des = { 1: "q0", 2: "q0", 3: "q1", 4: "q3", 5: "q2", 6: "q4",
        7: "q01", 8: "q01", 9: "q11", 10: "q31", 11: "q21", 12: "q41", 19: "q0",
        13: "q02", 14: "q02", 15: "q12", 16: "q32", 17: "q22", 18: "q42", 20: "q0",
        21: "q0"
       }

