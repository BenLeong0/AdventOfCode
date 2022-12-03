from string import ascii_lowercase

count = 0


## PART 1
# with open('inputs/day06.in', 'r') as f:
#     group = set()
#     while True:
#         line = f.readline()
#         if not line:
#             count += len(group)
#             group = set()
#             break
#         line = line[:-1]
#         if not line:
#             count += len(group)
#             group = set()
#         else:
#             group = group.union({i for i in line})


with open('inputs/day06.in', 'r') as f:
    group = {i for i in ascii_lowercase}
    while True:
        line = f.readline()
        if not line:
            count += len(group)
            break
        line = line[:-1]
        if not line:
            count += len(group)
            group = {i for i in ascii_lowercase}
        else:
            group = {i for i in group if i in line}


print(count)
