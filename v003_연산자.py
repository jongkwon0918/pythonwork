#멤버쉽 연산자
# SequenceType, MappingType에 특정한 값이 있는지 확인해주는 연산자
# in, not in
str_temp="apple"
print(f"str_temp에 p가 있니? : {'p' in str_temp}")
print(f"str_temp에 p가 없니? : {'p' not in str_temp}")

list_temp=["홍길동", "이순신", "고길동", "세종대왕"]
print(f"list_temp에 홍길동이 있니? : {'홍길동' in list_temp}")
print(f"list_temp에 유병승이 없니? : {'유병승' not in list_temp}")

tuple_temp=(1,2,3,4,5)
print(f"tuple_temp에 3이 있니? : {3 in tuple_temp}")
print(f"tuple_temp에 '3'이 있니? : {'3' in tuple_temp}")

dict_temp={"gender":"남", "email":"admin@admin.com"}
# key를 기준으로 검색을 함
print(f"dict_temp에 gender가 있니? : {'gender' in dict_temp}")
print(f"dict_temp에 '남'이 있니? : {'남' in dict_temp}")
# value를 기준으로 검색하기
# values()함수 사용하기
print(f"dict_temp에 '남'이 value에 있니? : {'남' in dict_temp.values()}")

#아이덴티티 연산자
#값이 아닌 주소로 비교연산하는 것
# == 동등성비교 -> 값 / is 동일성 -> 주소
print(str_temp == "apple")
# print("정수 입력 :", end=" ")
# input_data=input()
# print(str_temp is not input_data)

def test_su():
    return int('10')
su=test_su()
su1=test_su()
print(su == su1)
print(su is su1)

#None값을 비교할 때 사용 -> 안정적으로 사용
test_temp=None
print(test_temp == None)
print(test_temp is None)

#삼항연산자
age=20
result = "성인" if age>19 else "미성년"
print(result)

# 비트연산자
bnum=0b1010
bnum2=0b1100
print(f"{bnum:032b} 일반출력")
print(f"{bnum2:032b} 일반출력")
print(f"{bnum>>1:032b} >> 1 쉬프트연산(오른쪽으로 이동 / 2^n) ")
print(f"{bnum<<1:032b} << 1 쉬프트연산(왼쪽으로 이동 * 2^n) ")
print(f"{bnum & bnum2:032b} & 연산(AND) ")
print(f"{bnum | bnum2:032b} | 연산(OR) ")
print(f"{bnum ^ bnum2:032b} ^ 연산(XOR) ")
print(f"{~bnum:032b} ~ 연산(NOT)") 

#비트마스킹
# 특정값에서 지정한 자리수에 값이 있는지 확인

#권한 확인
bit=0b1010
bit2=0b0011
mask=0b1000
print(f"{bit:032b} {bit&mask > 0}")
print(f"{bit2:032b} {bit2&mask > 0}")

READ=0b100
WRITE=0b010
EXEC=0b001
user_auth=READ|WRITE
print(user_auth & READ > 0) #읽기 권한확인
print(user_auth & EXEC > 0) #실행 권한확인
print(user_auth & WRITE > 0) #쓰기 권한확인

#3.8이상 버전에서 사용할 수 있는 연산자
#위루스연산자(코끼리) 연산자 :=
#조건문 변수에 값을 저장하고 그 결과로 조건문을 처리할 수 있게 해주는 연산자
# 예) (변수:=대입될 값) 비교연산자
result="길이가 길다" if (length := len("안녕하세요")) > 5 else "길이가 짧다"
print(result)
print(length)   

print("나이 : ",end="")
result="성인" if(age:=int(input()))>19 else "미성년"
print(result)
print(age)