
#student MArks analyzer

marks = []
sum = 0
n = int(input("Enter number of students"))
for i in range(0, n):
    ip = float(input())
    marks.append(ip)
    sum+=ip

for i in range(0,n-1):
    max = 0
    min = 0
    if(marks[i]<marks[i+1]):
        max = marks[i+1]
        min = marks[i]
    else:
        max = marks[i]
        min = marks[i+1]

average = sum/n
print(f"The highest marks obtained by student is {max} and the lowest is {min}")
print(f"The average marks is {average}")
print(f"Total marks: {sum}")
