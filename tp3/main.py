from cmu_graphics import *
from helper import *
from startNew import *
import hint
import random
import readWriteFiles as rwf

class Player():
    def __init__(self, name):
        self.name = name
        self.puzzlesSolved = 0
        self.puzzlesMade = []
        self.puzzlesMadeColors = []
        self.puzzleInProg = []
        self.puzzleInProgColors = []
        self.currBoard = []
        self.currBoardColors = []
        self.currPuzzle = []
        self.currPuzzleColors = []
        self.savedBoard = []
        self.savedBoardColors = []
        self.lives = 9

    def __repr__(self):
        return str(self.name)
    

#base code for drawing the board from CS Academy 5.3.2


# states:  welcome screen (enter name), menu (choose mode), 
# generate puzzle, make your own puzzle, help screen (displays on top of current)
# welcome = 1, menu = 2, randomly generated puzzle = 3, 
# created puzzles = 4

def onAppStart(app):
    app.width = 1000
    app.height = 1000
    app.rows = 10
    app.cols = 10
    app.boardLeft = 200
    app.boardTop = 95
    app.boardWidth = 600
    app.boardHeight = 600
    app.cellBorderWidth = 2
    app.player = None
    app.players = []
    app.playersAll = False
    app.state = 1
    app.playerName = ''
    app.help = False
    app.currVals = None
    app.fill = True
    app.complete = False
    app.lose = False
    app.hintOn = False
    app.hint = None
    app.color = 'darkGray'

def redrawAll(app):
    # welcome screen
    if app.state == 1:
        drawLabel('Welcome! Please enter your name: ', 500, 300, size = 30)
        drawLabel(app.playerName, 500, 500, size = 20)
    # menu screen
    if app.state == 2:
        drawMenu(app)
        drawLabel('press \'h\' for help', 90, 750)

    # play generated puzzle
    if app.state == 3:
        drawLabel(f'Lives: {app.player.lives}', 900, 300, size = 20)
        drawBoard(app)
        drawBoardBorder(app)
        drawMenuButton(app)
        drawPlayer(app)
        drawButtons(app)
        drawVals(app, app.currVals)
        drawLabel('press \'h\' for help', 90, 750)
        drawHint(app)
        if app.complete:
            drawWin(app)
        if app.lose:
            drawLose(app)

    if app.state == 4:
        drawBoard(app)
        drawBoardBorder(app)
        drawMenuButton(app)
        drawPlayer(app)
        drawButtons(app)
        drawVals(app, app.currVals)
        drawColors(app)
        drawLabel('press \'h\' for help', 90, 750)
    
    if app.state == 5:
        drawMenuButton(app)
        drawPlayer(app)
        drawNoCustom(app)

    if app.help == True:
        drawHelp(app)
    pass

def drawHint(app):
    if app.hintOn:
        hintOn = 'black'
    else:
        hintOn = None
    drawRect(900, 700, 50, 50, align = 'center', fill = 'lavender', border = hintOn)
    drawLabel('hint', 900, 700, size = 20)

def drawColors(app):
    colors = rwf.colorList()
    for i in range(len(colors)):
        drawRect(900, 300 + 20*i, 50, 20, align = 'center', fill = colors[i])

def drawNoCustom(app):
    drawRect(500, 500, 700, 200, align = 'center', fill = 'lavender', 
             border = 'black')
    drawLabel('No custom puzzles made yet!', 500, 475, size = 35, 
              font = 'cursive')

def drawWin(app):
    drawRect(500, 500, 700, 200, align = 'center', fill = 'lavender', 
             border = 'black')
    drawLabel(f'Congrats! You have solved {app.player.puzzlesSolved} puzzle(s)',
              500, 475, size = 35, font = 'cursive')
    drawLabel('Press any key to return to the menu.', 500, 525, size = 35, 
              font = 'cursive')

