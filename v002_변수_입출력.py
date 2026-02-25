# 변수활용하기
# 파이썬에서 변수는 자료형이 없이 선언함
# 동적자료형으로 데이터는 Object로 처리(변수 주소저장)

# 변수선언 및 대입
bool_var=True
int_var=19
float_var=180.5
str_var="유병승"
list_var=[1,2,3,4,5]
tuple_var=("가","나","다","라")
set_var={'a','b','c','d','e'}
dict_var={"name":"유병승","age":19}

# 한번에 다수의 변수를 선언하고 저장하기
test1,test2,test3="이러지마",200,["리","스","트"]

# print함수 활용하기
# 기본 리터럴 출력
print("test")
print(1234)
print(True)

# 한번에 여러값 출력하기
print("test",19,180.5)

# print함수 옵션이용하기
# sep옵션 -> 기본값 ' '
print(2026,'02',25,sep='-')

# end옵션 -> 기본값 \n
print("test", end='\t')
print("test2")

# print()함수에서 변수출력하기
print(bool_var)
print(int_var)
print(float_var)
print(str_var)
print(list_var)
print(tuple_var)
print(set_var)
print(dict_var)

# 문자열 패턴을 출력하기
# f-string 이용하기
name="박종권"
age=25
print(f"이름은 {name} 나이는 {age}")

# 문자열 정렬하기
# {변수명:<n} : 왼쪽정렬
# {변수명:>n} : 오른쪽정렬
# {변수명:^n} : 가운데정렬
# {변수명:<0n} : 공백을 0으로 표시
print(f"내 이름은 {name:<10} 나이는 {age:>3}입니다")
print(f"내 이름은 {name:>10} 나이는 {age:<3}입니다")
print(f"내 이름은 {name:>10} 나이는 {age:>03}입니다")
print(f"내 이름은 {name:^10} 나이는 {age:^3}입니다")
print(f"내 이름은 {name} 나이는 {age} 키는 {174.12165464:.2f}입니다")

#format함수 이용하기
print("이름 : {} 나이 : {}".format(name, age))
print("이름 : {0} 나이 : {1} 키 : {2:.2f}".format(name, age, 180.5))
print("이름 : {n} 나이 : {a}".format(n=name, a=age))
print("이름 : {0} 나이 : {a}".format(name, a=age))

# %패턴
print("이름 : %s, 나이 : %d, 키 : %.2f" % (name, age, 180.5))

# 변수의 타입을 확인하기
# type()함수를 이용
print(type(str_var))
print(type(list_var))
print(type(tuple_var))
print(type(set_var))
print(type(dict_var))

type_test=type(str_var)
# dir() 함수는 해당 객체(여기서는 str 클래스)가 가진 모든 속성과 메서드를 리스트로 반환합니다.
print(dir(type_test))
# __name__ 속성은 클래스의 이름을 문자열로 반환합니다.
print(type_test.__name__)

#모든값은 객체로 처리
print(int_var)
print(id(int_var))

# 호이스팅이 가능한가?
# print(a)
# a="가능?"
# 결론 : 불가능

# 문자열 합치기 => + 연산자
# temp="나이는"+19+"살"

# 출력을 다른곳으로 하고
# print() -> console에 출력
with open('output.txt', 'w',encoding='utf-8') as f :
    print(f"내이름은 {name} 나이는 {age}입니다", file=f)

# 형 변환하기
# 문자열을 정수형으로 변경하기
# int()함수 이용해서 변경
str_var="10"
test=int(str_var)
print(f"값 :{test} / 타입 : {type(test)}") 

# test=float(str_var)
print(f"값 :{test} / 타입 : {type(test)}") 

# 실수형을 문자열로 변경
# str()함수 이용해서 변경
test=str(float_var)
print(f"값 :{test} / 타입 : {type(test)}")

#문자열을 실수형으로 변경
# float()함수 이용
str_float = "180.5"
test = float(str_float)
# test=int(str_float) -> float형이라서 오류남
print(f"값 : {test} / 타입 : {type(test)}")

#리스트 타입을 문자열로 변경하기
# str()함수를 이용
test=str(list_var)
print(f"값 : {test} / 타입 : {type(test)}") 

#튜플타입을 문자열로 변경
test=str(tuple_var)
print(f"값 : {test} / 타입 : {type(test)}") 

#딕셔너리 타입을 문자열로 변경
test=str(dict_var)
print(f"값 : {test} / 타입 : {type(test)}")

#진위형으로 변경하기
# bool()함수를 이용

#숫자데이터를 진위형으로 변경
num_test=1
bool_var=bool(num_test)
print(f"값 : {bool_var} / 타입 : {type(bool_var)}")

num_test=0
bool_var=bool(num_test)
print(f"값 : {bool_var} / 타입 : {type(bool_var)}")

num_test=int(bool_var)
print(f"값 : {num_test} / 타입 : {type(num_test)}")

#실수값 진위형
bool_var=bool(float_var)
print(f"값 : {bool_var} / 타입 : {type(bool_var)}")

bool_var=bool(0.0)
print(f"값 : {bool_var} / 타입 : {type(bool_var)}")

#문자열 진위형 -> 값이 있으면 True / 공란이면("") False
bool_var=bool(str_var)
print(f"값 : {bool_var} / 타입 : {type(bool_var)}")

bool_var=bool("")
print(f"값 : {bool_var} / 타입 : {type(bool_var)}")

# 시퀀스, set, dict
# bool로 변환하기 -> 값이 있으면 True / 값이 없으면 False
print(bool(list_var))
print(bool(set_var))
print(bool(tuple_var))
print(bool(dict_var))
print(bool([]))
print(bool({}))
print(bool(()))

#사용자가 입력하는 값 가져오기
# input()함수를 이용
print("문자열 입력 :", end=" ")
str_var=input()
print(str_var,type(str_var))

print("나이를 입력 :", end=" ")
num_var=int(input())
print(num_var+10,type(num_var))
bool_var=True
while(bool_var) :
    try :
        print("정수 입력 :", end=" ")
        input_data=int(input())
        bool_var=False
        print(f"input_data : {input_data}")
    except ValueError : 
        print("잘못입력했습니다. 다시 입력하세요")