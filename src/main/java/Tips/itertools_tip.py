

#모든 순열 구하
import itertools

def solution(n, k):
    answer = []
    mylist = [*range(1,n+1)]
    mypermuatation =  itertools.permutations(mylist)
    # mypermuatation =  itertools.permutations(range(1,n+1))
    return list(list(mypermuatation)[k-1])


#조합
from itertools import combinations
list(combinations('1234', 2))