def drawLose(app):
    drawRect(500, 500, 700, 200, align = 'center', fill = 'lavender', 
             border = 'black')
    drawLabel(f'Not quite! You have solved {app.player.puzzlesSolved} puzzle(s)',
              500, 475, size = 35, font = 'cursive')
    drawLabel('Press any key to try again.', 500, 525, size = 35, 
              font = 'cursive')


def drawMenuButton(app):
    drawRect(20, 10, 160, 65, fill = 'thistle', border = 'black')
    drawLabel('Menu', 100, 42, size = 40, font = 'cursive')

def drawPlayer(app):
    if not app.playersAll:
        drawRect(900, 42, 180, 60, fill = 'lavender', align = 'center')
        drawLabel(app.player, 900, 42, size = 30, font = 'cursive')
    else:
        for i in range(len(app.players)+1):
            drawRect(900, 42 + 60*i, 180, 60, fill = 'lavender', align = 'center')
            if i == len(app.players):
                drawLabel('New Player', 900, 42 + 60*i, size = 30, 
                      font = 'cursive')
            else:
                drawLabel(app.players[i], 900, 42 + 60*i, size = 30, 
                        font = 'cursive')
        

    

# menu screen
def drawMenu(app):
    drawRect(app.width/3, app.height/2, 200, 50, fill = 'lavender', 
                 border = 'orchid', align = 'center')
    drawRect(app.width*(2/3), app.height/2, 215, 50, fill = 'lavender', 
                 border = 'orchid', align = 'center')
    drawLabel('Solve puzzle', app.width/3, app.height/2, size = 30)
    drawLabel('Create puzzle', app.width*(2/3), app.height/2, 
                size = 30)
    drawRect(app.width/2, (app.height/2 + 100), 215, 50, fill = 'lavender', 
                 border = 'orchid', align = 'center')
    drawLabel('Created Puzzle', app.width/2, (app.height/2 + 100), size = 30)
    drawPlayer(app)

# draw help screen
def drawHelp(app):
    text = ['Each row and column has numbers representing lengths', 
            'of tiles in a row in the given row or column.', ' ',
            'Fill tiles by selecting the check and then the tile',
            'you wish to fill.', ' ', 'When making a puzzle,', 
            'press \'p\' to play and \'r\' to reset.',
            ' ', 'Press \'h\' again to exit this screen.']
    drawRect(500, 400, 600, 500, fill = 'lavender', border = 'orchid', 
             align = 'center')
    for i in range (len(text)):
        drawLabel(text[i], 500, 350 + 20*i, size = 20)
    pass

# draw fill and empty buttons
def drawButtons(app):
    if app.fill:
        widthX = 2
        widthCheck = 4
    else:
        widthX = 4
        widthCheck = 2
    drawRect(425, 750, 70, 70, align = 'center', fill = 'lightCyan', 
             border = 'steelBlue', borderWidth = widthX)
    drawRect(575, 750, 70, 70, align = 'center', fill = 'lightCyan',
             border = 'steelBlue', borderWidth = widthCheck)
    drawLine(400, 775, 450, 725, fill = 'gray', lineWidth = widthX)
    drawLine(400, 725, 450, 775, fill = 'gray', lineWidth = widthX)
    drawLine(550, 750, 565, 775, fill = 'plum', lineWidth = widthCheck)   
    drawLine(565, 775, 600, 725, fill = 'plum', lineWidth = widthCheck)  

# draw values along left and top
def drawVals(app, vals):
    rowVals, colVals = vals[0], vals[1]

    for i in range(len(rowVals)):
        L = (rowVals[i])[::-1]
        for j in range(len(rowVals[i])):
            number = str(L[j])
            x = 190 - 20*j
            y = 125 + 60*i
            drawLabel(number, x, y, size = 15)

    for i in range(len(colVals)):
        L = (colVals[i])[::-1]
        for j in range(len(colVals[i])):
            number = str(L[j])
            x = 230 + 60*i
            y = 85 - 20*j
            drawLabel(number, x, y, size = 15)



# draw board
def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col)

