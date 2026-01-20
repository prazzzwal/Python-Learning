
# reading from a file
f = open("/home/prajwalmac/python_self/file_handling/hello.txt","r")
text = f.read()
print(text)
f.close() #file needs to be closed after it is closed
