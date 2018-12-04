import bisect
# index메서드는 리스트 길이에 비혜한 선형 시간
x = list(range(10**6))
i = x.index(991234)
# bisect 는 바이너리 검색
i = bisect.bisect_left(x, 991234)

