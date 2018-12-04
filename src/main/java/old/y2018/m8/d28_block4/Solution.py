import re


# 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)

def solution(m, n, board):
    board = [list(b) for b in board]
    board = [list(reversed([b[i] for b in board])) for i in range(n)]
    remove_target = get_remove_target(board)
    while not "".join([str.strip("".join(t)) for t in remove_target]) == "":
        for i in range(len(board)):
            for j in range(len(board[i]) - 1, -1, -1):
                if "*" == remove_target[i][j]:
                    del board[i][j]
        remove_target = get_remove_target(board)
    cnt = 0
    for b in board:
        cnt += len(b)
    return m * n - cnt


def get_remove_target(board):
    remove_target = [list(" " * len(board[i])) for i in range(len(board))]
    for i in range(len(board) - 1):
        for j in range(len(board[i]) - 1):
            try:
                if board[i][j] == board[i + 1][j] and board[i + 1][j] == board[i + 1][j + 1] and board[i + 1][j + 1] == \
                        board[i][j + 1]:
                    remove_target[i][j] = "*"
                    remove_target[i + 1][j] = "*"
                    remove_target[i][j + 1] = "*"
                    remove_target[i + 1][j + 1] = "*"
            except IndexError:
                continue
    return remove_target


m = [4, 6]
n = [5, 6]
board = [["CCBDE", "AAADE", "AAABF", "CCBBF"], ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]
answer = [14, 15]

for i in range(len(m)):
    solution1 = solution(m[i], n[i], board[i])
    if answer[i] == solution1:
        print(i, "true")
    else:
        print(i, "false : expect :", answer[i], " : but :", solution1)
