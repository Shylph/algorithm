def mean(arr):
    return sum(arr) / len(arr)


def var(arr):
    m = mean(arr)
    return sum([(i - m) * (i - m) for i in arr]) / len(arr)


def std(arr):
    return var(arr) ** 0.5


def solution():
    n, k = map(int, input().split(" "))
    dolls = list(map(int, input().split(" ")))
    doll_len = len(dolls)
    stds = []
    for j in range(k):
        for i in range(doll_len - k + 1 - j):
            stds.append(std(dolls[i:k + i + j]))
    print(min(stds))


solution()
