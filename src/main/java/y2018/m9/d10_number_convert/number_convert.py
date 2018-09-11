def solution(n):
    result = []
    while n > 0:
        result.insert(0,n%3 if n%3 != 0 else 4)
        if n%3 != 0:
            n = int(n/3)
        else:
            n = int(n/3) -1
    return "".join(map(str,result))


# 10진법	124 나라	10진법	124 나라
#  1 	      1	         6  	14
#  2 	      2	         7  	21
#  3 	      4	         8  	22
#  4 	      11	     9  	24
#  5 	      12	    10  	41