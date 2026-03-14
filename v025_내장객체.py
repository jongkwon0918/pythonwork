# 정규표현식
import re
text="홍길동 이메일은 test@example.com이고, 예비 메일은 demo@test.com입니다"

# 이메일패턴
# r"정규표현식작성"
email_pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
# 문장에서 이메일 찾기
emails=re.findall(email_pattern,text)
print(emails)

# 첫번째 이메일만 찾기
result=re.search(email_pattern,text)
print(result)
if result : 
    print(result.group())

# 마스킹처리하기
# 이메일은 다른값으로 대체하기
result=re.sub(email_pattern,"******",text)
print(result)

import random
lunch=["닭쌈밥","닭칼국수","짜장면","컵라면","토스트"]

today_lunch=random.choice(lunch)
print(today_lunch)
today_lunch=random.choices(lunch) # 중복값이 나옴
print(today_lunch)
today_lunch=random.sample(lunch,2)
print(today_lunch)

print(random.randint(1,10))

random.seed(42)

