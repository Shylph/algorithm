def solution(arr1, arr2):
    answer =  []
    for i in range(len(arr1)):
        answer.append([])
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            sum = 0
            for r1 in range(len(arr1[0])):
                sum = sum + arr1[i][r1] * arr2[r1][j]
            answer[i].append(sum)
    return answer


def solution2(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
