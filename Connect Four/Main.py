import random
def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []

    for r in range(height):
        row = [0] * width  # a row containing width 0s
        grid += [row]

    return grid
a = create_grid(3,5)
# print(a)

## Support code ##
def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and one space between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid) #rows of list
    width = len(grid[0])#columns of list

    for r in range(height):
        for c in range(width):
            print(grid[r][c], end=' ')  # print a space instead of a newline
        print()  # at end of row, go to next line
# print_grid(a)


def mod_grid(grid, n):
    #FILL IN THIS FUNCTION WITH YOUR CODE  
    height = len(grid)
    width = len(grid[0])
    for r in range(height):
        for c in range(width):
            grid[r][c] = grid[r][c]%n
    pass
mygrid = [[1, 0, 1, 1], [0, 1, 1, 1], [0, 1, 1, 0]]
# print_grid(mygrid)


def mod_grid_new(grid,n):
    #FILL IN THIS FUNCTION WITH YOUR CODE

    height = len(grid)
    width = len(grid[0])
    new_grid = create_grid(height,width)
    for r in range(height):
        for c in range(width):
            new_grid[r][c] = grid[r][c]%n
    return new_grid
    pass
# print_grid(mygrid)
# print()
# print_grid(mod_grid_new(mygrid,2))
# print()
# print_grid(mygrid)


# ##
# ##  Problem 5.1c)
# ##

def diagonal_grid(height,width):

	#FILL IN THIS FUNCTION WITH YOUR CODE.
    grid = create_grid(height,width)
    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1
    return grid

    pass
b = diagonal_grid(6,8)
# print_grid(b)

def inner_grid(height,width):
	#FILL IN THIS FUNCTION WITH YOUR CODE,
    new_grid = create_grid(height,width)
    for r in range(1,height-1):
        for c in range(1,width-1):
            new_grid[r][c] = 1
    return new_grid
    pass
c = inner_grid(5,5)
# print_grid(c)

def random_grid(height,width):
	#FILL IN THIS FUNCTION WITH YOUR CODE.
    #Do not worry about writing test cases for this function
    new_grid = create_grid(height,width)
    for r in range(1,height-1):
        for c in range(1,width-1):
            new_grid[r][c] = random.choice([0,1])
    return new_grid
    pass
d = random_grid(10,10)
print_grid(d)


def copy(grid):
	#FILL IN THIS FUNCTION WITH YOUR CODE.
    height = len(grid)
    width = len(grid[0])
    new_grid = create_grid(height,width)
    for r in range(height):
        for c in range(width):
            new_grid[r][c] = grid[r][c]
    return new_grid
    pass
e = copy(mygrid)
# print_grid(e)
# print()
# print_grid(mygrid)

def invert(grid):
	#FILL IN THIS FUNCTION WITH YOUR CODE.
    height = len(grid)
    width = len(grid[0])
    for r in range(height):
        for c in range(width):
            if (grid[r][c]== 0):
                grid[r][c] = 1
            else:
                grid[r][c] = 0
    pass

# print_grid(mygrid)
# print()
# invert(mygrid)
# print()
# print_grid(mygrid)
grid = diagonal_grid(5,5)
print_grid(grid)
print()
invert(grid)
print_grid(grid)

