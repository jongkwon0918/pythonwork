#함수 선언하기
#def 함수면(매개변수) :
#   실핼할 로직
#   [return 값]

#기본 함수 선언하기
def basic_func() :
    """
    docstring : 선언한 함수에 대한 설명을 작성
    어떤 기능을 하는지 설명
    parameters : 
        name str : 제품명
        prince number : 가격
    return : 
        str 제품명과 가격을 json방식으로 출력
    """
    print("내가 선언한 함수")

#함수 실행 -> 호출
basic_func()
#docstring 확인하기
help(basic_func)

#매개변수 있는 함수 선언하기
def parameter_test(val) :
    """
    인수를 전달받아 처리하는 함수
    """
    print(f"전달받은 매개변수 : {val} type : {type(val)}")

parameter_test(10)
parameter_test("안녕")

#매개변수에 전달하지 않기 -> 불가능함
#parameter_test()
#parameter_test(1,2,3,4)

#반환값이 있는 함수 선언하기
def return_test() :
    return 10*10
result=return_test()
print(result)
print(return_test())

def plus_number(su1,su2) :
    if isinstance(su1,int) and isinstance(su2,int) :
        result=su1+su2
        return result
    raise TypeError("에러에러")

result=plus_number(10,20)
print(result)
# print(plus_number("십","이십"))

#매개변수에 기본값 설정하기
def default_param_test(name="아무개") : 
    """
    매개변수에 default값을 설정하면 그 인수는 선택 파라미터가 됨
    """
    print(f"당신의 이름은 {name}")
default_param_test("박종권")
#default를 선언하지 않은 매개변수는 필수값이 됨
default_param_test()

def default_param_test2(name, age=19) :
    print(f"당신의 이름은 {name} 나이는  {age}")

#default_param_test2()
default_param_test2("김영호")
default_param_test2("김영호", 25)

# 선언시 필수 인수는 앞에 선언을 하고 선택은 뒤에 선언해야함.
# def default_param_test3(name="아무개", age) : 
#     pass

# 매개변수, 리턴값에 대한 힌트 설정 -> 파이썬 3.5이상에서 사용
# typing모듈에서 제공하는 타입을 이용 ->3.8이하 버전, 
# 3.9이상에서는 자동으로 적용이 가능함
# int, str, bool, List, Dict, Tuple, Set, Any

# 전달받은 데이터를 json방식으로 반환
def param_hint(product_name:str, product_price:int) -> str: 
    return "{"+f"상품명:{product_name},가격:{product_price}"+"}";
    # return product_price
result=param_hint("컴퓨터",200)
print(result)
result=param_hint(200,"컴퓨터")
print(result)

# 다수타입을 힌트로 사용하기
# Union / Optional
# Union : 설정한 타입 중 하나 -> 타입을 리스트로 설정
# Optional : 지정된 타입이거나 None
from typing import Union,Optional

def param_test_multi(data : Union[list,tuple]) -> Optional[dict[str,int]] :
    # return "sadf"
    print("테스트")
    # return {10:"안녕"}
    return {"안녕":10}

# param_test_multi("문자열")
param_test_multi([1,2,3,4])
param_test_multi((1,))
param_test_multi({1,2,3,4})

#가변인자 선언하기
#함수 기능 구현에 필요한 인수의 갯수가 정해져 있지 않을때 사용할 수 있는 선언법
#*args -> 전달된 인수를 리스트로 받음
def multi_args(*args) :
    for v in args :
        print(f"전달받은 데이터 : {v}")

multi_args(1,2,3,4,5)
multi_args("하나","둘","셋")

#로그, 이벤트 메시지를 출력, 불특정 다수의 값을 합쳐주는 기능 구현

#파일 시스템에서 기본경로에 인수로 받은 경로를 연결해주는 기능
# /var/www/a, /var/www/b/c/e
import os
def make_path(base_path:str,*paths) -> str :
    print(f"paths : {paths}")
    return os.path.join(base_path,*paths)
config_path=make_path("/home","ubuntu","config","setting.ini")
print(config_path)

# 사용자가 전달한 문자열데이터를 csv로 반환해주는 기능 구현하기
def make_csv(*data) : 
    str_data=map(str,data)
    print(str_data)
    return ",".join(str_data)
    # return ",".join([str(n) for n in data])
result=make_csv("유병승","19","경기도시흥시")
print(result)
result=make_csv("유병승",19,"경기도시흥시")
print(result)

# 데이터 분석용 평균을 계산해주는 함수만들기
score_data={"1반":(80,90,50,40,60),"2반":(70,80,60,30,90),"3반":(100,90,50,10,20),"4반":(10,50,60,70,40,66,100)}

def label_avg(label, *scores) : 
    if scores : 
        avg=sum(scores)/len(scores)
        return f"{label}의 평균 {avg:.2f}"
    else :
        return "계산할 값이 없습니다."
    
for k,v in score_data.items() : 
    print(label_avg(k,*v))

#키워드 가변인자 사용하기
# **kwargs -> 인수의 갯수와 이름을 무작위로 사용할 때 선언 가능
def basic_kwargs(**kwargs) :
    print(kwargs)

basic_kwargs(name="박종권", age=19,gender="남")

# 태그를 생성함수 만들기
# 태그명과 속성을 전달받아 태그 만들기
# <태그명 속성명=속성값 속성명=속성값 ....>출력할내용</태그명>
def make_tag(tag_name:str,message="",**attr) : 
    attribute=" ".join([f"{k}='{v}'" for k,v in attr.items()])
    print(attribute)
    if message!="" : 
        return f"<{tag_name} {attribute}>{message}</{tag_name}>"
    return f"<{tag_name} {attribute}/>"
