This is a program for the opacity verification of the Extended Finite Autoamta with Event Parameters(EP-EFAs), 
and their Finite Automata counterpart with finite domain.

The files of "EFA_model1.py" and "EFA_model1_reverse.py" are for a specific EP-EFA and its reverse EP-EFA. 
The current files are for the EP-EFA as shown below.
<p align="center">
![fsm_symbolic png](https://github.com/williamtengit/Opacity_EP-EFA_TAC_TN/assets/68321173/46ab66f8-0a49-4287-b974-48e451b29d27)

        Fig 1. the EFA described by the current file of "EFA_model1.py"
<p>

Also, one can construct the new files of "EFA_model1.py" and "EFA_model1_reverse.py" for his EP-EFA model followed by this example. 

The files of "FA_model1.py" and "FA_model1_reverse.py" are for the FAs counterparts of the EP-EFA.
The current files are for the FA and its reverse FA corresponding to the EP-EFA described by "EFA_model1.py", 
and the FAs are shown below.
<p align="center">
![fsm png](https://github.com/williamtengit/Opacity_EP-EFA_TAC_TN/assets/68321173/49166d94-ac1c-4a31-879d-a3b63d2a847c)

            Fig 2. the counterpart FA (with domain [1,10]) for the EFA shown in Fig 1.
<p>

<p align="center">
![fsm_reverse png](https://github.com/williamtengit/Opacity_EP-EFA_TAC_TN/assets/68321173/3378e3d4-d390-4a85-aadb-cbb6ed40126f)

                                    Fig 3. the reverse of the FA shown in Fig 2.
<p>
By running "test_EFA_Opacity.py" in PyCharm, one can obtain the opacity properties of EFA described in "EFA_model1.py", and the total
execution time of the program.

By running "test_FA_Opacity.py" in PyCharm, one can obtain the opacity properties of FA described in "FA_model1.py", and the total
execution time of the program.
By changing the "Max_Domain = 40" to other numbers in the files of "FA_model1.py" and "FA_model1_reverse.py", one can set the finite
domain of the event parameters.

The total running time in my computer is as follows (When the total running time exceeds 300 seconds, we will consider the program timed out.).

	Table 1 : The total execution times for the verfication of opacity properties of EP-EFA and FA models in finite domains

![total_time](https://github.com/williamtengit/Opacity_EP-EFA_TAC_TN/assets/68321173/edba36fb-9ddd-4fd4-9f2e-3e0b4628abda)


From the table, it can be seen that the opacity verification complexity of EP-EFA is basically independent of the data domain, while for FA, opacity verification becomes almost infeasible when the data domain is large. 
This suggests that the EP-EFA model is more suitable for characterizing data flow in the system compared to the FA model.




