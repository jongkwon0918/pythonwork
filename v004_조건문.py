# 파이썬에서 조건문을 사용할때 {}를 사용하지 않는다
# : 과 들여쓰기를 기준으로 조건문의 영역을 구분함

# if조건문
# if 조건문 : 
#   실행할 구문 작성

# print("수입력 : ",end="")
# su=int(input())

# if su>10 : 
#     print(f"{su}는 10보다 크다")

# if su<10 : print(f"{su}는 10보다 작다")

# 조건에 따라 할인율 적용하기
# coopon='W1234'
# product_price=100000

# if coopon=='W1234' : 
#     discount=0.2 # 블록범위가 없음

# print(f"쿠폰을 사용한 가격은 {product_price*(1-discount)}원 입니다")


# # 문자열에 특정 문자가 있는지 확인하기
# str_names="유병승,오수환,하승우,전재우,김태련,신동호"
# if (t:=input()) in str_names :
#     print(f"{t}는 str_names에 있습니다")

# # if ~ else문 이용하기
# height=float(input("당신의 키는"))
# if height>180 : 
#     print("괜찮네요!")
# else :
#     print("아쉽네요")

# if (d:=int(input("수입력 : "))) % 2==0 : 
#     print(f"{d}는 짝수입니다")
# else : 
#     print(f"{d}는 홀수입니다")

# if ~ elif ~ else 구문이용하기
# 성적 등급출력하기
# jumsu=int(input("점수입력 : "))
# if jumsu<=100 and jumsu>=90 : 
#     grade="A"
# elif jumsu<90 and jumsu>=80 : 
#     grade="B"
# elif jumsu<80 and jumsu>=70 : 
#     grade="C"
# elif jumsu<70 and jumsu>=60 : 
#     grade="D"
# else : grade="F"

# print(f"{jumsu}는 등급 {grade}입니다")

# if문 내부에 다른 if문 사용하기
# if (coopon:=input("쿠폰번호 : ")) == "C1234" : 
#     if(age :=int(input("나이 : "))) > 19 : 
#         print("재밌게 노세요!")
#     else : 
#         print("성인만 사용할 수 있습니다.")
# else : 
#     print("잘못된 쿠폰번호입니다.")

# 404,403,400,200,500

# match ~ case구문이용하기
print("==== 정수형을 MATCH문에 넣기 ====")
print("1. 회원등록")
print("2. 회원수정")
print("3. 회원삭제")
print("4. 회원조회")
choice=int(input("메뉴선택 : "))

match choice : 
    case 1 : print("등록 기능 개발중....")
    case 2 : print("수정 기능 개발중....")
    case 3 : print("삭제 기능 개발중....")
    case 4 : print("조회 기능 개발중....")
    case _ : print("없는 기능입니다.")

print("==== 조건문 match문에 넣기 ====")
match choice<4 : 
    case True : print("메뉴에 있는 번호입니다.")
    case False : print("메뉴에 없는 번호 입니다.")

# 데이터 구조를 확인하는 조건문에 사용할 수 있음
# 리스트 매칭하기
list_sample=[1,2,3,4,5]
list_sample=[10,20,'삼','사']
list_sample=["문자열", 10, 180.5]
list_sample=[100, 200, 300, 'a', 'b', 'c']


match list_sample :
    case [1,2,3,4,5] : print("[1,2,3,4,5]인 값")
    #0인덱스가 10이고 길이가 4인 리스트
    case [10,x,y,z]: print(f"[10,{x},{y},{z}]인 값")
    #0인덱스가 100이고 임의의 값 2개, 최소길이가 3개인 리스트
    case [100,x,y,*other] : print(f"[100,{x},{y},{other}]인 값")
    case [x,y,z] : print(f"길이가 3인 리스트: [{x}, {y}, {z}]")
    case [str() as a,int() as b,float() as c] : print(f"타입 매칭: {a}, {b}, {c}")
    case _ : print("일치하는게 없음")
    

move_tuple=("",x,y)
match move_tuple : 
    case ("FORWARD",x,y) : print(f"앞으로 ({x},{y})")
    case ("BACKWARD",x,y) : print(f"뒤로 ({x},{y})")
    case ("STOP",X,Y) : print("이동 중지")
    case _ : print("없는 명령입니다.")

#딕셔너리 -> key, value
dict_sample={"code":404, "status":"error"}

match dict_sample : 
    case {"code":404, "status":x} : print(f"{dict_sample['code']}")
    case {"code":404, "status":"fall"} : print(f"{dict_sample['code']} 서버에서 에러가 발생함")
    case {"code":200, **other} : print(f"{dict_sample['code']} {other}")
    case _ : print("일치하는게 없음")

#가드 이용하기
data=[2,4,6]
match data:
    case list() as lst if len(lst) >=3 and all(x%2==0 for x in lst) : print("짝수만 있는 3개 이상의 리스트")
    case [a,b] if a+b > 10 :print(f"{a+b}는 10보다 큽니다")

    case _ : print("가드 조건에 맞지 않음")
    
#튜플
#최소 두개 이상 요소, 첫번째 요소는 음수 나머지 합(sum)은 양수인 데이터 패턴 찾기
# 길이가 3이고 모든 요소가 4같은 값인 패턴찾기
# 단일 요소의 튜플 찾기
tuple_data=[-100,200,600]
match tuple_data:
    case list() as tuplelst if len(tuplelst)>=2 and sum(tuplelst)>0 and tuplelst[0]<0 : print("최소 두개 이상 요소, 첫번째 요소는 음수 나머지 합(sum)은 양수인 데이터")
    case _ : print("튜플 조건에 맞지 않음")