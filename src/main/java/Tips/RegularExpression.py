# []  문자 클래스
# \d  숫자
# \D  숫자 아닌것, [^0-9]
# \s  whiteSpace문자와 매치,  [ \t\n\r\f\v]
# \w  문자+숫자와 매치, [a-zA-Z0-9]
# .   \n을 제외한 모든 문자
# *   반복, 바로 앞에 있는 문자 0 ~ 무한까지 반복
# +   반복, 최소 1부
# ?   있어도 되고 없어도 되고
# {n1, n2}  반복, n1 ~ n2, n1 생략은 0, n2 생략은 무한

import re


# match()	문자열의 처음부터 정규식과 매치되는지 조사한다.  없을경우 None
# search()	문자열 전체를 검색하여 정규식과 매치되는지 조사한다.   없을경우 None
# findall()	정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다
# finditer()	정규식과 매치되는 모든 문자열(substring)을 iterator 객체로 리턴한다

input_str = "ab, abb, abd ab b,aab b"
p = re.compile('ab b')
print(p.match(input_str))
# None
print(p.search(input_str).group())
# ab b
print(re.search('ab b', input_str).group())  # 축약형
# ab b

# group()	매치된 문자열을 리턴한다.
#           group(0)	매치된 전체 문자열
#           group(1)	첫 번째 그룹에 해당되는 문자열
# start()	매치된 문자열의 시작 위치를 리턴한다.
# end()	    매치된 문자열의 끝 위치를 리턴한다.
# span()	매치된 문자열의 (시작, 끝) 에 해당되는 튜플을 리턴한다.

# 컴파일 옵션
# p = re.compile('a.b', re.DOTALL)   or   p = re.compile('a.b', re.D)
# DOTALL(S) - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
# IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
# MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
# VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)

# 메타문자
# ^ 처음 시작,  # ^python인 경우 문자열의 처음은 항상 python으로 시작
# $ 마지막,  # python$이라면 문자열의 마지막은 항상 python
# | 는 or
# \A는 문자열의 처음
# \Z는 문자열의 끝과 매치됨
# \b는 단어 구분자(Word boundary)
# \B 메타문자는 \b 메타문자의 반대의 경우이다. 즉, whitespace로 구분된 단어가 아닌 경우

# () 그룹핑, (ABC)+ 는 ABCABC와 매치 됨
# p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
# m = p.search("park 010-1234-1234")
# print(m.group(1))
# park
# print(m.group(2))
# 010-1234-1234

# \1  그룹 재참조


# \는 \\로 쓰거나 r'\'로 써야 됨
# 아니면 \section 이  [ \t\n\r\f\v]ection 로 변환 됨

# -------------------
# 문자열 변경 sub(바꿀 문자열, 원본 소스, 바꿀 횟수 없으면 모두)
p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes', count=1)
# 'colour socks and red shoes'

# p = re.compile('(blue|white|red)')
# p.subn( 'colour', 'blue socks and red shoes')
# ('colour socks and colour shoes', 2)


# -----------------
# 탐욕 제어
# >>> s = '<html><head><title>Title</title>'
# >>> len(s)
# 32
# >>> print(re.match('<.*>', s).span())
# (0, 32)
# >>> print(re.match('<.*>', s).group())
# <html><head><title>Title</title>

# ? 사용시
# >>> print(re.match('<.*?>', s).group())
# <html>