import re


def solution(str1, str2):
    p = re.compile("[a-zA-Z][a-zA-Z]")
    str1 = [str1[0 + i:2 + i] for i in range(len(str1) - 1)]
    str1_list = list(filter(lambda s: p.match(s), str1))
    str1_list_len = len(str1_list)
    str1_set = {s.lower() for s in str1_list}
    print(str1_set)
    str1_data_len = str1_list_len - len(str1_set)

    str2 = [str2[0 + i:2 + i] for i in range(len(str2) - 1)]
    str2_list = list(filter(lambda s: p.match(s), str2))
    str2_list_len = len(str2_list)
    str2_set = {s.lower() for s in str2_list}
    str2_data_len = str2_list_len - len(str2_set)
    sum_set = str1_set | str2_set
    intersection = str1_set & str2_set
    if len(sum_set) == 0:
        return 1 * 65536

    return int((len(intersection) + str1_data_len) / (len(sum_set) + str2_data_len) * 65536)


str1 = ["FRANCE", "handshake", "aa1+aa2", "E=M*C^2"]
str2 = ["french", "shake hands", "AAAA12", "e=m*c^2"]
answer = [16384, 65536, 43690, 65536]

for i in range(len(answer)):
    result = solution(str1[i], str2[i])
    if answer[i] == result:
        print(i, "true")
    else:
        print(i, "false : expect :", answer[i], " : but :", result)
