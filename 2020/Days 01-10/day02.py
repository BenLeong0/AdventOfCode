inputs = [];

ranges = [];
letters = [];
passwords = [];


with open('day02.in', 'r') as f:
    for line in f:
        inputs.append(line[:-1].split(' '));

for input in inputs:
    ranges.append(input[0].split('-'));
    letters.append(input[1][0]);
    passwords.append(input[2])


# counter = 0
# for i in range(len(passwords)):
#     letter_count = passwords[i].count(letters[i]);
#     if int(ranges[i][0]) <= letter_count <= int(ranges[i][1]):
#         counter += 1;

counter = 0
for i in range(len(passwords)):
    a = (letters[i] == passwords[i][int(ranges[i][0]) - 1])
    b = (letters[i] == passwords[i][int(ranges[i][1]) - 1])
    if (a and not b) or (b and not a):
        counter += 1;


print(counter)
