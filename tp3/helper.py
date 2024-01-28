import random
from readWriteFiles import *


# get colors for filled puzzle tiles
def generateColors(puzzle):
    colors = colorList()
    colorFill = []
    for i in range(len(puzzle)):
        colorFill.append([])
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 1:
                index = random.randint(0, len(colors)-1)
                color = colors[index]
                colorFill[i].append(color)
            else:
                colorFill[i].append(None)
    return colorFill

def generatePuzzle(rows, cols):
    # generate puzzle
    # check if solvable
    # if solvable, return 
    # if not solvable, generate new puzzle

    puzzle = []
    # generate a row
    for i in range (rows):
        newRow = generateRow([], cols)
        puzzle.append(newRow)
    return puzzle


def generateRow(row, cols):
    # use 0 for empty cells and 1 for filled cells
    # randomly pick how many empty or filled cells until row is full
    x = random.randint(0,1)
    if x == 1:
        fill = True
    else:
        fill = False
    while len(row) < 10:
        rowLen = len(row)
        if fill:
            y = 1
        else:
            y = 0
        count = random.randint(0, cols - rowLen)
        for j in range(count):
            row.append(y)
        fill = not fill
    if isEmpty(row):
        return generateRow([], cols)
    else:
        return row
    

def isEmpty(L):
    for elem in L:
        if elem == 1:
            return False
    return True


# loop through puzzle to get number of tiles in a row in each row and col
def getRowCol(puzzle):
    rows = []
    for i in range(len(puzzle)):
        rows.append([])
        count = 0
        for tile in puzzle[i]:
            if tile == 1:
                count += 1
            elif count > 0:
                rows[i].append(count)
                count = 0
        if count != 0:
            rows[i].append(count)
        if rows[i] == []:
            rows[i] = [0]
        
    cols = []
    for i in range (len(puzzle[0])):
        cols.append([])
        count = 0
        for j in range (len(puzzle)):
            if puzzle[j][i] == 1:
                count += 1
            elif count > 0:
                cols[i].append(count)
                count = 0
        if count != 0:
            cols[i].append(count)
        if cols[i] == []:
            cols[i] = [0]
    return [rows, cols]




