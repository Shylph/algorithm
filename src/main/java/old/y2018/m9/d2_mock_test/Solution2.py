def get_r(works):
    result = 0
    for i in works:
        result = result + i**2
    return result


def solution(no, works):
    result = 0
    if no > sum(works):
        return 0
    for i in range(no):
        works.sort(reverse=True)
        # print(works)
        works[0] = works[0] - 1
    # print(works)
    result = get_r(works)
    return result



n = [4, 2, 0, ]
m = [[4,3,3], [3,3,3] ,[2]]
out = [12, 17, 4]

for i in range(len(n)):
    answer = solution(n[i], m[i])
    if out[i] == answer:
        print(i, "true")
    else:
        print(i, "false : expect :", out[i], " : but :", answer)
