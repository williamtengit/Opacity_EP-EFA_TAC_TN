from itertools import chain, combinations
from z3 import *
import graphviz

Max_Domain = 40
# domain function for the first parameter
def domain1(x1):
    return And(x1 > 0, x1 <= Max_Domain)

# domain function for the second parameter
def domain2(x2):
    return And(x2 > 0, x2 <= Max_Domain)

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

# the function return all solutions for a solver
def allSolution(solver):
    solutions = []
    i = 1;
    solver_variables = []
    for line in solver.sexpr().split('\n'):
        if 'declare-fun' in line:
            var_name = line.split()[1]
            solver_variables.append(var_name)
    while solver.check() == sat:
        model = solver.model()
        solutions.append(model)
        block = []
        # print("========================");
        for d in model:
            # print(i, end=" ")
            i = i + 1
            c = d()
            # print(c,end=" ")
            # print(d)
            block.append(c != model[d])
        solver.add(Or(block))
    return solutions

# define states class in a FAs model
class State:
    def __init__(self, name):
        self.name = name
        self.transitions = set()

    def add_transition(self, input_symbol, next_state):
        if (input_symbol, next_state) not in self.transitions:
            self.transitions.add((input_symbol, next_state))

    def __repr__(self):
        return self.name

# define FA class
class StateMachine:
    def __init__(self):
        self.states = {}
        self.initial_state = None

    def add_state(self, state):
        """add a state to FA model"""
        self.states[state.name] = state

    def set_initial_state(self, initial_state_name):
        """set the initial state"""
        self.initial_state = self.states[initial_state_name]

    def draw(self, output_file="fsm.png", format="png"):
        """draw the FA model"""
        graph = graphviz.Digraph(format=format)
        for state in self.states.values():
            graph.node(state.name)
            for input_symbol, next_state in state.transitions:
                graph.edge(state.name, next_state.name, label=input_symbol)
        graph.render(output_file, format=format, cleanup=True, view=True)


#define global variables
FA_model = StateMachine()
stateset = {}
stateset["q0"] = State("q0")
stateset["q1"] = State("q1")
stateset["q2"] = State("q2")
stateset["q3"] = State("q3")
stateset["q4"] = State("q4")
solver = Solver()
solver.reset()
x1, x2, x3, x4 = Ints('x1 x2 x3 x4')
all_obs_x = set()
solver.reset()
solver.add(And(theta(x1), domain1(x1)))
for sol in allSolution(solver):
    all_obs_x.add(str(sol[x1]))

#construct function for  FA objects
def constuctFA():
    solver.reset()
    solver.add(And(phi1(x1),domain1(x1)))
    for sol in allSolution(solver):
        stateset["q0"].add_transition(str(sol[x1]), stateset["q1"])

    solver.reset()
    solver.add(And(phi4(x1),domain1(x1)))
    for sol in allSolution(solver):
        stateset["q3"].add_transition(str(sol[x1]), stateset["q4"])

    solver.reset()
    solver.add(And(phi5(x1),domain1(x1)))
    for sol in allSolution(solver):
        stateset["q2"].add_transition(str(sol[x1]), stateset["q2"])

    solver.reset()
    solver.add(And(phi6(x1),domain1(x1)))
    for sol in allSolution(solver):
        stateset["q4"].add_transition(str(sol[x1]), stateset["q4"])

    solver.reset()
    solver.add(And(phi2(x1,x2),domain1(x1),domain2(x2)))
    x1set=set()
    allsol = allSolution(solver);
    for sol in allsol:
        x1set.add(sol[x1])
    for xvalue in x1set:
        stateset["q3_"+str(xvalue)] = State("q3_"+str(xvalue))
        stateset["q0"].add_transition(str(xvalue), stateset["q3_"+str(xvalue)])
    for sol in allsol:
        for xvalue in x1set:
            if sol[x1] == xvalue:
                stateset["q3_"+str(xvalue)].add_transition(str(sol[x2]), stateset["q3"])
    solver.reset()
    solver.add(And(phi3(x1,x2),domain1(x1),domain2(x2)))
    x1set=set()
    allsol = allSolution(solver);
    for sol in allsol:
        x1set.add(sol[x1])
    for xvalue in x1set:
        stateset["q2_"+str(xvalue)] = State("q2_"+str(xvalue))
        stateset["q1"].add_transition(str(xvalue), stateset["q2_"+str(xvalue)])
    for sol in allsol:
        for xvalue in x1set:
            if sol[x1] == xvalue:
                stateset["q2_"+str(xvalue)].add_transition(str(sol[x2]), stateset["q2"])

    for state in stateset:
        FA_model.add_state(stateset[state])
    # FA_model.draw()


# secret state set and non-secret state set for current state opacity
Q_s = set({"q2"})
Q_ns = set({"q0", "q1", "q3", "q4"})

# secret state set and non-secret state set for infinite step opacity
Q_s_infinite = set({"q3"})
Q_ns_infinite = set({"q4"})

# initial state set
q_0 = set({"q0"})
