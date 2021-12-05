from collections import Counter

f = open("input.txt", "r")
#$f = open("testInput.txt", "r")
dat = f.read().splitlines()

nums = [int(d) for d in dat[0].split(",")]

i = 2
boards = []
while i < len(dat):
    board = []
    #print(i)

    # get board
    while i < len(dat) and dat[i] != "":
        board.append([int(d) for d in dat[i].split(" ") if d])
        i += 1
    
    boards.append(board)
    i += 1

# for b in boards:
#     for r in b:
#         print(r)
    
#     print()

# print()

def v(b,i):
    for k in range(len(b)):
        if b[k][i] != -1:
            return False
    
    return True

def h(b,j):
    for k in b[j]:
        if k != -1:
            return False
    
    return True

def unmarked(b):
    total = 0
    for r in b:
        for k in r:
            if k != -1:
                total += k
    
    return total

for g in nums:
    for board in boards:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if g == board[i][j]:
                    #print("mf")
                    board[i][j] = -1

                    # if g == 24:
                    #     print("mf")
                    #     for r in boards[2]:
                    #         print(r)
                    #     print()

                    if v(board,j) or h(board,i):
                        ub = unmarked(board)
                        print(ub, g,ub*g )
                        exit()








    






