# 딕셔너리 자료형을 이용하기
# key:value 쌍으로 이루는 저장방식 -> 자바의 Map과 유사
# 리터럴 : {key:value} / dict()함수
# 기본생성
dict_data={}
print(type(dict_data))
dict_data=dict()
print(type(dict_data))

# 초기화 후 dict생성하기
dict_data={1:"a",2:"b",3:"c"}
print(dict_data)

# key값은 중복이 불가능
employee={"사원명":"김사원","나이":19,"급여":300,"급여":500}
print(employee)

# 생성된 딕셔너리에 값을 추가하기
# key:value를 추가
employee['보너스']=0.02
print(employee)

# 딕셔너리에 저장된 값을 접근
# []연산자를 이용해서 접근
print(employee['사원명'])
print(employee['나이'])

# get()이용하기
print(employee.get("급여"))
print(employee.get("보너스"))

# key값이 없을때 차이
# print(employee['성별']) # KeyError발생
print(employee.get("성별"))

# get()함수 이용시 기본값 설정하기
# 설정한 key가 있으면 key값을 반환, 없으면 설정한 default값을 반환
# get("key",default)
print(employee.get("급여",100))
print(employee.get("성별",'남'))

# setdefault()함수
# 설정한 key 값이 없으면 key를 default값과 함께 dict에 추가
print(employee.setdefault("결혼","미혼"))
print(employee)

#튜플의 데이터를 map으로 전환하기
employee_test=[("경영","홍길동"),("경영","임꺽정"),("회계","김회계"),("영업","하영업"),("회계","홍회계")]
dict_employee={} # key:[]

for key,value in employee_test : 
    dict_employee.setdefault(key,[])
    dict_employee.get(key).append(value)
print(dict_employee)

# dict에 저장된 key값을 가져오기
# keys()함수를 이용
allkey=employee.keys()
print(allkey)

for k in allkey :
    # print(employee.get(k))
    print(employee[k])

# value값 가져오기
# values()함수를 이용
print(employee.values())

for v in employee.values() : 
    print(v)

# 인덱스 값으로 접근이 불가능함
# print(allkey[0])
# print(employee.values()[0])
test_list=list(allkey)
print(test_list[0])
test_list=list(employee.values())
print(test_list[0])

# key,value를 한번에 출력하기
# items()함수를 이용 -> 리스트튜플방식으로 값을 반환
# 접근할때 이차원리스트 접근방식으로 접근
print(employee.items())
list_tuple_emp=tuple(employee.items())
print(list_tuple_emp[0])

for k,v in employee.items() : 
    print(k,v)

employee["사원명"]="재미니"
print(employee)

# dict데이터 병합하기
default_config={"host":"localhost",'port':80,"debug":False}
user_config={"port":8080,"user":"admin"}

#서버 환경 데이터 만들기
# update()함수를 이용
default_config.update(user_config)
print(default_config)

# 딕셔너리에 key가 있는지 확인하기
# in 연산자 이용하기
print("사원명" in employee)
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
# **변수명 -> js 스프레드연산자 {...변수명}

def test_unpacking(사원명, 나이, 급여) : 
    print("매개변수 받아서 처리하기")
    # print(f"사원명 : {사원명} 나이 : {나이} 급여 {급여} 보너스 : {보너스} 결혼 : {결혼}")
    print(f"사원명 : {사원명} 나이 : {나이} 급여 {급여}")

# test_unpacking(**employee)
# 가변인자를 받을때 
def test_unpacking2(x,y,**kwarg) : 
    print(x)
    print(y)
    print(kwarg)

test_unpacking2(10,20,test=10,name="test")
test_unpacking2(10,20,**employee)
test_unpacking2(10,20)


# 딕셔너리 정렬해서 출력하기
# sorted() 함수를 이용
character_dict={"pororo":"뽀로로","loopy":"루피","herry":"해리","crong":"크롱","pobi":"포비","eddy":"에디"}
import operator
# operator.itemgetter(0/1)
# 0 : key를 기준으로 정렬
# 1 : value기준으로 정렬
result=sorted(character_dict.items(), key=operator.itemgetter(0))
print(result)
result=sorted(character_dict.items(), key=operator.itemgetter(1),reverse=True)
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








