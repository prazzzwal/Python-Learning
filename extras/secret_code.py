import random
import string


def encrypt():
    """
    Takes a string as input, slices the letter at the front,
    then adds it to the end of the string and randomly adds
    3 alphabets at the front and back.
    """
    try:
        message = input("Enter the word you want to encode: ")
        if (len(message)<3):
            encoded_message = message[::-1]  # reversing the string
            print(f"{encoded_message}")
        else:
            front = ''.join(random.choice(string.ascii_letters) for _ in range(3)) # generates 3 random alphabets
            back = ''.join(random.choice(string.ascii_letters) for _ in range(3))
            
            sep = message[0] #storing first lieral for further encoding
            half_message = message[1:] # slicing the string
            
            encoded_message = half_message + sep

            final_encoded_message = front + encoded_message + back

            print(f"The encoded message is {final_encoded_message}")
    except ValueError:
        print("Invalid Input!")


def decrypt():
    """
    Takes a string as input, slices 3 letters at the front and back,
    then slices the string at length - 1 and adds the last character
    back to the front to retrieve the original message.
    """
    try:
        encoded_message = input("Enter the word you want to decode: ")
        if (len(encoded_message)<3):
            message = encoded_message[::-1]  # reversing the string
            print(f"{message}")
        else:
           #removing the front and back alphabets

           stripped_string = encoded_message[3:-3:]
           sep = stripped_string[len(stripped_string)-1]
           splitted_message = stripped_string[:-1:]
           final_message = sep + splitted_message

           print(f"The decoded meassage is {final_message}")

    except ValueError:
        print("Invalid Input!")


def main_body():
    operation = int(input("Enter \n1.Encode \n2.Decode\n"))

    match operation:
        case 1:
            encrypt()
        case 2:
            decrypt()
        case _:
            print(f"Invalid Input")          

main_body()
