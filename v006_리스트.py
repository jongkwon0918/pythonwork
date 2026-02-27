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
# 문자열 대입하기
list_temp[len(list_temp)-1]="안녕하세요"
print(list_temp)

# 특정 범위를 삭제하기
print(f"이전값 {list_temp}")
list_temp[0:4]=[]
print(f"이후값 {list_temp}")

# 시작, 끝이 동일하면 삽입으로 처리
print(f"전체값 list_int {list_int}")
list_int[2:2]=range(5)
print(f"전체값 list_int {list_int}")

# 범위를 벗어나서 지정 -> 자동으로 추가
list_empty=[]
print(f"list_empty : {list_empty}")
list_empty[0:2]=[1,2,3,4]
print(f"list_empty : {list_empty}")
print(list_empty[2])

# 반복문을 이용해서 데이터 순회하기
# 방법 : for 변수명 in sqeunceType : 로직

for a in list_int : 
    print(f"a = {a}")

# 인덱싱을 이용하기
for i in range(len(list_int)) : 
    print(f"{i} : {list_int[i]}")

# 인덱스, 값을 한번에 반복문에서 활용하기
for i,v in enumerate(list_int) : 
    print(f"{i} : {v}")
# 옵션 : start=시작인덱스 지정
print("===== start인덱스 =====")
for i,v in enumerate(list_int,start=5) : 
    print(f"{i} : {v}")

# 리스트의 길이확인하기
print(len(list_int))

# 리스트 연산하기 -> 연산자 제공
print("==== +연산자 ====")
list_op_a=[1,2,3,4]
list_op_b=["유병승","홍길동","이순신"]
list_op_result=list_op_a + list_op_b
print(list_op_result)
print(list_op_a)
print(list_op_b)

#곱하기 연산
list_op_result=list_op_a*3
print(f"list_op_a*3 : {list_op_result}")

list_op_result=list_op_b*3
print(f"list_op_b*3 : {list_op_result}")

# list_op_result=list_op_a*list_op_b 이거는 안됌

#리스트 대소 비교하기
print("==== 리스트 대소 비교 ====")
list_str_com=["a","b","c"]
list_str_com2=["z","a","b"]
print(f"com<com2 : {list_str_com<list_str_com2}")

list_tuple_com=[(1,2,3),(4,5,6)]
list_tuple_com2=[(4,3,2),(1,2,3)]
print(f"com<com2 : {list_tuple_com<list_tuple_com2}")

#list에 저장된 값 확인하기
#in, not in
result=3 in list_op_a
print(f"result : {result}")

if 3 in list_op_a : 
    print("3이 있다")

#list_op_b에 김영호가 없으면 추가하기
if "김영호" not in list_op_b :
    list_op_b[len(list_op_b):]=["김영호"]
print(list_op_b)

#내장함수 이용하기 -> built-in함수
#sorted함수
#데이터를 정렬하는 함수
#매개변수 iterable, key, reverse이용
print("==== sorted함수 이용하기====")
list_order=sorted(list_int)
print(f"list_order : {list_order}")
#내림차순 정렬
list_order=sorted(list_int,reverse=True)
print(f"list_order(내림차순) : {list_order}")

#key파라미터 : 정렬기준
list_str=["하나","코리아","비","대한민국","우리나라만세","두리두리두둥실덩기덩기더덩실"]
list_str=sorted(list_str,key=len, reverse=True)
print(list_str)

# enumerate함수
tuple_result=enumerate(list_str)
print(f"타입 {type(tuple_result)} \n 값 {tuple_result}")

# for i,v in tuple_result : 
#     print(f"{i} : {v}")

print(next(tuple_result))

# max/min함수
print("=== 숫자형 list ====")
print(f"list_int max = {max(list_int)}")
print(f"list_int min = {min(list_int)}")
print("=== 문자형 list ====")
print(f"list_str max = {max(list_str)}")
print(f"list_str min = {min(list_str)}")

# sum() : 합계
print(f"list_int 합계 : {sum(list_int)}")


#메소드 활용하기
# 메소드 이용해서 데이터를 조작하기
#append(): 추가
list_test=[]
list_test.append("박종권")
list_test.append("홍길동")
print(f"list_test : {list_test}")
# list_test.append("김영호","유병승") 이거는 안됌

#랜덤데이터 추가하기
#random 모듈
import random
list_test=[]
for i in range(1, 20, 1) : 
    list_test.append(random.randint(1,10))
print(f"random : {list_test}")

