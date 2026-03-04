# Set
# 중복값을 저장하지 않는 객체, 순서가 없음
# 생성 => {값,값,...} / set()
# 빈 Set을 생성 -> a={} x / set()

set_data={1,2,3,4}
print(set_data,type(set_data))
set_data={1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4}
print(set_data)

# 다수 자료형을 저장하기
# List자료형은 저장이 불가능함.
# set데이터 튜플 데이터만 저장이 가능함.
set_other={1,2,'가','나',180.5,True,(1,2,3),(1,2,3)}
print(set_other)

# set 데이터 조작하기
# 메소드 이용
set_data.add(10)
set_data.add(20)
print(set_data)
# 다수 요소를 추가하기
# update()
set_data.update(range(10,20))
print(set_data)
# 요소 삭제하기
# remove()
try : 
    set_data.remove(100)
except : 
    print("지정된 요소가 없습니다")

print(set_data)

# discard() 요소삭제-> 요소가 없어도 에러가 발생하지 않음
set_data.discard(11)
print(set_data)

set_data.discard(100)
print(set_data)

# pop() : 임의값의 잘라내기함.
# 3.8 
print(set_data.pop())
print(set_data.pop())
print(set_data.pop())
print(set_data.pop())
print(set_data.pop())
print(set_data)
# 전체 삭제하기
set_data.clear()
print(set_data)
set_data=None

# 다른 타입과의 호환성
test_list=[1,1,1,1,2,3,3,3,4,4,4,5,5,6,6,6,7,7]
print(test_list)
set_data=set(test_list)
test_list=list(set_data)
print(test_list)
# 문자열에서 중복값 제거하기
str_data=f"{'김'*10}{'밥'*10}{'천국'*5}"
print(str_data)
result=set(str_data)
print(result)
str_data=''.join(result)
print(str_data)

# set(집합)
# 집합연산자 활용하기
# 합집합 연산
# set|set
set_data={1,2,3,4,5,6,7}
set_data2={5,6,7,8,9,10}
set_result=set_data | set_data2
print(set_result)
set_str={'가','나','다','라'}
set_result=set_data|set_str
print(set_result)
# set_result=set_data|['하','호','하','가']
# print(set_result)


# 메소드 : union() -> 다른 타입도 가능
set_result=set_data.union(set_data2)
print(set_result)
set_result=set_data.union(['하','호','하','가'])
print(set_result)
set_result=set_data.union("하하하하하 호호호호호 후후후후후 히히히히")
print(set_result)
temp="".join([x for x in "하하하하하 호호호호호 후후후후후 히히히히" if x!=" "])
print(temp)

# 교집합연산
set_result=set_data&set_data2
print(set_result)

# intersection() 메소드 이용
# 두 집합의 공통된 요소를 반환하는 메소드

set_result=set_data.intersection(set_data2)
print(set_result)
set_result=set_data.intersection([1,2,3,4,5,6])
print(set_result)

# 차집합
set_result=set_data-set_data2
print(set_result)
# difference()
set_result=set_data.difference((1,2,3,4))
print(set_result)

#대칭차집합
set_result=set_data^set_data2
print(set_result)
# symmetric_difference()함수를 이용
# 두 집합 중 한 곳에만 존재하는 요소들의 합집합을 반환하는 메소드
set_result=set_data.symmetric_difference(set_data2)
print(set_result)

# 인플레이스 연산자 
# |= 합집합
set_data={1,2,3,4,5}
set_data2={3,4,5,6,7,8}
result=set_data|set_data2
set_data|=set_data2
print(set_data)

#교집합
set_data&={1,2,3,4,5,6}
print(set_data)

# -= 차집합, ^= 대칭차집합

# set데이터간 포함관계를 확인하기 -> 대소비교를 통해 확인
set_data={1,2,3,4,5}
set_data2={2,3,4}
set_data3={2,3,6}
set_data4={1,2,3,4,5,6,7,8,9,10,11,12}
#요소 전체가 포함이 되어야 True /아니면 False
print(f"set_data>=set_data2 : {set_data>=set_data2}")
print(f"set_data>=set_data3 : {set_data>=set_data3}")

print(f"set_data<=set_data2 : {set_data<=set_data2}")
print(f"set_data<=set_data3 : {set_data<=set_data3}")
print(f"set_data<=set_data4 : {set_data<=set_data4}")

