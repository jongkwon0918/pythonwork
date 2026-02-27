str_data="안녕하세요 제 이름은 박종권입니다."

#각 값을 인덱스로 접근할 수 있음
#"test".chatAt(index번호)
#[]
str_result=str_data[1]
print(str_result)
str_result=str_data[-1]
print(str_result)

#슬라이싱 접근하기 -> substring()
str_result=str_data[0:5]
print(str_result)
str_result=str_data[-7:-4]
print(str_result)

#반복문이용하기
for s in str_data : 
    print(s,end=" ")
print()

#문자열 데이터를 다루는 메소드
#공백을 제거하는 메소드 -> strip()
str_data="     공백이 있는 문자열"
str_result=str_data.strip()
print(str_result)

#특정 문자를 제거하기
str_data="aaaaaa특정문구aaaaaa"
str_result=str_data.strip("a")
print(str_result)
str_data="abcsdsghlsdligealgda여기 문구 지우기sgohsdgjpaofoag"
str_result=str_data.strip('abcdefghijklnmopqrstuvwxyz')
print(str_result)

# 대소문자 변경하는 메소드 upper(), lower()
str_data="Hello Python How Are You"
str_result=str_data.upper()
print(str_result)
str_result=str_data.lower()
print(str_result)

# 문자열을 리스트로 변경하기
# 특정문자를 기준으로 변경 -> split()
str_list=str_data.split() # 기본 띄어쓰기를 기준으로 분할함.
# str_list=str_data.split("")
print(str_list)

str_csv="자바,오라클,html/css,javascript,servlet/jsp,spring,sprinboot,springsecurity,react.js"
str_result=str_csv.split(",")
print(str_result)

# 리스트를 문자열로 변경 -> join()
temp_list=["일","이","삼","사"]
str_result="".join(temp_list)
print(str_result)
str_result="->".join(temp_list)
print(str_result)

# 문자열에서 특정 문자찾기 -> find() ->인덱스번호를 반환
result=str_data.find("How")
print(result)
# index()함수와 동일
result=str_data.index("How")
print(result)

# 앞, 뒤 문자열 찾기
# startswith(), endswith()
str_data="http://google.com"
result=str_data.startswith("http")
print(result)
result=str_data.endswith("com")

#숫자로 변환이 가능한지, 알파벳인지
# isdigit() / isalpha()

#대문자만 문자열로 저장
str_data="AdaKLGKhjHJgbyGHGBksdfmlsJ"
str_result="".join([x for x in str_data if 'A'<=x<='Z'])
print(str_result)

#컴프리핸션
str_data="sgidjisgin25qeoi52ngw352pmngs234mg"
#문자열에서 숫자만 저장하기
str_result="".join([x for x in str_data if x.isdigit()])
print(str_result)