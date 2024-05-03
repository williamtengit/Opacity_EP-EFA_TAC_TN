import time
from itertools import chain, combinations
from z3 import *
import EFA_model1
import EFA_model1_reverse


# EFA_model1 = EFA_model3
# EFA_model1_reverse = EFA_model3_reverse
# powerset function for sets, return all non-empty subsets for a set.
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1,len(s) + 1))


# epsilon-reach function
def ereach(qobs, EFA_model):
    qobs_done = set()
    while qobs - qobs_done != set():
        for q in qobs - qobs_done:
            for i in EFA_model.src[q]:
                if s.check(EFA_model.T[i - 1][0]) == sat:
                    if EFA_model.des[i] not in qobs:
                        qobs.add(EFA_model.des[i])
            qobs_done.add(q)
    return tuple(qobs)


# generate the set of states of the symbolic observer for a EFA_model
def genObserver(q_0_obs, EFA_model):
    Q_obs_done.clear()
    Q_obs.clear()
    # print(q_0_obs)
    q0_obs = ereach(q_0_obs, EFA_model1)
    # print(q0_obs)
    Q_obs.add(q0_obs)
    while Q_obs - Q_obs_done != set():
        for q_obs in Q_obs - Q_obs_done:
            for k in {1,2,3,4}:
                T_k_obs_idx = set()
                for q in q_obs:
                    for i in EFA_model.src[q]:
                        if len(EFA_model.T[i-1]) > k:
                            if s.check(EFA_model.T[i-1][k]) == sat:
                                T_k_obs_idx.add(i-1)
                for sub_idx in powerset(T_k_obs_idx):
                    phi_idx = True;
                    for j in sub_idx:
                        phi_idx = And(phi_idx, EFA_model.T[j][k])
                    for j in T_k_obs_idx:
                        if j not in sub_idx:
                            phi_idx = And(phi_idx, Not(EFA_model.T[j][k]))
                    if(s.check(phi_idx)) == sat:
                        new_obs_state = set()
                        for j in sub_idx:
                            new_obs_state.add(EFA_model.des[j+1])
                        new_obs_state = ereach(new_obs_state, EFA_model)
                        if all(set(new_obs_state) != set(tup) for tup in Q_obs):
                            Q_obs.add(new_obs_state)
                            # print(q_obs,"-->", s.model()  ,"-->" ,new_obs_state)
            Q_obs_done.add(q_obs)


# the function for the verification of current state opacity of EFA_Model,
# also for the verification of initial state opacity, as the latter can be reduced to the former.

 # Qns denotes the set of non-secret states, and Qs denotes the set of secret states
def cso( Q_s, Q_ns):
    for q_obs in Q_obs:
        if set(q_obs).intersection(Q_ns) == set() and set(q_obs).intersection(Q_s) != set():
            # print(q_obs, Q_s, Q_ns)
            return False;
    return True;

# the function for verification of infinite step opacity for EFA_Model
# Q_obs1 denotes the set of the states of observer, Q_obs1 denotes the set of the states of reverse observer,
# Q_ns denotes the set of non-secret states, Q_s denotes the set of secret states
def inf_step_opacity(Q_obs1,Q_obs2,Q_s,Q_ns):
    for q_obs1 in Q_obs1:
        for q_obs2 in Q_obs2:
            if (set(q_obs1).intersection(set(q_obs2))).intersection(Q_ns) == set() and (set(q_obs1).intersection(set(q_obs2))).intersection(Q_s) != set():
                # print(q_obs1,q_obs2)
                return False
    return True


s = Solver()
solutions = []

q0_obs = set()
Q_obs = set()
Q_obs_done = set()

####################################### Current State Opacity verification ##################################

EFA_model1.construct_EFA()
genObserver(EFA_model1.q_0, EFA_model1)
print("current state opaque: ", cso(EFA_model1.Q_s, EFA_model1.Q_ns), \
      "for Q_s=", EFA_model1.Q_s, "and Q_ns=", EFA_model1.Q_ns)
Q_obs_obverse = Q_obs


####################################### Initial State Opacity verification ##################################
EFA_model1_reverse.construct_Reverse_EFA()
genObserver(EFA_model1_reverse.q_0, EFA_model1_reverse)
print("initial state opaque: ", cso(EFA_model1_reverse.Q_s_initial, EFA_model1_reverse.Q_ns_initial), \
      "for Q_s=", EFA_model1_reverse.Q_s_initial, "and Q_ns=", EFA_model1_reverse.Q_ns_initial)

Q_obs_reverse = Q_obs


####################################### Infinite Step Opacity verification ##################################
print("infinite step opaque: ", inf_step_opacity(Q_obs_obverse,Q_obs_reverse,EFA_model1.Q_s_infinite,EFA_model1.Q_ns_infinite), \
      "for Q_s=", EFA_model1.Q_s_infinite, "and Q_ns=", EFA_model1.Q_ns_infinite)