#pop() -> 맨 뒤의 값을 삭제/반환
result=list_test.pop()
print(f"pop(삭제값) : {result} / 원본 {list_test}")
#매개변수 index번호 -> 해당 인덱스의 값을 잘라냄
result=list_test.pop(3)
print(f"pop(삭제값) : {result} / 원본 {list_test}")

#sort() / reverse()
list_test.sort()
print(f"list_test. sort : {list_test}")
list_test.reverse()
print(f"list_test. reverse : {list_test}")

# 값의 인덱스번호 가져오기
# index()
search_index=list_test.index(5)
print(f"결과 : {search_index}")
# 값이 없으면 에러가 발생함. -> -1이 아님
# search_index=list_test.index(20)
# print(f"결과 : {search_index}")
# if list_test.index(20)!=-1 : 
# if(list.indexOf(20)!=-1)

# insert(index,value) 중간에 값을 삽입하는 함수
list_test.insert(3,100)
print(list_test)

# remove() 삭제하는 함수
list_test.remove(5)
print(list_test)

#extend() 결합하는 함수
list_test.extend([100,200,300,400])
print(list_test)
# result=list_test+[100,200,300,400]
# print(result)

#count() : 값의 갯수를 찾아주는 함수
result=list_test.count(3)
print(f"3의 중복 갯수 : {result} 개")

#copy() : 리스트 복사본 만들기
copy_list=list_test.copy()
print(f"copy_list : {copy_list}")

copy_list[0]=100000
print(f"copy_list(사본) : {copy_list}")
print(f"list_test(원본) : {list_test}")

#clear() : 전체삭제
copy_list.clear()
print(f"copy_list(clear) : {copy_list}")

# 리스트삭제 : 
copy_list=None
# print(copy_list[0])

# 원하는 위치의 값을 삭제하는 방법
# del(list[인덱스번호])
print(list_test)
del(list_test[0])
print(list_test)

#리스트 언패킹
#리스트에 있는 요소를 각 변수 저장해주는 기능
#조건: 리스트에 저장된 요소수와 변수의 수가 동일해야함.
#변수명 : 그외 요소를 리스트로 받음
list_unpacking=[1,2,3,4,5]
a,b,c,d,e=list_unpacking
print(f"{a},{b},{c},{d},{e}")
# a,b,c=list_unpacking 숫자를 맞추지 않으면 에러가 발생함
a,b,c,*d=list_unpacking
print(f"{a},{b},{c},{d}")

#for문에서 언패킹 이용하기 -> 2차원 방식의 데이터를 활용할때
#for i,v in enumerate(list_unpacking) :
list_unpacking=[[1,2,3],[4,5,6],[7,8,9]]
for col1, col2, col3 in list_unpacking : 
    print(f"{col1} {col2} {col3}")

#이차원 리스트 이용하기
list_matrix=[[1,2,3,4],["박종권","유병승","김태우","김민규"],[180.5,175.5,168.1,184.2]]

#인덱스로 접근하기 변수면[행][열]
print(list_matrix[0])
print(list_matrix[1][2])
print(list_matrix[2][3])

#슬라이싱으로 접근하기
# [:]
print(list_matrix[1][1:3])
print(list_matrix[2][:2])

#행 가져오기
print(list_matrix[0:2])

#인덱스로 데이터 저장하기
list_matrix[0][1]=200
list_matrix[1][3]="짱구"
print(list_matrix)
list_matrix[1]=list("abcde")
print(list_matrix)
#인덱스를 초과해서 저장
list_matrix[len(list_matrix):len(list_matrix)]=list("일이삼사")
print(list_matrix)

for row in list_matrix : 
    for col in row : 
        print(col,end=" ")
    print()

#특정 지역의 좌표를 가져와 출력하기
list_coords=[[32.2,123.12],[37.5, 126.97], [35, 129],[35.87, 128.60]]

for x,y in list_coords : 
    print(f"x좌표 : {x}, y좌표 : {y}")

# 컴프리핸션
list_data=[11,23,30,45,50]
# list_result=[]
# for i in list_data : 
#     list_result.append(i**2)
# print(list_result)
list_result=[x**2 for x in list_data]
print(list_result)

# 짝수인 값만 거듭제곱해서 새로운 리스트만들기
list_result=[x**2 for x in list_data if x%2==0]
print(list_result)
import random
# 랜덤 원하는 수만큼 배열만들기
list_result=[random.randint(1,10) for _ in range(5)]
print(list_result)

list_data=["유병승","이순신","홍길동","피카츄","김유신"]
# 성만 빼서 리스트 만들기
list_result=[n[0] for n in list_data]
print(list_result)
# 이름만 빼서 리스트 만들기
list_result=[n[1:] for n in list_data]
print(list_result)



