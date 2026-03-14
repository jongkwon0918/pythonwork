# 모듈을 가져오는 방식

# 모듈전체를 가져오기
import utils.import_test
# 모듈에 별칭을 부여해서 가져오기
import utils.import_test as importtest

# 모듈에서 특정 데이터, 함수, 객체만 가져오기
from utils.import_test import save_game as save, MAX_LEVEL as level

def main() : 
    print(utils.import_test.MAX_LEVEL)
    utils.import_test.save_game("user01")
    p=utils.import_test.Player("박종권")
    print(p)
    print(importtest.SERVET_NAME)

    # save_game(p.name)
    # print(MAX_LEVEL)
    save("동호")
    print(level)

if __name__ =='__main__' : 
    main()