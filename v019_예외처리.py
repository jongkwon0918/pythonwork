# 예외처리하기
# 예외처리 구문
# try : 
#   예외발생구문
# except 발생예상 예외 as 변수명 :
# [else : ]
# [finally :  ]
import traceback
def input_data() : 
    try : 
        a=int(input("정수입력 : "))
        return a
    except ValueError as e : 
        print(e)
        traceback.print_exc()

# result=input_data()
# print("추가 로직 실행")
# print(result)

test_data=[]
try : 
    test_data[0]=100
except IndexError as e : 
    # e : 에러 객체 -> 발생한 에러에 대한 정보를 저장하고 있는 객체
    print(e)
    print(e.args) # 예외클래스의 생성자에 전달된 인수를 확인 -> 오류 메세지
    print(e.__traceback__) # traceback객체를 저장한 속성 -> 튜플
    print(e.__traceback__.tb_frame.f_code.co_filename) # 예외발생 파일명
    print(e.__traceback__.tb_frame.f_code.co_name) # 예외발생 apthemaud
    print(e.__traceback__.tb_frame.f_lineno) # 예외발생 apthemaud

# 다중으로 예외처리하기
# test_data.append(10)
try : 
    # IndexError
    test_data[0]="23124"
    # ValueError
    su=int(input("정수입력 : "))
except IndexError as e : 
    print("인덱스 에러")
except ValueError as e : 
    print("형변환 에러")
except Exception as e : 
    print("에러발생!")   


# else, finally구문이용하기
try : 
    # result=1/2
    result=1/0
except ZeroDivisionError as e : 
    print(e)
else : 
    # try문의 코드가 에러가 발생하지 않았을때
    print("예외가 발생하지 않으면 실행!")
finally : 
    print("예외와 상관없이 무조건 실행!")


try : 
    su=int(input("정수입력 : "))
except ValueError as e : 
    print("정수를 입력해야합니다.")
else : 
    print(f"입력한 값 : {su}")
    print(f"결과 : {su*2}")


# 파일입출력에서 이용하기
try : 
    f=open("data.txt","r",encoding="utf-8")
except FileNotFoundError as e : 
    print(e)
else : 
    data=f.read()
    print(f"파일내용 {data}")
    f.close()
# finally : 
#     if f : 
#         f.close()    


# DB연결시 사용하기
# try : 
#     conn=cx_Oracle.connect(user="scott",password="tiger",
#                            dsn="localhost:1521/xe")
# except cx_Oracle.DataBaseError as e : 
#     print(f"DB연결실패 {e}")
# else : 
#     cusor=conn.cursor()
#     cusor.execute("SELECT * FROM emp")

#     for empno,ename,sal in cusor : 
#         pass
# finally : 
#     if cusor : 
#         cusor.close()
#     if conn : 
#         conn.close()

# 예외발생시키기
# raise예약어를 이용
# raise ValueError("메롱 에러지롱!")

# 나만의 에러를 만들기

import utils.CustomException as myex
import datetime

def check_admin(id) : 
    if id!='admin' : 
        raise myex.AdminError(datetime.datetime.now(),"관리자가 아닙니다.")

try : 
    check_admin("user")
except myex.AdminError as e : 
    print(e)
    print(e.trigger_date)