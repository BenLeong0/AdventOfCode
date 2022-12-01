test_ingredients = {
    "Butterscotch": [-1, -2, 6, 3, 8],
    "Cinnamon": [2, 3, -2, -1, 3],
}

full_ingredients = {
    "Sugar": [3, 0, 0, -3, 2],
    "Sprinkles": [-3, 3, 0, 0, 9],
    "Candy": [-1, 0, 4, 0, 1],
    "Chocolate": [0, 0, -2, 2, 8],
}


# Part 1

assert max([
    max(0, b*test_ingredients["Butterscotch"][0] + (100-b)*test_ingredients['Cinnamon'][0]) *
    max(0, b*test_ingredients["Butterscotch"][1] + (100-b)*test_ingredients['Cinnamon'][1]) *
    max(0, b*test_ingredients["Butterscotch"][2] + (100-b)*test_ingredients['Cinnamon'][2]) *
    max(0, b*test_ingredients["Butterscotch"][3] + (100-b)*test_ingredients['Cinnamon'][3])
    # max(0, b*test_ingredients["Butterscotch"][4] + (100-b)*test_ingredients['Cinnamon'][4])
    for b in range(101)
]) == 62842880

curr_max = -float("inf")
for i in range(101):
    for j in range(101-i):
        for k in range(101-i-j):
            l = 100-i-j-k
            curr_max = max(curr_max,
                max(0, sum([x*y[0] for x,y in zip((i,j,k,l), [full_ingredients[ing] for ing in full_ingredients])])) *
                max(0, sum([x*y[1] for x,y in zip((i,j,k,l), [full_ingredients[ing] for ing in full_ingredients])])) *
                max(0, sum([x*y[2] for x,y in zip((i,j,k,l), [full_ingredients[ing] for ing in full_ingredients])])) *
                max(0, sum([x*y[3] for x,y in zip((i,j,k,l), [full_ingredients[ing] for ing in full_ingredients])]))
            )
print(curr_max)


# Part 2

assert max([
    max(0, b*test_ingredients["Butterscotch"][0] + (100-b)*test_ingredients['Cinnamon'][0]) *
    max(0, b*test_ingredients["Butterscotch"][1] + (100-b)*test_ingredients['Cinnamon'][1]) *
    max(0, b*test_ingredients["Butterscotch"][2] + (100-b)*test_ingredients['Cinnamon'][2]) *
    max(0, b*test_ingredients["Butterscotch"][3] + (100-b)*test_ingredients['Cinnamon'][3])
    for b in range(101) if b*test_ingredients["Butterscotch"][4] + (100-b)*test_ingredients['Cinnamon'][4] == 500
]) == 57600000

curr_max = -float("inf")
for i in range(101):
    for j in range(101-i):
        for k in range(101-i-j):
            l = 100-i-j-k
            curr_max = max(curr_max,
                max(0, sum([x*y[0] for x,y in zip((i,j,k,l), [full_ingredients[ing] for ing in full_ingredients])])) *
                max(0, sum([x*y[1] for x,y in zip((i,j,k,l), [full_ingredients[ing] for ing in full_ingredients])])) *
                max(0, sum([x*y[2] for x,y in zip((i,j,k,l), [full_ingredients[ing] for ing in full_ingredients])])) *
                max(0, sum([x*y[3] for x,y in zip((i,j,k,l), [full_ingredients[ing] for ing in full_ingredients])])) *
                1 if sum([x*y[4] for x,y in zip((i,j,k,l), [full_ingredients[ing] for ing in full_ingredients])]) == 500 else 0
            )
print(curr_max)
