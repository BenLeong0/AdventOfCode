expenses = [];

with open('day01.in', 'r') as f:
    for line in f:
        expenses.append(int(line[:-1]))

def f(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == 2020:
                return array[i] * array[j]

def g(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                if array[i] + array[j] + array[k] == 2020:
                    return array[i] * array[j] * array[k]

print(f(expenses))
print(g(expenses))
