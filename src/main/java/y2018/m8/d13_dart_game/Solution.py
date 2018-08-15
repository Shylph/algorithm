import re


def solution(data):
    p = re.compile("\d*\d")
    scores = list(map(int, p.findall(data)))
    p = re.compile("\D*\D")
    suffixes = p.findall(data)
    for i in range(len(scores)):
        for suffix in list(suffixes[i]):
            if suffix == "D":
                scores[i] = scores[i] ** 2
            elif suffix == "T":
                scores[i] = scores[i] ** 3
            elif suffix == "#":
                scores[i] = -scores[i]
            elif suffix == "*":
                scores[i] = scores[i] * 2
                if i > 0:
                    scores[i - 1] = scores[i - 1] * 2
    return sum(scores)


inputs = ["1S2D*3T", "1D2S#10S", "1D2S0T", "1S*2T*3S", "1D#2S*3S", "1T2D3D#", "1D2S3T*"]
out = [37, 9, 3, 23, 5, -4, 59]

for i in range(len(inputs)):
    if out[i] == solution(inputs[i]):
        print(i, "true")
    else:
        print(i, "false : expect :", out[i], " : but :", solution(inputs[i]))
