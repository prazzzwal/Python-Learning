
#readline() is used to read a single line and it can be looped to read multiple lines

with open("/home/prajwalmac/python_self/file_handling/intro.txt") as f:
  for lines in f:
    print(lines)