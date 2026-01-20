import os

# creating multiple folder inside a directory
for i in range(1,11):
    if(not os.path.exists(f"/home/prajwalmac/python_self/os_module/os_demo/Python_Day{i}")): #checking if the directory exists or not
            os.mkdir(f"/home/prajwalmac/python_self/os_module/os_demo/Python_Day{i}")

#removing directories from a directory
for i in range(6,11):
    if(os.path.exists(f"/home/prajwalmac/python_self/os_module/os_demo/Python_Day{i}")):
        os.rmdir(f"/home/prajwalmac/python_self/os_module/os_demo/Python_Day{i}")

#displaying the directories and files inside them

folders = os.listdir(f"/home/prajwalmac/python_self/os_module/os_demo/")

for folder in folders:
    print(folder)
    print(os.listdir(f"/home/prajwalmac/python_self/os_module/os_demo/{folder}"))