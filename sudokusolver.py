grid = [
    [0,7,0,0,9,0,0,3,1],
    [2,4,0,1,7,0,0,0,8],
    [1,0,8,5,6,0,0,0,0],
    [9,2,0,6,0,0,0,0,0],
    [0,1,3,0,0,0,2,8,0],
    [0,0,0,0,0,7,0,9,6],
    [0,0,0,0,3,2,9,0,5],
    [3,0,0,0,4,5,0,7,2],
    [7,5,0,0,1,0,0,4,0]
]

#solver uses recursion
def solver(grid):
    find = find_empty(grid)
    if not find:
        return True
    else: 
        row, col = find

    for i in range(1, 10):
        if valid(grid, i, (row,col)):
            grid[row][col] = i

            if solver(grid):
                return True
            grid[row][col] = 0
    return False    

def valid(grid, number, position):
    #check row
    for i in range(len(grid[0])):
        if grid[position[0]][i] == number and position[1] != i:
            return False
    #check column
    for i in range(len(grid)):
        if grid[i][position[1]] == number and position[0] != i:
            return False
    #check squares
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y *3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == number and (i, j) != position:
                return False
    return True

def grid_print(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print(" - - - - - - - - - - - - - ")
        for j in range(len(grid[0])):
            if j % 3 == 0 and j !=0:
                print("|", end="")
            if j == 8:
                print (grid[i][j])
            else:
               print(str(grid[i][j])+ " ", end="")

def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j) #row, col
    return None

solver(grid)
grid_print(grid)