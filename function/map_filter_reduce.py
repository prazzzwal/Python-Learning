

from functools import reduce

salaries = [12000, 18000, 25000, 30000, 15000, 40000]

#map() function
increased_salary = list(map(lambda x : x + 0.1*x,salaries))

#filter() function
greater_salaries = list(filter(lambda x:x>20000,increased_salary))

#reduce() function
filtered_total_salary = reduce(lambda x,y: x+y,greater_salaries)

print(f"Updated salary list:\n{increased_salary}\n")

print(f"Filtered salary list:\n{greater_salaries}\n")

print(f"Total expense:\n{filtered_total_salary}\n")