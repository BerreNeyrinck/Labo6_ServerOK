import sys
import platform
import subprocess


def myping(host):
    # Choose parameter based on OS
    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    # Constructing the ping command
    command = ["ping", parameter, "1", host]
    response = subprocess.call(command)

    # Interpreting the response
    return response == 0

# add = 0.0
  
# # Getting the length of command 
# # line arguments 
# n = len(sys.argv) 
  
# for i in range(1, n): 
#     add += float(sys.argv[i]) 
#     print(sys.argv[i])
  
# print ("the sum is :", add) 
