import re


def solution(str1, str2):
    p = re.compile("[a-zA-Z][a-zA-Z]")
    str1 = [str1[0 + i:2 + i] for i in range(len(str1) - 1)]
    str1_list = list(filter(lambda s: p.match(s), str1))
    str1_list = [s.lower() for s in str1_list]
    str1_list.sort()

    str2 = [str2[0 + i:2 + i] for i in range(len(str2) - 1)]
    str2_list = list(filter(lambda s: p.match(s), str2))
    str2_list = [s.lower() for s in str2_list]
    str2_list.sort()

    sum = []
    index1 = 0
    index2 = 0
    for i in range(min(len(str1_list), len(str2_list))):
        if str1_list[i] == str2_list[i]:
            sum.append(str1_list[i])
            index1 += 1
            index2 += 1
        elif str1_list[i] > str2_list[i]:
            sum.append(str2_list[i])
            index2 += 1
        else:
            sum.append(str1_list[i])
            index1 += 1
    for i in range(min(len(str1_list), len(str2_list)), max(len(str1_list), len(str2_list))):
        if len(str1_list) > len(str2_list):
            sum.append(str1_list[i])
        else:
            sum.append(str2_list[i])

    intersection = []
    set1 = set(str1_list)
    set2 = set(str2_list)

    big = str2_list
    small = str1_list
    if len(str1_list) > len(str2_list):
        big = str1_list
        small = str2_list
    rast_key = ""
    key_index = 0
    for key in small:
        count1 = big.count(key)
        count2 = small.count(key)
        if count1 > count2:
            for j in range(count2):
                intersection.append(key)
        else:
            for j in range(count1):
                intersection.append(key)
        if key in big:
            key_index += 1
    index = key_index
    index += 1
    if index <= len(big):
        for i in range(index, len(big)):
            intersection.append(big[index])

    if len(sum) == 0:
        return 1 * 65536

    return int((len(intersection)) / (len(sum)) * 65536)


str1 = ["FRANCE", "handshake", "aa1+aa2", "E=M*C^2"]
str2 = ["french", "shake hands", "AAAA12", "e=m*c^2"]
answer = [16384, 65536, 43690, 65536]

for i in range(len(answer)):
    result = solution(str1[i], str2[i])
    if answer[i] == result:
        print(i, "true")
    else:
        print(i, "false : expect :", answer[i], " : but :", result)
