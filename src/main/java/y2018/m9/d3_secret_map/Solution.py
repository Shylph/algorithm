def solution(n, arr1, arr2):
    result = []
    for i in range(len(arr1)):
        result.append(bin(arr1[i] | arr2[i]))
        result[i] = result[i].replace("0b", "")
        if len(result[i]) != n:
            result[i] = "0" * (n - len(result[i])) + result[i]
        result[i] = result[i].replace("1", "#")
        result[i] = result[i].replace("0", " ")
    return result


n = [5, 6]
arr1 = [[9, 20, 28, 18, 11], [46, 33, 33, 22, 31, 50]]
arr2 = [[30, 1, 21, 17, 28], [27, 56, 19, 14, 14, 10]]
out = [["#####", "# # #", "### #", "# ##", "#####"], ["######", "### #", "## ##", " #### ", " #####", "### # "]]

for i in range(len(n)):
    answer = solution(n[i], arr1[i], arr2[i])
    if out[i] == answer:
        print(i, "true")
    else:
        print(i, "false : expect :", out[i], " : but :", answer)
