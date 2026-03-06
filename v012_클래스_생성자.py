class ConstructorDefault : 
    def __init__(self) : 
        self.test=""

class ConstructorParam : 
    def __init__(self,name) : 
        self.name=name

test=ConstructorParam("유병승")
print(test.name)

class ConstructorTest :
    pass
    # def __init__(self,name,age) :
    #     self.name=name
    #     self.age=age

    # def __init__(self,name) :
    #     self.name=name

    # 오버로딩은 안됨
    def __init__(self,*args,**kwargs) :
        if len(args) > 1 :
            self.name,self.age=args
        elif len(kwargs)>1 :
            self.name=kwargs.get('name',"")
            self.age=kwargs.get("age",19)
        else :
            self.name="아무개"
            self.age=10

test=ConstructorTest()
print(f"{test.name} {test.age}")
test=ConstructorTest("박종권",20)
print(f"{test.name} {test.age}")
test=ConstructorTest(age=30, name="김태우")
print(f"{test.name} {test.age}")

data={"name":"하승우","age":40}
test=ConstructorTest(**data)
print(f"{test.name} {test.age}")
data=["신동호",50]
test=ConstructorTest(*data)
print(f"{test.name} {test.age}")

test=ConstructorTest("김재민",age=60)
print(f"{test.name} {test.age}")



