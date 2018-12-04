import datetime
from datetime import time



# 시간 -> 문자열
dt = datetime.datetime.now()
s = dt.strftime("%A %d. %B %Y")
print(s)
# Thursday 13. September 2018
# %Y	앞의 빈자리를 0으로 채우는 4자리 연도 숫자
# %m	앞의 빈자리를 0으로 채우는 2자리 월 숫자
# %d	앞의 빈자리를 0으로 채우는 2자리 일 숫자

# %H	앞의 빈자리를 0으로 채우는 24시간 형식 2자리 시간 숫자
# %M	앞의 빈자리를 0으로 채우는 2자리 분 숫자
# %S	앞의 빈자리를 0으로 채우는 2자리 초 숫자

# %A	영어로 된 요일 문자열
# %B	영어로 된 월 문자열

#문자열 -> 시간
datetime.datetime.strptime("2017-01-02 14:44", "%Y-%m-%d %H:%M")


datetime.timedelta
# days: 일수
# seconds: 초 (0 ~ 86399)
# microseconds: 마이크로초 (0 and 999999)
# total_seconds(): 모든 속성을 초단위로 모아서 변환

print(time(9,0))

t= datetime.time(0,20)
d = datetime.timedelta(0,30)
