import os

#making directory
# os.mkdir("/home/prajwalmac/python_self/os_module/os_demo")


#checking if the directory is present or not
if (not os.path.exists("/home/prajwalmac/python_self/os_module/os_demo")):
    os.mkdir("/home/prajwalmac/python_self/os_module/os_demo") #creates a directory if not present
else:
    print(f"The directory is present")


#returns the type of os 
print(f"The os of the systen is {os.name}")


#returns the no of CPU in the device
print(f"This device has {os.cpu_count()} CPU's")


#Return the name of the user logged in on the controlling terminal
print(os.getlogin())


#return the current directory
print(os.getcwd())