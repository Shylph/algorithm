# 절대값
abs(-1)

# 모두 참이면 True
all([1, 2, 3])
# True
all([1, 2, 3, 0])
# False

# 하나라도 참이면 True
any([1, 2, 3, 0])
# True

# 아스키 변환
chr(97)
# 'a'
ord('a')
# 97

# 몫과 나머지 튜플 반
divmod(7, 3)
# (2, 1)

# enumerate 열거, index 붙여줌
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# 0 body
# 1 foo
# 2 bar

# 실행 가능한 문자열 실행
eval('1+2')
# 3
eval('divmod(4, 3)')
# (1, 1)

# 진수 변환
bin(3)  # 2진수
# '0b10'
format(3, 'b')  # or   f'{3:#b}'  or  f'{3:b}'
# '10'
oct(34)  # 8진수
# '0o42'
hex(234)  # 16진
# '0xea'
int('11', 2)
# 3

# 반올림
round(4.6)
# 5

# 대소문자
"hi".upper()
"HI".lower()
