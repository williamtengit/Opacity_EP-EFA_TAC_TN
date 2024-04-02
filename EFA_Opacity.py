import time
from itertools import chain, combinations
from z3 import *
import EFA_model1
import EFA_model1_reverse

# powerset function for sets, return all non-empty subsets for a set.
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1,len(s) + 1))


# epsilon-reach function
def ereach(qobs, EFA_model):
    qobs_done = set()
    #print(qobs)
    while qobs - qobs_done != set():
        for q in qobs - qobs_done:
            for i in EFA_model.src[q]:
                #print(i, " ", T[i - 1][0])
                if s.check(EFA_model.T[i - 1][0]) == sat:
                    if EFA_model.des[i] not in qobs:
                        qobs.add(EFA_model.des[i])
            qobs_done.add(q)
    return tuple(qobs)


# generate the set of states of the symbolic observer for a EFA_model
def genObserver(q_0_obs, EFA_model):
    Q_obs_done.clear()
    Q_obs.clear()
    q0_obs = ereach(q_0_obs, EFA_model1)
    # print(q0_obs)
    Q_obs.add(q0_obs)
    # print(Q_obs)

    while Q_obs - Q_obs_done != set():
        for q_obs in Q_obs - Q_obs_done:
            for k in {1,2,3,4}:
                T_k_obs_idx = set()
                for q in q_obs:
                    for i in EFA_model.src[q]:
                        #print(i, "#########################################")
                        if len(EFA_model.T[i-1]) > k:
                            if s.check(EFA_model.T[i-1][k]) == sat:
                                T_k_obs_idx.add(i-1)
                # print("&&&&&&&&", T_k_obs_idx ,"&&&&&&&&&&&&&")
                # for j in T_k_obs_idx:
                #     print(j,k,T[j][k], '++++++++++++++++++++++++++++++++++++++')
                # print(k, "=======================================")
                # print(T_k_obs_idx)
                for sub_idx in powerset(T_k_obs_idx):
                    phi_idx = True;
                    for j in sub_idx:
                        phi_idx = And(phi_idx, EFA_model.T[j][k])
                    for j in T_k_obs_idx:
                        if j not in sub_idx:
                            phi_idx = And(phi_idx, Not(EFA_model.T[j][k]))
                    # print(sub_idx)
                    # print(phi_idx)
                    # print("#########################################")
                    if(s.check(phi_idx)) == sat:
                        new_obs_state = set()
                        for j in sub_idx:
                            # print(j,"here")
                            new_obs_state.add(EFA_model.des[j+1])
                        new_obs_state = ereach(new_obs_state, EFA_model)
                        if all(set(new_obs_state) != set(tup) for tup in Q_obs):
                            # print(new_obs_state)
                            Q_obs.add(new_obs_state)
            Q_obs_done.add(q_obs)
            # print(Q_obs, "   ====  ", Q_obs_done, "   ====> ", Q_obs - Q_obs_done)
            # Q_obs.update()


# the function for the verification of current state opacity of EFA_Model,
# also for the verification of initial state opacity, as the latter can be reduced to the former.

 # Qns denotes the set of non-secret states, and Qs denotes the set of secret states
def cso(Q_ns, Q_s):
    for q_obs in Q_obs:
        if set(q_obs).intersection(Q_ns) != set() and set(q_obs).intersection(Q_s) == set():
            return False;
    return True;

# the function for verification of infinite step opacity for EFA_Model
# Q_obs1 denotes the set of the states of observer, Q_obs1 denotes the set of the states of reverse observer,
# Q_ns denotes the set of non-secret states, Q_s denotes the set of secret states
def inf_step_opacity(Q_obs1,Q_obs2,Q_ns,Q_s):
    for q_obs1 in Q_obs1:
        for q_obs2 in Q_obs2:
            if (set(q_obs1).intersection(set(q_obs2))).intersection(Q_ns) != set() and (set(q_obs1).intersection(set(q_obs2))).intersection(Q_s) == set():
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
# print("the state set of observer: ", Q_obs_obverse)

# print(Q_obs_done)

####################################### Initial State Opacity verification ##################################
EFA_model1_reverse.construct_Reverse_EFA()
genObserver(EFA_model1_reverse.q_0, EFA_model1_reverse)
print("initial state opaque: ", cso(EFA_model1_reverse.Q_s_initial, EFA_model1_reverse.Q_ns_initial), \
      "for Q_s=", EFA_model1_reverse.Q_s_initial, "and Q_ns=", EFA_model1_reverse.Q_ns_initial)
# print(Q_obs)
# print(Q_obs_done)
Q_obs_reverse = Q_obs
# print("the state set of reverse observer: ", Q_obs_reverse)

####################################### Infinite Step Opacity verification ##################################
print("infinite step opaque: ", inf_step_opacity(Q_obs_obverse,Q_obs_reverse,EFA_model1.Q_s_infinite,EFA_model1.Q_ns_infinite), \
      "for Q_s=", EFA_model1.Q_s_infinite, "and Q_ns=", EFA_model1.Q_ns_infinite)

