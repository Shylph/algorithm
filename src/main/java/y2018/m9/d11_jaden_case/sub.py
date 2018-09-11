import re


def solution(s):
    answer = s.lower()
    p = re.compile("[\s][a-z]")
    answer = p.sub(lambda m: m.group().upper(), answer)
    answer = answer[:1].upper() + answer[1:]
    return answer
