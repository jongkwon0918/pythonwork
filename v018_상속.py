# 상속이용하기
class Parent : 
    def __init__(self,title,data) : 
        self.title=title
        self.data=data
        # private 속성설정
        self.__private_data="비밀"
   
    def parent_method(self) : 
        print("부모메소드")
    
    def common_method(self) : 
        print("자식들이 재정의 해서 사용하는 것")
    
    @property
    def private_data(self) : 
        return self.__private_data
    @private_data.setter
    def private_data(self,value) : 
        self.__private_data=value

# 상속관계 설정하기
# 클래스 선언부에서 (상속할 클래스명)
class Child(Parent) :
    def __init__(self,title,data,c_data) : 
        super().__init__(title,data) # 부모속성이 생성되지 않음
        self.c_data=c_data

    # 부모 메소드 오버라이딩하기
    def common_method(self):
        print("자식이 재정의한 메소드")

    # 메소드에서 부모의 속성에 접근하기
    def use_attr(self) : 
        print(self.title)
        print(self.data)
        print(self.c_data)

    # private 속성에 접근하기
    def use_private_attr(self) : 
        # print(self.__private_data)
        print(self.private_data) # getter를 호출

c=Child("부모",[1,2,3,4],"자식")
print(c.title,c.data,c.c_data)
c.common_method()
c.use_attr()
c.use_private_attr()
c.private_data="너 이제 비밀아니야"
print(c.private_data)

# 다중상속 가능함
class Root : 
    def __init__(self) : 
        self.data="루트"

    def test(self) : 
        print("루트메소드")
        print(self.data)
    
class SecondA(Root) : 
    def __init__(self) : 
        super().__init__()
        self.data="세컨드A"

    def test(self) : 
        print("세컨트A 메소드")
        print(self.data)

class SecondB(Root) : 
    def __init__(self) : 
        super().__init__()
        self.data="세컨드B"

    def test(self) : 
        print("세컨트B 메소드")
        print(self.data)        

# 내부적으로 상속관계에 대한 순서를 저장
# MRO를 이용해서 저장 -> 왼쪽에서 오른쪽 순서로 저장
class Test(SecondA,SecondB) : 
    def __init__(self):
        super(SecondA,self).__init__()
    
    def check_run(self) : 
        super(SecondB,self).test()
        # self.test() #??????
test=Test()
test.check_run()        
print(f"MRO정보 \n{Test.__mro__}")
print(Test.mro())

class Animal : 
    def __init__(self,name) : 
        self.name=name

    def speak(self) : 
        print("짖어봐")

# 상속 -> 다형성 -> 동일한 메소드가지고 있는 객체를 처리
class Duck(Animal) : 
    def __init__(self, name):
        super().__init__(name)

    def speak(self) : 
        print("꽥꽥")
class Dog(Animal) : 
    def __init__(self, name):
        super().__init__(name)

    def speak(self) : 
        print("멍멍")
class Note : 
    def write(self, data) : 
        print(f"{data}를 노트에 작성")
duck=Duck("도날드덕")
dog=Dog("구피")
for animal in (duck,dog) : 
    animal.speak()

def bark(animal) : 
    animal.speak()
bark(duck)
bark(dog)
# bark(Note())

# 메소드를 강제할 수 있는 데코레이터를 제공
# 추상클래스와 추상메소드 
from abc import ABC,abstractmethod
# 추상클래스 선언하기
class BasicAbstract(ABC) : 
    def __init__(self) -> None:
        super().__init__()
        self.data="data"
    @abstractmethod
    def abstract_method_test(self):
        pass
# test=BasicAbstract()
# print(test)

class ChildImplement(BasicAbstract) : 
    def abstract_method_test(self):
        print("추상메소드 구현하기")
    
child_impl=ChildImplement()


# 결제 기능 구현하기
class Payment(ABC) : 
    @abstractmethod
    def pay(self,amount):
        pass

class CashPayment(Payment) : 
    def pay(self,amount) : 
        print(f"{amount}가 현금으로 결제 되었습니다")

class CardPayment(Payment) : 
    def pay(self,amount) : 
        print(f"{amount}가 카드로 결제 되었습니다")


class Controller : 
    def __init__(self,pay_method) -> None:
        self.pay_method=pay_method
    
    def purcharse(self,method:str,product) : 
        self.pay(self.pay_method[method],product.price)

    def pay(self,payment,account:int):
        payment.pay(account)

from dataclasses import dataclass
@dataclass
class Product : 
    name:str
    price:int

p=Product("노트북",200)
p1=Product("핸드폰",170)
controller=Controller({"cash":CashPayment(),"card":CardPayment()})
controller.purcharse("card",p)
controller.purcharse("cash",p)


class MLModel(ABC) :
    @abstractmethod
    def train(self,x) : 
        pass
    @abstractmethod
    def predict(self,x) : 
        pass
class LinearRegression(MLModel) : 
    def __init__(self) -> None:
        super().__init__()
        self.weight=10
        self.bias=3

    def train(self,x) : 
        print("선형 회귀 학습")

    def predict(self, x):
        return (self.weight*x)+self.bias
    
