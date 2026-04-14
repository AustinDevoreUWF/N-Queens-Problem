def printBoard(n):
    board_size = n
    for i in range(board_size):
        for j in range(board_size):
            print("x",end=" ")
        print()
    print("Board size is: ",board_size)

printBoard()