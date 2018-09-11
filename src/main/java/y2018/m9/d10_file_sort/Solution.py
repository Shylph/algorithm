import re
import operator


def solution(files):
    infos = []
    p = re.compile("(\D+)(0*)([0-9]+)")
    for i in range(len(files)):
        match = p.match(files[i])
        infos.append([match.group(1).lower(), int(match.group(3)),match.group(2),files[i]])

    infos = sorted(infos,key=operator.itemgetter(0, 1))

    return [i[3] for i in infos]


inputs = [["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]]
answer = [["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]]

for i in range(len(answer)):
    result = solution(inputs[i])
    if answer[i] == result:
        print(i, "true")
    else:
        print(i, "false : expect :", answer[i], " : but :", result)