def drawBoardBorder(app):
    drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
        fill=None, border='black',
        borderWidth=2*app.cellBorderWidth)
    
def drawCell(app, row, col):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    tileRow, tileCol = locateTile(app, cellLeft+30, cellTop+20)
    tileState = app.player.currBoard[tileRow][tileCol]
    if tileState == 1:
        color = app.player.currBoardColors[tileRow][tileCol]
        drawRect(cellLeft, cellTop, cellWidth, cellHeight,
                fill=color, border='black',
                borderWidth=app.cellBorderWidth)
    elif tileState == -1:
        drawRect(cellLeft, cellTop, cellWidth, cellHeight,
                fill=None, border='black',
                borderWidth=app.cellBorderWidth)
    elif tileState == 0:
        drawRect(cellLeft, cellTop, cellWidth, cellHeight,
                fill=None, border='black',
                borderWidth=app.cellBorderWidth)
        drawLine(cellLeft+10, cellTop + 10, cellLeft+cellWidth-10, 
                 cellTop+cellHeight-10, fill = 'gray')
        drawLine(cellLeft+10, cellTop+cellHeight-10, cellLeft+cellWidth-10, 
                 cellTop + 10, fill = 'gray')
    elif tileState == -2:
        drawRect(cellLeft, cellTop, cellWidth, cellHeight,
                fill=None, border='black',
                borderWidth=app.cellBorderWidth)
        drawLine(cellLeft+10, cellTop + 10, cellLeft+cellWidth-10, 
                 cellTop+cellHeight-10, fill = 'red')
        drawLine(cellLeft+10, cellTop+cellHeight-10, cellLeft+cellWidth-10, 
                 cellTop + 10, fill = 'red')
    elif tileState == 2:
        drawRect(cellLeft, cellTop, cellWidth, cellHeight,
                fill='yellow', border='black',
                borderWidth=app.cellBorderWidth)


def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)


def onKeyPress(app, key):
    if app.state != 1:
        if key == 'h':
            app.help = not app.help
    if app.complete or app.lose:
        app.complete = False
        app.lose = False
        app.state = 2
    
    if app.state == 1:
        stateOneKeys(app, key)
    elif app.state == 4:
        stateFourKeys(app, key)

# check state and use correct mouse functions
def onMousePress(app, mouseX, mouseY):
    if app.state == 4:
        stateFourMouse(app,mouseX,mouseY)
    if app.state == 3:
        stateThreeMouse(app, mouseX, mouseY)
        saveProgress(app)
    if app.state == 2:
        stateTwoMouse(app, mouseX, mouseY)
    if app.state != 1 and app.state != 2:
        checkMenuButton(app, mouseX, mouseY)
    if app.state != 1:
        checkPlayer(app, mouseX, mouseY)

# welcome screen enter name and start    
def stateOneKeys(app, key):
    if key == 'enter':
        if app.playerName in app.players:
            pass
        else:
            app.playerName = Player(app.playerName)
            app.players.append(app.playerName)
        app.player = app.playerName
        app.state = 2
        app.playerName = ''
    elif key == 'space': 
        app.playerName += ' '
    elif key == 'backspace':
        if app.playerName == '':
            pass
        else:
            app.playerName = app.playerName[:-1]
    elif key.isalpha():
        app.playerName += key

def stateFourKeys(app, key):
    if key == 'p':
        app.player.currPuzzle = app.player.puzzlesMade
        app.player.currPuzzleColors = app.player.puzzlesMadeColors
        app.player.currBoard = emptyBoard()
        app.player.currBoardColors = emptyColors()
        app.currVals = getRowCol(app.player.currPuzzle)
        app.player.lives = 9
        app.state = 3
    if key == 'r':
        app.player.currBoard = emptyBoard()
        app.player.currBoardColors = emptyColors()
        app.currVals = getRowCol(app.player.currBoard)
        app.player.puzzlesMade = []


