# recursive hint function
import numpy as np 
import random
import copy


def findHint(vals, board):
    for i in range(len(board)):
        if -1 in board[i]:
            index = solveHint(vals[0][i], board[i])
            if index != None:
                result = [i, index, True]
                return result
    colsList = getColList(board)
    for j in range(len(colsList)):
        if -1 in colsList[j]:
            index = solveHint(vals[1][j], colsList[j])
            if index != None:
                result = [index, j, True]
                return result
            
    for i in range(len(board)):
        if -1 in board[i]:
            index = solveEmpty(vals[0][i], board[i])
            if index != None:
                result = [i, index, False]
                return result
    colsList = getColList(board)
    for j in range(len(colsList)):
        if -1 in colsList[j]:
            index = solveEmpty(vals[1][j], colsList[j])
            if index != None:
                result =  [index, j, False] 
                return result
    return
    


def getColList(board):
    boardCopy = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            boardCopy[i][j] = board[j][i]
    return boardCopy


def solveHint(vals, list):
    allPerms = cleanPerms(vals, list)
    index = 0
    if len(allPerms) < 1:
        return None
    while index < len(allPerms[0]):
        valsEqual = True
        while list[index] == 1:
            index += 1
            if index >= len(allPerms[0]):
                return None
        for perm in allPerms:
            if perm[index] != 1:
                valsEqual = False
                break
        if valsEqual:
            return index
        index += 1
    return None


def solveEmpty(vals, list):
    allPerms = cleanPerms(vals, list)
    index = 0
    if len(allPerms) < 1:
        return None
    while index < len(allPerms[0]):
        valsEqual = True
        while list[index] == 0:
            index += 1
            if index >= len(allPerms[0]):
                return None
        for perm in allPerms:
            if perm[index] != 0:
                valsEqual = False
                break
        if valsEqual:
            return index
        index += 1
    return None
            


# generates and cleans up possible solutions
def cleanPerms(vals, list):
    allPerms = permutations(vals, list, 0, [], [])
    i = 0
    while i < len(allPerms):
        j = 0
        while j < len(allPerms[0]):
            if not isinstance(allPerms[i][j],int):
                allPerms.pop(i)
                break
            else:
                j += 1
        i += 1
    return allPerms



# find all possible solutions to a row given values
def permutations(vals, list, index, perms, startList):
    if index == len(list):
        if isLegal(vals, startList):
            return startList
        return None
    
    copyList = copy.copy(startList)
    runCopy = False
    startVal = 1
    copyVal = 0

    # if a value is already solved, don't test other options
    if list[index] == 1:
        pass
    elif list[index] == -2:
        startVal = 0
    else:
        runCopy = True

    startList.append(startVal)
    copyList.append(copyVal)
    option1 = permutations(vals, list, index + 1, perms, startList)
    option2 = None
    if runCopy:
        option2 = permutations(vals, list, index + 1, perms, copyList)
    
    # check that the result is not empty
    if option1 != None and len(option1) == len(list):
        perms.append(option1)
    if option2 != None and len(option2) == len(list):
        perms.append(option2)
    return perms


def isLegal(vals, list):
    listVals = []
    count = 0
    for elem in list:
        if elem == 1:
            count += 1
        elif count != 0:
            listVals.append(count)
            count = 0
    if count != 0:
        listVals.append(count)
    if listVals == vals:
        return True
    return False
    

vals1 = [3, 3]
list1 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
index1 = 0
perms1 = []
startList1 = []

allPerms = permutations(vals1, list1, index1, perms1, startList1)

