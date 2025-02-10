import random
import numpy as np
#intialize the array fir tge first time
board = np.zeros((8, 8), dtype=int)
count = 1
for columns in range(8):
    rows = random.randint(0, 7)
    board[rows, columns] = 1



#shows the board when needed
def show_board(board):
    for row in board:
        for item in row:
            print(item, end=" ")
        print()
    print("---------")





#Todo
#check rows
#check diagonols
#look into numpy for this
#https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html
#https://sparkbyexamples.com/numpy/how-to-get-numpy-diagonal/
#https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/
#https://numpy.org/doc/stable/reference/generated/numpy.trace.html
def heuristicScore(board):
    conflicts = 0
    size = 8

    for row in range(size):
        for col in range(size):
#check for value of 1 before calculations using numpy
            if board[row, col] ==1:
                # Check conflicts in the same row
                conflicts += np.sum(board[row, col +1:] == 1)
#use trace to sum the diagnols and account for counting values twice
#sweep main diag
                diag = np.trace(board, offset=col -row)
                conflicts = conflicts+ diag
#sweep reverse diag
                reverseDiag = np.trace(np.fliplr(board), offset=(size -col -1) -row)
#account for the trace adding the sum of the diag and anati diag
                conflicts = conflicts- 2
                conflicts = conflicts + reverseDiag

    return conflicts
#Todo
#check compare scores
#check restart if board is worse then current
#continue looping until 0 or max atteampt
#print relavent info
#https://www.geeksforgeeks.org/introduction-hill-climbing-artificial-intelligence/#
def restart(board):
    restartAttempts = 0
    restartsAllowed = int(input("Enter the number of restarts for this attempt: "))
    currentScore = heuristicScore(board)


    while currentScore > 0 and restartAttempts < restartsAllowed:
        possibilities = possibilitiesGenerator(board)
 #dummy data to intialize variables
        bestPossibility = None
        newScore = float('inf')
#tries all the possible outcomes generated
        for i in possibilities:
            possibilityScore = heuristicScore(i)
#checks if the score is better then the other possibilitys
            if possibilityScore < newScore:
                bestPossibility = i
                newScore = possibilityScore
#if possible score better then current score replace it  and show new board
        if newScore < currentScore:
            print("Current board state:")
            show_board(bestPossibility)
            print("Current number of conflicts:",newScore)
            print("Current restart value:",restartAttempts)

            board = bestPossibility
            currentScore = newScore
        else:
            print("Best new board was worse than the current board... restarting")
#genrate new board if no possible outcomes
            for col in range(8):
                row = np.random.randint(0,7)
                board[row,col] = 1

            currentScore = heuristicScore(board)
            restartAttempts = restartAttempts +1

    if currentScore == 0:
        print("-----------------")
        show_board(board)
        print("Solution found!")
    else:
        print("No suitable solution found")

#Todo
#loop through and move pieces to try various outcomes
#https://towardsdatascience.com/how-to-implement-the-hill-climbing-algorithm-in-python-1c65c29469de
def possibilitiesGenerator(board):
    possibleOutcomes = []
    for col in range(8):
        for row in range(8):
            if board[row, col] == 1:
        #loop over all the rows to generate every possible postion
                for i in range(8):
                    if i != row:
                        trial = np.copy(board)
                        trial[row, col] = 0
                        trial[i, col] = 1
                        possibleOutcomes.append(trial)

    return possibleOutcomes



restart(board)
