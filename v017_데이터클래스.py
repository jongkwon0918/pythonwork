# 데이터를 보관하는 전용 클래스 
from dataclasses import dataclass

@dataclass
class User : 
    userId:str
    password:str
    userAge:int
    height:float=180.5
    
    # 필요한 매직메소드가 자동으로 구현
    # __eq__, __init__, __repr__
    def __hash__(self) : 
        return hash((self.userId))

u=User("admin",'1234',34)
u1=User("admin",'1234',34)
print(u)
set_data={u,u1}
print(set_data)