'''Docstring are string literal that appear 
after the function,method,class or module declaration 
that describes the working of the function
'''
##Zen of Python
import this

def print_name():
    """ Function takes user's name as input and greets the user"""
    name = input("\nEnter your name: ")
    print(f"Hello {name}")

print_name()

#prinitng the docstring content
print(print_name.__doc__)