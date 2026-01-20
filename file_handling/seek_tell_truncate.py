
with open("/home/prajwalmac/python_self/file_handling/intro.txt","r") as f:
    
    #move to the 10th byte in the file
    f.seek(10)

    current_position = f.tell()
    print(f"The current position is {current_position}")

    #read the next 5 bytes
    next_bytes = f.read(5)
    print(f"{next_bytes}")

with open("/home/prajwalmac/python_self/file_handling/intro.txt","a") as f:
    #truncate function can only be used in write or append mode
    #truncating the file size to 10 bytes
    final_bytes = f.truncate(10)

with open("/home/prajwalmac/python_self/file_handling/intro.txt","r") as f:
    contents = f.read()
    print(contents)