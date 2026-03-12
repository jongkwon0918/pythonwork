# 매직 메소드 활용
# 클래스내부에 선언되는 특별한 용도로 사용되는 메소드
# 메소드명 앞,뒤에 __ 가 있는 메소드

class MagicMethodTest : 

    def __init__(self,name, price):
        self.name=name
        self.price=price
    
    # 객체의 정보를 출력해주는 매직메소드
    # 객체를 print()함수의 인자로 전달하면 하면 자동으로 실행되는 메소드
    # def __str__(self): return 출력할내용 -->java의 toString()메소드와 유사한 기능
    # 일반적으로 사용하는 객체의 내용을 출력하는 기능
    def __str__(self) : 
        return f"이름 : {self.name} 가격 : {self.price}"
    
    # 개발자가 사용하는 용도 -> 개발자가 객체의 정보를 확인하는 용도
    def __repr__(self) : 
        return f"MagicMethodTest(name={self.name},price={self.price})"

    # 연산자 함수
    # 객체의 연산자 이용을 가능하게 해주는 함수
    # +, -....
    # __add__() : 더하기 연산자를 사용할 수 있게 해줌
    # def __add__(self, other) : 
    #    return [self,other]

    def __add__(self,other) : 
        # print(self)
        # print(other)
        names=f"{self.name},{other.name}"
        price=self.price+other.price
        return MagicMethodTest(names,price)
        # return [self,other]

    def __sub__(self,other) : 
        names=self.name.split(",")
        if other.name in names : 
            names.remove(other.name)
            names=",".join(names)
            price=self.price-other.price
            return MagicMethodTest(names,price)
        else : 
            raise Exception("빼기 연산이 불가능합니다.")

    # 비교연산
    # __eq__, __lt__ (<), __gt__ (>)  
    def __hash__(self) : 
        return hash((self.name,self.price))
    def __eq__(self,other) : 
        return self.name==other.name and self.price==other.price
    
p=MagicMethodTest("핸드폰",1200000)
print(p)
p1=MagicMethodTest("닌텐도",800000)
result=p+p1 # p.__add__(p1)
print(result)
result=result-p1
print(result)
p2=MagicMethodTest("핸드폰",1200000)
p3=MagicMethodTest("핸드폰",1200000)
# product_set=set([p,p1,p2,p3])
product_set={p,p1,p2,p3}
print("=============")
print(product_set)
print("=============")

class Order : 
    def __init__(self,carts:list=[]) : 
        self.carts=carts

    # Order[0] Order[1]
    def __getitem__(self, product):
        return self.carts[product]
    
    # Order[10]=값
    def __setitem__(self, key, value):
        self.carts[key]=value

    def __len__(self) : 
        return len(self.carts)
    # in 연산이 가능하게 해줌
    def __contains__(self, item):
        return item in self.carts
    
    # 반복문에서 사용이 가능
    def __iter__(self):
        return iter(self.carts)

    def __str__(self) : 
        return f"{self.carts}" 
    
order=Order(["핸드폰","닌텐도","김밥"])
print(order)
order[-1]="감자"
order[-2]="고구마"
print(order)
print(order[0])

print("재미니" in order)

for o in order : 
    print(o)

# __enter__, __exit__ 메소드
# with예약어를 이용할 때 사용되는 메소드들
# with 클래스생성 as 별칭 : 
#   실행 코드 작성
import time
class SimpleTest : 
    def __init__(self,title) : 
        self.title=title

    def __enter__(self) : 
        print("== 작업 시작 ==")
        self.start=time.time()
        return self
    
    def __exit__(self, exc_type,exc_value,traceback) : 
        print("== 작업 종료 ==")
        duration=time.time()-self.start
        print(f"작업 소요시간 : {duration}")
        if exc_type : 
            print(f"에러타입 : {exc_type}")
            print(f"에러내용 : {exc_value}")
            print(traceback)
    def test_method(self,data) : 
        if len(data)<=2 : 
            raise BaseException("에러 발생")
        self.title=data
try : 
    with SimpleTest("클래스 사용") as st : 
        time.sleep(0.5)
        # st.test_method("정상처리"
        st.test_method("안")
except BaseException as e :
    print(f"에러 발생!!! : {e}") 

# __call__함수
# 생성된 객체를 함수처럼 호추하게 해주는 기능

class ModelTest : 
    def __init__(self, weight,bias) : 
        self.weight=weight
        self.bias=bias

    def __call__(self, x) : 
        print(f"입력값 : {x} -> ",end=" ")
        prediction=(self.weight*x)+self.bias
        print(f"예측 : {prediction}")
        return prediction
    
linear_model=ModelTest(weight=3, bias=2)
pred=linear_model(20)
print(pred)