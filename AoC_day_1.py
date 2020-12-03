expenses = []

with open('day1inputs.txt') as f:
    for line in f:
        expenses.append(int(line))

minimum = 0
maximum = len(expenses)-1
expenses.sort()

print(expenses)