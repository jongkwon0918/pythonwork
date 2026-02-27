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


