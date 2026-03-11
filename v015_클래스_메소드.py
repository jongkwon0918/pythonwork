# 클래스내부에 선언하는 메소드는 
# 인스턴스 메소드와 클래스 메소드, 정적메소드로 구분할 수 있음

from typing import Union

class MethodTest : 
    def __init__(self, nick_name:str,items:list=[]) :
        self.nick_name=nick_name
        self.items=items
        self.level=1
    
    # 인스턴스 메소드
    def get_nick_name(self) : 
        return self.nick_name
    def add_item(self,item:str) -> None : 
        self.items.append(item)
    def level_up(self) : 
        self.level+=1
    def get_items(self) : 
        return self.items
    def use_items(self,item:Union[str,int]) : 
        if item in self.items : 
            self.items.remove(item)
        else :
            raise Exception("잘못된 아이템 호출함 비상비상")
    def get_level(self):
        return self.level
    
    def info(self) : 
        return f"{self.nick_name} {self.level} {self.items}"

ch1=MethodTest("고양이")
print(ch1.info())
ch1.add_item("츄르")
print(ch1.info())
ch1.add_item("통조림")
ch1.add_item("캣잎")
print(ch1.info())

ch1.use_items("츄르")
print(ch1.info())

# 정적메소드
# 프로젝트 내에서 공용을 사용하는 메소드를 선언할때 사용
# @staticmethod데코레이터를 이용
# 객체 생성없이 활용할 수 있는 메소드 -> self를 전달받지 않음
class StaticMethodTest : 
    def __init__(self) : 
        self.data=[]
    
    @staticmethod
    def test_static(num):
        print("static메소드 실행")
    
    # def test_method() : 
    #     print("sdasdf")

StaticMethodTest.test_static(10)
import string,random
class Utils : 
    # 이메일 유효성검사 메소드
    @staticmethod
    def is_email(email:str) -> bool : 
        """
        값에 @와 .이 있는지 확인하는 메소드
        """
        return "@" in email and "." in email.split("@")[-1]

    @staticmethod
    def create_repassword(length:int) -> str : 
        chars=string.ascii_letters+string.digits 
        return "".join(random.choice(chars) for _ in range(length))

print(Utils.create_repassword(10))


# 클래스메소드
# 클래스 메소드는 static메소드와 유사, 접근한 클래스의 정보를 확인할 수 있음
# @classmethod데코레이터를 이용해서 선언

class ClassMethodTest() : 
    def __init__(self,data:list=[]) : 
        self.data=data
    
    @classmethod
    def create_from_csv(cls,data:str):
        """csv문자열을 리스트로 변경해주는 객체를 생성"""
        return cls(data.split(","))
        # return ClassMethodTest(data.split(data))

    @classmethod
    def create_from_dict(cls,data:dict={}) : 
        return cls(list(data.values()))

    def __str__(self) : 
        return f"{self.data}"
    
test=ClassMethodTest.create_from_csv("하나,둘,셋")
print(test)

