
#write mode creates new file if the file isnt present

# when with statement is used there is not need to close the file, it is closed auto

with open("/home/prajwalmac/python_self/file_handling/intro.txt","w") as f:
    f.write("Hi , Myself Prajwal ")