#서로소를 확인하는 메소드 -> 서로 두 집합간 같은 값이 없으면 true, 아니면 false
#isdisjoint() 함수
print(f"중복값 20,30 : {set_data.isdisjoint({20,30})}")
print(f"중복값 1,30 : {set_data.isdisjoint({1,30})}")

#수정이 불가능한 Set만들기
#frozenset()함수를 이용
fset_data=frozenset({10,20,30,40})
fset_data2=frozenset({1,2,30,40})
print(fset_data)
# fset_data.add(100) -> 수정이 불가능한 set으로 만듦
#set_data.add(200)

#집합연산가능
print(fset_data|fset_data2)

#리스트에서 중복값을 제거
names=["유병승","아인슈타인","홍길동","둘리","김김동","유병승","이순신","유병승","재미나이","유병승"]
#중복값 제거 후 리스트로 출력하기 반복문으로 출력
result=list(set(names))
for name in result :
    print(name)

#데이터를 in연산자 조회할때 list보다 set 더 좋다
data=list(range(10000000))
set_data=set(data)
import time
start=time.time()
if 300 in data :
    print("찾았다")
    print(f"리스트로 찾기 :{time.time()-start}")

start=time.time()
if 300 in set_data :
    print("찾았다")
    print(f"셋으로 찾기 : {time.time()-start}")

#장바구니 목록에서 구매하지 않은 품목찾기
cart_pro={"컴퓨터", "키보드", "마우스"}
buy_pro={"키보드","마우스"}
result=cart_pro-buy_pro
print(result)

#컴프리핸션 이용하기
str="이것을 반복해서 만들어보자구요! 집중해서"
set_str={s for s in str}
print(set_str)
# 1~100사이 값 중 3의 배수, 8의 배수를 set으로 만들기
set_num={n for n in range(1,100) if n%3==0 or n%8==0}
print(set_num)

#딕셔너리 자료형을 이용하기
#key:value 쌍으로 이루는 저장방식 -> 자바의 Map과 유사
#리터럴 : {key:value} / dict()함수
#기본생성
dict_data={}
print(type(dict_data))
dict_data=dict()
print(type(dict_data))

#초기화 후 dict 생성하기
dict_data={1:"a",2:"b",3:"c"}
print(dict_data)

#key값은 중복이 불가능
employee={"사원명":"김사원","나이":19,"급여":300,"급여":500} #마지막 값만 출력
print(employee)

#생성된 딕셔너리에 값을 추가하기
#key:value를 추가
employee['보너스']=0.02
print(employee)

#딕셔너리에 저장된 값을 접근
#[]연산자를 이용해서 접근
print(employee['사원명'])
print(employee['나이'])
# get() 이용하기
print(employee.get('급여'))
print(employee.get('보너스'))

#key 값이 없을때 차이
# print(employee['성별']) #keyError 발생
print(employee.get("성별"))

#get()함수 이용시 기본값 설정하기
#설정한 key가 있으면 key값을 반환, 없으면 설정한 default값을 반환
#get("key","default")
print(employee.get("급여",100))
print(employee.get("성별","남"))

#setdefault()함수
#key에 설정할 값이 없으면 key를 default값과 함께 dict에 추가
print(employee.setdefault("결혼","미혼"))
print(employee)

#튜플의 데이터를 map으로 전환하기
employee_test=[("경영","홍길동"),("경영","임꺽정"),("회계","김회계"),("영업","하영업"),("회계","박회계")]
dict_employee={} #key:[]

for key, value in employee_test :
    dict_employee.setdefault(key,[])
    dict_employee.get(key).append(value)
print(dict_employee)

#dict에 저장된 key값을 가져오기
#keys()함수를 이용
allkey=employee.keys()
print(allkey)

for k in allkey :
    # print(employee.get(k)) -> 이게 더 안정적임
    print(employee[k])

#value값 가져오기
#values()함수 이용하기
print(employee.values())

for v in employee.values() :
    print(v)

#인덱스 값으로 접근이 불가능함
#print(allkey[0])
# print(allkey.values()[0])
test_list=list(allkey)
print(test_list[0])
test_list=list(employee.values())
print(test_list[0])

