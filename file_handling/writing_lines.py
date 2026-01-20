
with open("/home/prajwalmac/python_self/file_handling/intro.txt","w") as f:
    lines = ["line1","line2","line3","line4"]
    for line in lines:
        f.write(line + "\n")