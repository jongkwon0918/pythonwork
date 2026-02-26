list_int=[1,2,3,4,5]
list_float=[180.3,145.2,172.2,167.3,188.3,176.3]
list_str=["유병승","오수환","하승우","전재우","김태련","신동호"]
list_mixed=[10,"유병승",[183.2,180.5]]

list_int=list(range(1,6))
list_obj=list("하나둘셋")
print(list_obj)
print(list_int)

# 생성된 리스트 인덱스로 접근하기
print(f"list_int[0] : {list_int[0]} {type(list_int[0])}")
print(f"list_float[0] : {list_float[0]} {type(list_float[0])}")

# 인덱스로 값 수정하기
list_int[0]=100
list_str[2]="김태리"
print(list_int)
print(list_str)

# 기본 슬라이싱 이용하기
# 인덱스 범위를 지정해서 값을 가져오거나 저장하는것
# 리스트명[[시작인덱스]:[끝인덱스]] 시작인덱스 끝 인덱스는 생략이 가능함
# 시작인덱스는 포함, 끝인덱스는 불포함
print(list_int[2:4]) # 2~3번 인덱스 값

print(list_int[3:]) # 3번 인덱스 부터
print(list_int[:2]) # 0~1번 인덱스 값
print(list_int[:])

# 인덱스번호에 음수를 넣으면? 가능
print(list_int[-1]) # 맨마지막 인덱스지정 len()-1
print(list_int[-2])
print(list_int[-1*(len(list_int))])

# 슬라이싱으로 음수이용하기
print(list_int[-3:-1])

# 슬라이싱을 이용해서 값 대입하기
print(list_str)
list_str[1:3]=['이경민','박종권','김태우','김민규']
print(list_str)
list_str[4:]=['a','b','c']
print(list_str)
list_temp=[]
list_temp[4:]=['a','b','c']
print(list_temp)
list_temp[len(list_temp):]=range(1,11)
print(list_temp)
#문자열 대입하기
list_temp[len(list_temp):]="안녕하세요"
print(list_temp)


