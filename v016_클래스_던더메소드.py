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

p=MagicMethodTest("핸드폰",1200000)
print(p)
p1=MagicMethodTest("닌텐도",800000)
result=p+p1 # p.__add__(p1)
print(result)
result=result-p1
print(result)

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