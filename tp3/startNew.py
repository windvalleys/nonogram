import helper

def startNewPuzzle():
    puzzle = helper.generatePuzzle(10, 10)
    vals = helper.getRowCol(puzzle)
    playerBoard = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
    boardColors = helper.generateColors(playerBoard)
    colors = helper.generateColors(puzzle)
    result = [puzzle, vals, playerBoard, colors, boardColors]
    return result

def emptyBoard():
    playerBoard = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
           [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
    return playerBoard

def checkRow(puzzle, board, row):
    puzzRow = puzzle[row]
    boardRow = board[row]
    for i in range(len(puzzRow)):
        if puzzRow[i] == 1:
            if boardRow[i] != 1:
                return False
    return True

def checkCol(puzzle, board, col):
    puzzCol = []
    boardCol = []
    for i in range(len(puzzle)):
        puzzCol.append(puzzle[i][col])
        boardCol.append(board[i][col])
    for j in range(len(puzzCol)):
        if puzzCol[j] == 1:
            if boardCol[j] != 1:
                return False
    return True

def emptyColors():
    board = emptyBoard()
    colorBoard = helper.generateColors(board)
    return colorBoard
    