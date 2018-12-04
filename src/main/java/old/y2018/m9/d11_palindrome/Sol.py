def palindrome_rec(s):
    if len(s) == 1 or len(s) ==0:
        return True
    elif s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False


def palindrome(s):
    le = len(s)
    for i in range(le//2):
        if s[i] != s[le - i -1]:
            return False
    return True


def solution(s):
    max = 1
    for i in range(len(s),0,-1):
        for j in range(len(s) - i):
            p = s[j:i+j + 1]
            if palindrome(p):
                if max < len(p):
                    max = len(p)
                    break
        if max != 1:
            break
    return max