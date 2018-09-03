def solution(n, m):
    palindrome_cnt = 0
    for i in range(n, m):
        raw = list(str(i))
        cnt = 0
        flag = True
        for j in range(len(raw)):
            if raw[j] == raw[len(raw) - 1 - j]:
                cnt = cnt + 1
            else:
                flag = False
        if cnt > len(raw)/2 and flag == True:
            palindrome_cnt = palindrome_cnt + 1

    return palindrome_cnt


n = [1, 100]
m = [100, 300]
out = [18, 20]

for i in range(len(n)):
    answer = solution(n[i], m[i])
    if out[i] == answer:
        print(i, "true")
    else:
        print(i, "false : expect :", out[i], " : but :", answer)
