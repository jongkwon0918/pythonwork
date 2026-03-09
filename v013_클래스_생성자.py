class ConstructorDefault : 
    def __init__(self) : 
        self.test=""

class ConstructorParam : 
    def __init__(self,name) : 
        self.name=name

test=ConstructorParam("유병승")
print(test.name)

class ConstructorTest : 
    # def __init__(self,name,age=10) : 
    #     self.name=name
    #     self.age=age

    # def __init__(self,name) : 
    #     self.name=name

    # 오버로딩은 안되나요? 응!
    def __init__(self,*args,**kwargs) : 
        if len(args) > 1 : 
            self.name,self.age=args
        elif len(kwargs)>1 : 
            self.name=kwargs.get("name","")
            self.age=kwargs.get("age",10)
        else : 
            self.name="아무개"
            self.age=10
        
test=ConstructorTest()
print(f"{test.name} {test.age}")
test=ConstructorTest("유병승",19)
print(f"{test.name} {test.age}")
test=ConstructorTest(age=19,name="유병승")
print(f"{test.name} {test.age}")

data={"name":"하승우","age":25}
test=ConstructorTest(**data)
print(f"{test.name} {test.age}")
data=["김태우",25]
test=ConstructorTest(*data)
print(f"{test.name} {test.age}")

test=ConstructorTest("유병승",age=19)
print(f"{test.name} {test.age}")
