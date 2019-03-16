import subprocess

a=raw_input("enter your interface:")

b=raw_input("enter yout mac:")

subprocess.call("ifconfig " + a + " down",shell=True)

subprocess.call("ifconfig  " + a + " hw ether " + b ,shell=True)

subprocess.call("ifconfig " + a + " up",shell=True)
