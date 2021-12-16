#!/usr/bin/env python3

def check_winner(board):
    for i in range(0,len(board[0])):
        if not False in [row[i][1] for row in board]:
            return True

    for row in board:
        if not False in [e[1] for e in row]:
            return True

def play_number(boards, play):
    for board in boards:
        for row in board:
            for num in row:
                if num[0] == play:
                    num[1] = True
                    if check_winner(board):
                        return board
                    
    return None

boards = []
with open('input.txt') as f:
    plays = [int(e) for e in f.readline().strip().split(',')]

    board = []
    for line in f.readlines():
        if line.strip() == '':
            if len(board) > 0:
                boards.append(board)
                board = []
            continue

        board.append([[int(e),False] for e in line.strip().split()])
    if len(board) > 0:
        boards.append(board)

for play in plays:
    board = play_number(boards, play)
    if board:
        total = sum([sum([e[0] for e in row if e[1] is False]) for row in board])
        print(total * play)
        break
