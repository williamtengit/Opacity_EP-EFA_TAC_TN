import time
import subprocess
import sys

# start time
start_time = time.time()

# run the py program
script_path = r"D:\PYprojects\Opacity_EP-EFA_TAC_TN\EFA_Opacity.py"
subprocess.run([sys.executable, script_path])

# end time
end_time = time.time()

# total time
total_time = end_time - start_time
print("Total execution time:", total_time, "seconds")
