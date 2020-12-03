expenses = []

with open('day1inputs.txt') as f:
    for line in f:
        expenses.append(int(line))

min = 0
max = len(expenses)-1
expenses.sort()

#Two Sum
while min < max:
    sum = expenses[min] + expenses[max]
    if sum == 2020:
        print(expenses[min] * expenses[max])
        break

    if sum > 2020:
        max -= 1
    else:
        min += 1