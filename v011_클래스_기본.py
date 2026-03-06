# 파이썬에서 클래스 선언하기
# 클래스 내부 구성
# 생성자, 속성(필드), 메소드를 내부에 선언할 수 있음

# 기본 클래스 만들기
# 클래스 이름은 첫글자 대문자로 사용 -> 파스칼케이스
class BasicObj : 
    # 생성자 선언
    def __init__(self) : 
        # 속성설정
        # self를 이용해서 변수를 선언하면 속성이 됨
        self.data="기본데이터"
        self.items=[]
    # 메소드
    def get_data(self) : 
        return "문구반환하기"

# 클래스로 객체 생성하기
# 객체 생성 -> 클래스명()
basic_obj=BasicObj()
print(basic_obj)

# 객체 속성에 접근하기
print(basic_obj.data)
print(basic_obj.items)


# 속성에 새로운 값 저장하기
basic_obj.data="쉬는시간"
print(basic_obj.data)
basic_obj.items.append("break-time")
print(basic_obj.items)

# 인스턴스메소드 호출하기
print(basic_obj.get_data())

basic_obj2=BasicObj()
print(basic_obj2.data)