# mouse click for menu
def stateTwoMouse(app, x, y):
    if (app.height/2 - 25) <= y <= (app.height/2 + 25):
        # play random puzzle
        if (app.width/3 - 100) <= x <= (app.width/3 + 100):
            if app.player.puzzleInProg != []:
                app.player.currPuzzle = app.player.puzzleInProg
                app.player.currPuzzleColors = app.player.puzzleInProgColors
                app.player.currBoard = app.player.savedBoard
                app.player.currBoardColors = app.player.savedBoardColors
                app.currVals = getRowCol(app.player.currPuzzle)   
                app.player.savedBoard = []
                app.player.savedBoardColors = []
                app.player.puzzleInProg = []
                app.player.puzzleInProgColors = []
            else:
                app.player.lives = 9
                newPuzzle = startNewPuzzle()
                app.player.currPuzzle = newPuzzle[0]
                app.currVals = newPuzzle[1]
                app.player.currBoard = newPuzzle[2]
                app.player.currPuzzleColors = newPuzzle[3]
                app.player.currBoardColors = newPuzzle[4]
            app.state = 3
        # create puzzle
        elif (app.width*(2/3) - 100) <= x <= (app.width*(2/3) + 100):
            if app.player.puzzlesMade == []:
                app.player.currBoard = emptyBoard()
                app.player.currBoardColors = emptyColors()
            else:
                app.player.currBoard = app.player.puzzlesMade
                app.player.currBoardColors = app.player.puzzlesMadeColors
                if app.player.puzzlesMadeColors == []:
                    app.player.currBoardColors = emptyColors()
            app.currVals = getRowCol(app.player.currBoard)
            app.state = 4
    # other player's custom puzzle
    elif (393 <= x <= 607) and (app.height/2 + 75 <= y <= app.height/2 + 135):
        if len(app.players) <= 1:
            app.state = 5
        else:
            for player in app.players:
                if player != app.player:
                    app.player.lives = 9
                    app.player.currPuzzle = player.puzzlesMade
                    app.player.currPuzzleColors = player.puzzlesMadeColors
                    app.currVals = getRowCol(player.puzzlesMade)
                    app.player.currBoard = emptyBoard()
                    app.player.currBoardColors = emptyColors()
                    break
            app.state = 3

def stateThreeMouse(app, x, y):
    checkFill(app, x, y)
    if locateTile(app, x, y) != None:
        tileRow, tileCol = locateTile(app, x, y)
        if app.hint != None:
            i, j = app.hint
            if tileRow == i and tileCol == j:
                app.hintOn = False
        boardTile = app.player.currBoard[tileRow][tileCol]
        puzzleTile = app.player.currPuzzle[tileRow][tileCol]
        if app.fill:
            if puzzleTile == 1:
                (app.player).currBoard[tileRow][tileCol] = 1
                app.player.currBoardColors[tileRow][tileCol] = app.player.currPuzzleColors[tileRow][tileCol]
            elif boardTile == -1:
                (app.player).currBoard[tileRow][tileCol] = -2
                app.player.lives -= 1
        else:
            if boardTile == -1:
                (app.player).currBoard[tileRow][tileCol] = 0
            elif boardTile == 0:
                (app.player).currBoard[tileRow][tileCol] = -1
        # check row and col for completion
        if checkRow((app.player).currPuzzle, (app.player).currBoard, tileRow):
            for i in range(len(app.player.currPuzzle[0])):
                if (app.player).currBoard[tileRow][i] == -1:
                    (app.player).currBoard[tileRow][i] = 0
        if checkCol((app.player).currPuzzle, (app.player).currBoard, tileCol):
            for j in range(len(app.player.currPuzzle)):
                if (app.player).currBoard[j][tileCol] == -1:
                    (app.player).currBoard[j][tileCol] = 0
        
        app.complete = True
        for row in app.player.currBoard:
            if -1 in row:
                app.complete = False
        if app.complete:
            app.player.puzzlesSolved += 1
            app.player.puzzleInProg = []
                
        if app.player.lives <= 0:
            app.lose = True
            app.player.puzzleInProg = []
    elif (875 <= x <= 925) and (675 <= y <= 725):
        app.hintOn = not app.hintOn
        if app.hintOn:
            getHint(app)
    else:
        if app.hintOn:
            app.hintOn == False
            app.hint == None