p=make_tag("p","이거 되니?",id="1234")
img=make_tag("img",src="test.png",width="100px",height="100px")
print(p)
print(img)
# 데이터베이스 연결정보를 만들어주는 함수
# url과 port을 받아서 처리하는 함수
def connection_config(**option)->dict :
    connect={}
    connect["url"]=option.get("url","localhost")
    connect["port"]=option.get("port",1521)
    return connect
result=connection_config()
print(result)
result=connection_config(url="192.168.1.2")
print(result)
result=connection_config(url="192.168.1.2", port=8080)
print(result)
# 상품과 선택한 옵션을 출력해주는 함수 구현하기 
#클로저 이용하기
def outer_func(basic_path:str) :
    def inner_func(partial:str) :
        print(f"기본 경로 : {basic_path}")
        print(f"추가 경로 : {partial}")
        print(f"{basic_path}{partial}")
    return inner_func
linux_path=outer_func("/home/ubuntu")
win_path=outer_func("c\\Users\\ubuntu")
linux_path("/tomcat")
win_path("/testwork")

from typing import Callable

def generate_count(count=0)-> Callable[[],int] :
    def count_func() :
        # 지역변수가 아닌 상위 스코프에서 변수를 가져와 처리 
        nonlocal count
        count+=1
        return count
    return count_func
count1=generate_count(10)
count2=generate_count()

for _ in range(10):
    print(count1())
for _ in range(10) : 
    print(count2())

#데코레이터 이용하기
#기존에 선언한 함수를 수정하지 않고 그 함수에 새로운 기능을 덧붙이거나 감싸는 함수
#특정함수의 시작이나 끝에 추가 로직을 구성할때 사용

#데코레이터를 적용할 함수를 선언
#함수를 매개변수로 받는 함수를 선언
#def 함수명(함수) :
def decoration_test(func) : 
    def new_func() : 
        print("함수 실행전 로직")
        func()
        print("함수 실행 후 로직")
    return new_func

def target_func() : 
    print("실제 호출할 함수")

# 데코레이터 함수 직접 호출해서 이용
# new1=decoration_test(target_func)
# new1()

# 어노테이션을 이용하는 방법
# @데코레이션함수명 -> 함수선언부
@decoration_test
def target_func2() : 
    print("어노테이션으로 데코레이션 이용하기")

target_func2()

#매개변수를 선언한 데코레이션 함수 선언하기
def decoration_param_test(func) :
    def new_func(*arg,**kwargs) :
        print("매개변수 처리하기 전")
        func(*arg,**kwargs)
        print("매개변수 이용한 후")
    return new_func

@decoration_param_test
def target_func3(name) : 
    print(f"당신의 이름 : {name}")

target_func3("박종권")

#특정 함수를 실행할때 권한이 필요한 경우
USER_SESSION_ROLE= "user"

def check_authority(func) :
    def check(*arg,**kwargs) :
        if USER_SESSION_ROLE == "admin" :
            func(*arg,**kwargs)
        else :
            raise Exception("실행할 권한이 없습니다")
    return check

@check_authority
def delete_data(id) :
    print(f"{id}가 삭제 되었습니다.")

USER_SESSION_ROLE="admin"
delete_data(10)

# 람다표현식 활용하기
# 표현방식
# lambda [매개변수] : 반환값

# 익명함수
lambda1=lambda : "매개변수 없는 고정값을 반환하는 함수"
print(lambda1())

# 매개변수 있는 함수 선언하기
lambda2=lambda name : f"{name}님 환영합니다"
print(lambda2("신입생"))

#매개변수가 다수인 함수를 선언
lambda3=lambda x,y,z : x+y+z
print(lambda3(1,2,3))

#람다표현식은 주로 다른 함수의 인자로 함수를 전달할 때 사용
#특히 파이선이 제공하는 sort()/sorted(),map(),filter(),reduce()

#map() : 리스트나 튜플에 저장된 값을 변경하여 새로운 리스트를 만들때 사용하는 함수
#타입변경, 값 자체를 변경
#map(함수->def (a):return 값,반복할 리스트|튜플)
list_data=[1,2,3,4,5]
result=map(lambda e : e**2, list_data)
for v in result :
    print(v,end="")
# print()
print(tuple(result))

#map함수의 두번째 이상 매개변수는 가변으로 전달받음
price=[100,200,300,400]
stock=[5,2,1,6]

result=map(lambda p,s : p*s,price,stock)
print(tuple(result))

# 컴프리핸션을 이용하기
result=[x**2 for x in list_data]
print(result)

# zip()함수를 이용하기
# 두개의 리스트/튜플을 한개의 리스트로 합쳐줌
result=zip(price,stock)
print(list(result))
result=[x*y for x,y in zip(price,stock)]
print(result)

# 문자열 -> 태그방식으로 변환해주기
# li태그로 만들기
names=["짱구","뽀로로","도라에몽","헬로키티","마이멜로디","호빵맨","시나모롤"]

list1=map(lambda n : f"<li>{n}</li>",names)
list2=[f"<li>{n}</li>" for n in names]
result=zip(list1,list2)

# filter함수
result=filter(lambda x : len(x)>=4,names)
print(tuple(result))

result=[n for n in names if len(n)>=4]
print(result)

list1=[1,2,3]
list2=[0.2,0.3]
result=zip(list1,list2)
print(tuple(result))


print(tuple(zip(list1,price,stock)))

# 행렬 전치할때 사용이 가능
matrix=[[2,4,6],[1,3,5]]
print(f"전치결과 : {list(zip(*matrix))}")

