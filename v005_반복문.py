# 파이썬에서 반복문은 간단하고 유연하게 사용이 가능
# for문 -> 자바의 foreach문과 유사함

#  for 변수 in range(값[,끝(포함X),간격])
# 0 ~ 9까지 출력하기
for i in range(10) : 
    print(i,end=" ")
print();
# 1 ~ 10까지 출력하기
for i in range(1,11) : 
    print(i,end=" ")
print()
# 10 ~ 1까지 출력하기
for i in range(10,0,-1) : 
    print(i,end=" ")
print()
# 간격을 조정하기
# 1~10까지 짝수출력하기
for i in range(2,11,2) : 
    print(i,end=" ")
print()

for i in range(1,11) : 
    if i%2==0 : print(i,end=" ")
print()

# 입력받은 단의 구구단 출력하기
dan=int(input("단 : "))
for i in range(1,10) : 
    print(f"{dan} X {i} = {dan*i}")

# for문은 리스트와 튜플을 이용할 수도 있다.
for s in ["가","나","다"] : 
    print(s)

# while
# 의도적인 무한루프, 조건에 맞는 루프를 처리할때
count=0
while True : 
    print("무한루프")
    if (count:=count+1) ==10 : break;

# 끝을 입력할때 까지 입력값을 저장하고 모든 입력을 출력하기
total=""
while (input_str:=input("입력값 : "))!="끝" :
    total+=input_str
print(total)