def stateFourMouse(app, x, y):
    checkFill(app, x, y)
    checkColor(app, x, y)
    if locateTile(app, x, y) != None:
        tileRow, tileCol = locateTile(app, x, y)
        boardTile = app.player.currBoard[tileRow][tileCol]
        if app.fill:
            if boardTile == 1:
                (app.player).currBoard[tileRow][tileCol] = -1
                (app.player).currBoardColors[tileRow][tileCol] = None
            elif boardTile == -1:
                (app.player).currBoard[tileRow][tileCol] = 1
                (app.player).currBoardColors[tileRow][tileCol] = app.color
        else:
            if boardTile == -1:
                (app.player).currBoard[tileRow][tileCol] = 0
            elif boardTile == 0:
                (app.player).currBoard[tileRow][tileCol] = -1 
    app.currVals = getRowCol(app.player.currBoard)  
    app.player.puzzlesMade = app.player.currBoard
    app.player.puzzlesMadeColors = app.player.currBoardColors


# check if fill or empty is selected
def checkFill(app, x, y):
    if 715 <= y <= 785:
        if 390 <= x <= 460:
            app.fill = False
        elif 540 <= x <= 610:
            app.fill = True
        else:
            pass

# player button
def checkPlayer(app, x, y):
    if  810 <= x <= 990:
        if app.playersAll:
            index = findPlayer(app, y) #locatePlayer(app, x, y)
            if index == len(app.players):
                if app.state == 3:
                    app.player.savedBoard = app.player.currBoard
                    app.player.savedBoardColors = app.player.currBoardColors
                    app.player.puzzlesInProg = app.player.currPuzzle
                    app.player.puzzlesInProgColors = app.player.currPuzzleColors
                app.player = None
                app.state = 1
            elif index == None:
                app.playersAll = False
            else:
                if app.state == 3:
                        app.player.savedBoard = app.player.currBoard
                        app.player.puzzlesInProg = app.player.currPuzzle
                        app.player.savedBoardColors = app.player.currBoardColors
                        app.player.puzzlesInProgColors = app.player.currPuzzleColors
                app.player = app.players[index]
                app.state = 2
            app.playersAll = False
        elif 12 <= y <= 72:
            app.playersAll = True
    pass

# check which player is selected
def findPlayer(app, y):
    totPlayers = len(app.players)
    if 12 <= y <= (12+(totPlayers+1)*60):
        return (y-12)//60 
    return None

def locateTile(app, x, y):
    if (200 <= x <= 800) and (95 <= y <= 695):
        col = (x-200)//60
        row = (y - 95)//60
        return int(row), int(col)
    else:
        return None
    
def checkColor(app, x, y):
    colors = rwf.colorList()
    if 875 <= x <= 925 and 300 <= y <= 300 + 20*(len(colors)-1):
        index = (y-300)//20
        app.color = colors[index]
    pass

# check if menu button clicked
def checkMenuButton(app, x, y):
    if (20 <= x <= 180) and (10 <= y <= 75):
        saveProgress(app)
        app.state = 2

# save board and puzzle to individual player
def saveProgress(app):
    app.player.puzzleInProg = app.player.currPuzzle
    app.player.puzzleInProgColors = app.player.currPuzzleColors
    if app.state == 3:
        app.player.savedBoard = app.player.currBoard
        app.player.savedBoardColors = app.player.currBoardColors

  
def getHint(app):
    resultList = hint.findHint(app.currVals, app.player.currBoard)
    if resultList != None:
        i, j = resultList[0], resultList[1]
        fill = resultList[2]
        app.hint = i, j
        if fill:
            app.player.currBoard[i][j] = 2
        else:
            app.player.currBoard[i][j] = 0


def main():
    runApp()

main()