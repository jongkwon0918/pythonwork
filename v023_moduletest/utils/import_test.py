# 변수
MAX_LEVEL=99
SERVET_NAME='Asia-1'

# 함수
def save_game(user_id) : 
    print(f"{user_id}님의 현재 상태를 저장합니다.")

# 클래스
class Player : 
    def __init__(self,name) -> None:
        self.__name=name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name) : 
        self.__name=name
    def __str__(self) -> str:
        return self.name