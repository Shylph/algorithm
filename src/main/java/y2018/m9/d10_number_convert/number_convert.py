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


def convert_base2(n, base):
    table = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    result = []
    if n == 0:
        return "0"
    while n > 0:
        v = table[n%base]
        result.insert(0,v)
        n = n//base
    return "".join(map(str,result))



def convert_base(value, base):
    if(base == 2):
        return list(str(format(value, 'b') ))
    elif(base == 8):
        return list(str(format(value, 'O') ))
    elif(base == 10):
        return list(str(value))
    elif(base == 16):
        return list(str(format(value, 'X') ))
    else:
        return list(convert_base2(value,base))
