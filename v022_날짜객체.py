from datetime import date
# 날짜를 가져오는 객체
today=date.today()
print(today)
end=date(2026,5,9)
print(end)

delta=end-today # 일수
print(delta)

# 문자열타입의 날짜형식으로 날짜로 변경하기
# fromisoformat -> YYYY-mm-DD T HH:MM:SS
birthday="2001-01-26"
d=date.fromisoformat(birthday)
print(d,type(d))

# 한국식 포멧으로 출력
# 원하는 포멧을 이용
# strftime(포멧지정)
print(f"반장님 생일 : {d.strftime("%Y년 %m월 %d일")}")

d=d.replace(year=d.year-100)
print(d)

from datetime import datetime

now=datetime.now()
print(now)
ts=now.isoformat()
print(ts)
str_dateime=now.strftime("%Y년 %m월 %d일 %H:%M:%S")
print(str_dateime)
s="2026-03-14 10:28"
dt=datetime.strptime(s,"%Y-%m-%d %H:%M")
print(dt)

print(dt.time())
print(dt.date())
birthday_time=datetime(2001,1,26,1,26)
delta=now-birthday_time
print(delta)
