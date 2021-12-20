import copy
from itertools import product
from typing import List, Literal, Tuple


Pixel = Literal['0','1']

def get_input(filename: str) -> Tuple[List[Pixel], List[List[Pixel]]]:
    with open(filename, "r", newline="\n") as readfile:
        file = readfile.read().replace('\r\n', '\n').split('\n\n')
        return (
            ['1' if x == "#" else '0' for x in file[0]], 
            [['1' if x == "#" else '0' for x in row] for row in file[1].split('\n')]
        )

test_algorithm, test_image = get_input("day20_test.in")
full_algorithm, full_image = get_input("day20.in")


# Shared
def get_empty_row(length: int) -> List[Pixel]:
    return ['0' for _ in range(length)]

def find_number_of_lit_pixels(
    algorithm: List[Pixel], 
    image: List[List[Pixel]], 
    iterations: int = 2
) -> int:
    image = copy.deepcopy(image)
    # Pad image (iterations + border)
    for _ in range(iterations+2):
        image = [get_empty_row(len(image[0]))] + image + [get_empty_row(len(image[0]))]
        image = [['0'] + row + ['0'] for row in image]

    # Iterate over all except outline and update
    for i in range(iterations):
        height, width = len(image), len(image[0])
        new_image = [get_empty_row(width) for __ in range(height)]
        for i, j in product(range(height), range(width)):
            if i in (0, height-1) or j in (0,width-1):
                key = int(image[i][j]*9, 2)     # Will be in homogenous area if on border
            else:
                # Flattens 3x3 around (i,j) to single string; eg [[a,b,c],[d,e,f],[g,h,i]] -> 'abcdefghi'
                key = int(''.join([''.join([image[x][y] for y in (j-1,j,j+1)]) for x in (i-1,i,i+1)]), 2)
            new_image[i][j] = algorithm[key]
        image = new_image
    
    return sum([row.count('1') for row in image])


# Part 1
assert find_number_of_lit_pixels(test_algorithm, test_image) == 35
print(find_number_of_lit_pixels(full_algorithm, full_image))  


# Part 2
assert find_number_of_lit_pixels(test_algorithm, test_image, 50) == 3351
print(find_number_of_lit_pixels(full_algorithm, full_image, 50))  
