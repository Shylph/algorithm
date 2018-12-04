import copy
def rec(n, signs):
    signs = copy.deepcopy(signs)
    for i in range(n):
        for j in range(n):
            if signs[i][j] == 1:
                for k in range(n):
                    if signs[i][k] != 1 and signs[j][k] == 1:
                        signs[i][k] = 1
    return signs

def solution(n, signs):
    answer = rec(n, signs)
    while answer != signs:
        signs = answer
        answer = rec(n, answer)

    return signs


n = [3, 3]
m = [[[0, 1, 0], [0, 0, 1], [1, 0, 0]], [[0, 0, 1], [0, 0, 1], [0, 1, 0]]]
out = [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 1, 1], [0, 1, 1], [0, 1, 1]]]

for i in range(len(n)):
    answer = solution(n[i], m[i])
    if out[i] == answer:
        print(i, "true")
    else:
        print(i, "false : expect :", out[i], " : but :", answer)