#key, value를 한번에 출력하기
#items()함수를 이용 -> 리스트튜플방식으로 값을 반환
#접근할때 이차원리스트 접근방식으로 접근
print(employee.items())
list_tuple_emp=tuple(employee.items())
print(list_tuple_emp[0][0])
print(list_tuple_emp[0])

for k,v in employee.items() : 
    print(k,v)

employee["사원명"]="재미니"
print(employee)

#dict데이터 병합하기
default_config={"host":"localhost","port":80,"debug":False}
user_config={"port":8080,"user":"admin"}

#서버환경 데이터 만들기
#update()함수 이용하기
default_config.update(user_config)
print(default_config)

#딕셔너리에 key가 있는지 확인하기
#in 연산자 이용하기
print("사원명" in employee)
print("재미니" in employee)  #value 조회안됨
print("재미니" in employee.values())

# dict 저장된 데이터 가져오기
# pop(), popitem()함수 이용
# result=employee.pop("결혼")
# print(result)
# print(employee)
# result=employee.popitem()# 마지막 key:value
# print(result)
# print(employee)

# del을 이용해서 key삭제하기
# del employee["급여"]
# print(employee)

# 언패킹 이용하기
# key와 일치하는 변수에 값을 저장
# dict을 병합할때 사용 -> 3.9이상에서 사용이 가능
# **변수명 -> js 스프레드 연산자{...변수명}

# def test_unpacking(사원명, 나이, 급여) : 
#     print("매개변수 받아서 처리하기")
#     print(f"사원명 : {사원명} 나이 : {나이} 급여 {급여}")

# test_unpacking(**employee)
#가변인자를 받을때
def test_unpacking2(x,y,**kwarg) :
    print(x)
    print(y)
    print(kwarg)
test_unpacking2(10,20,test=10,name="test")
test_unpacking2(10,20,**employee)
test_unpacking2(10,20)

#딕셔너리 정렬해서 출력하기
#sorted()함수를 이용하기
character_dict={"pororo":"뽀로로", "lupy":"루피","herry":"해리","crong":"크롱","pobi":"포비","eddy":"에디"}
import operator
# operator.itemgetter(0/1)
# 0 : key를 기준으로 정렬
# 1 : value를 기준으로 정렬
result=sorted(character_dict.items(), key=operator.itemgetter(0))
print(result)
result=sorted(character_dict.items(), key=operator.itemgetter(1))
print(result)

# 컴프리핸션이용하기
# 컴프리핸션이용해서 새로운 딕셔너리 만들기
user=["admin","user01","user02","user03"]
result={id:i for i,id in enumerate(user)}
print(result)
result['admin']+=1
print(result)
# result={}
# for u in user : 

# 값 조건필터링하기
score={"오수환":100,"김영호":87,"하승우":50,"강원준":10}
# 80점 이상인 학생만 있는 dict만들기

fruits={"apple":1.5,"banana":4,"cherry":12,"pear":6}
# 원화변경해서 새로운 dict만들기
won_fruits={f:int(v*1500) for f,v in fruits.items()}
print(won_fruits)

# 아래 데이터에서 제품별 총 매출과 고객별 구매목록을 출력하기
revenue_by_item={} # 제품별 총 매출,
items_by_customer={} # 고객 구매 목록
sales_data = [
    {'customer_id': 'userA', 'item': '노트북', 'price': 1500},
    {'customer_id': 'userB', 'item': '모니터', 'price': 300},
    {'customer_id': 'userA', 'item': '마우스', 'price': 40},
    {'customer_id': 'userC', 'item': '키보드', 'price': 120},
    {'customer_id': 'userB', 'item': '노트북', 'price': 1000},
    {'customer_id': 'userA', 'item': '키보드', 'price': 120},
]
for sale in sales_data : 
    item=sale['item']
    price=sale['price']
    cumstomer=sale['customer_id']
    revenue_by_item.setdefault(item,0)
    revenue_by_item[item]+=price
    items_by_customer.setdefault(cumstomer,[])
    items_by_customer[cumstomer].append(item)

print(revenue_by_item)
print(items_by_customer)

# 노트북 2800, 그래픽카드 : 3000 -> 판매금액
new_items={"노트북":2800,"그래픽카드":3000}
for item,price in new_items.items() : 
  revenue_by_item.setdefault(item,0)
  revenue_by_item[item]+=price  
# revenue_by_item.update(new_items)
print(revenue_by_item)


