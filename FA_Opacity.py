from itertools import chain, combinations
from z3 import *
import FA_model1
import FA_model1_reverse

# FA_model1 = FA_model3
# FA_model1_reverse = FA_model3_reverse
# epsilon-reach function
def ereach(qobs, FA):
    qobs_done = set()
    while qobs - qobs_done != set():
        for q in qobs - qobs_done:
            for transition in FA.FA_model.states[q].transitions:
                if FA.theta(int(transition[0])) == False:
                    if transition[1] not in qobs:
                        qobs.add(transition[1].name)
            qobs_done.add(q)
    return tuple(qobs)


# generate the set of states of the observer for a FA_model
def genObserver(q_0_obs, FA):
    Q_obs_done.clear()
    Q_obs.clear()
    # print(q_0_obs)
    q0_obs = ereach(q_0_obs, FA)
    # print(q0_obs)
    Q_obs.add(q0_obs)
    while Q_obs - Q_obs_done != set():
        for q_obs in Q_obs - Q_obs_done:
            for obs_x in FA.all_obs_x:
                new_obs_state = set()
                for q in q_obs:
                    for tran in FA.FA_model.states[q].transitions:
                        if tran[0] == obs_x:
                            new_obs_state.add(tran[1].name)
                new_obs_state = ereach(new_obs_state, FA)
                if new_obs_state != set() and all( set(new_obs_state) != set(tup) for tup in Q_obs ):
                    Q_obs.add(tuple(new_obs_state))
                    # print(q_obs,"-->",obs_x,"-->",new_obs_state)
            Q_obs_done.add(q_obs)

# the function for the verification of current state opacity of FA_Model,
# also for the verification of initial state opacity, as the latter can be reduced to the former.

 # Qns denotes the set of non-secret states, and Qs denotes the set of secret states
def cso(Q_s, Q_ns):
    for q_obs in Q_obs:
        if set(q_obs).intersection(Q_ns) == set() and set(q_obs).intersection(Q_s) != set():
            # print(q_obs)
            return False;
    return True;

# the function for verification of infinite step opacity for FA_Model
# Q_obs1 denotes the set of the states of observer, Q_obs1 denotes the set of the states of reverse observer,
# Q_ns denotes the set of non-secret states, Q_s denotes the set of secret states
def inf_step_opacity(Q_obs1,Q_obs2,Q_s, Q_ns):
    for q_obs1 in Q_obs1:
        for q_obs2 in Q_obs2:
            if (set(q_obs1).intersection(set(q_obs2))).intersection(Q_ns) == set() and (set(q_obs1).intersection(set(q_obs2))).intersection(Q_s) != set():
                # print(q_obs1,q_obs2)
                return False
    return True

s = Solver()

solutions = []
ss = Solver()

q0_obs = set()
Q_obs = set()
Q_obs_done = set()




####################################### Current State Opacity verification ##################################

FA_model1.constuctFA()
genObserver(FA_model1.q_0, FA_model1)
print("current state opaque: ", cso(FA_model1.Q_s, FA_model1.Q_ns), \
      "for Q_s=", FA_model1.Q_s, "and Q_ns=", FA_model1.Q_ns)
Q_obs_obverse = Q_obs
# print("the state set of observer: ", Q_obs_obverse)



####################################### Initial State Opacity verification ##################################
FA_model1_reverse.constuctReverseFA()
genObserver(FA_model1_reverse.q_0, FA_model1_reverse)
print("initial state opaque: ", cso(FA_model1_reverse.Q_s_initial, FA_model1_reverse.Q_ns_initial), \
      "for Q_s=", FA_model1_reverse.Q_s_initial, "and Q_ns=", FA_model1_reverse.Q_ns_initial)
# print(Q_obs)
Q_obs_reverse = Q_obs
ys_state=("q0","q1","q2","q3","q4")
# print("test");
# print("the state set of reverse observer: ", all(set(qq_obs).intersection(set(ys_state)) for qq_obs in Q_obs_reverse))

# ####################################### Infinite Step Opacity verification ##################################

print("infinite step opaque: ", inf_step_opacity(Q_obs_obverse,Q_obs_reverse,FA_model1.Q_s_infinite,FA_model1.Q_ns_infinite), \
      "for Q_s=", FA_model1.Q_s_infinite, "and Q_ns=", FA_model1.Q_ns_infinite)
