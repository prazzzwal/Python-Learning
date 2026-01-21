numbers = []

def take_input():
    print(f"Enter 5 numbers: ")
    for i in range(1,6):
        num = int(input())
        numbers.append(num)

    square = lambda x: x**2

    squared_list = list(map(square,numbers))
    print(f"The list after squaring:\n {squared_list}")


    even_list = list(filter(lambda x:x%2==0,squared_list))
    print(f"The list of even squares :\n {even_list}")

take_input()