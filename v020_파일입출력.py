# 파일관리

# pathlib모듈 이용해서 관리하기
from pathlib import Path

home=Path.home()
print(home) # 사용자 계정의 기본폴더를 가져옴

# 현재폴더 경로 가져오기
current_path=Path.cwd()
print(current_path)

# 새폴더 생성하기
# / 연산 : __truediv__() 매직메소드를 실행 -> Path
data_dir=current_path / "data"

# 매개변수
# mode : 0x777 -> 폴더 권한설정
# parents : 부모디렉토리가 없으면 FileNotFoundError가 발생, True -> 부모 디렉토리를 생성해서 만듬
data_dir.mkdir(exist_ok=True) # 디렉토리가 존재하면 FileExistsError가 발생(False)

# 파일 생성 및 쓰기
file=data_dir / "test.txt"
file.touch()

# write_text : 텍스트 데이터를 파일에 출력해주는 함수
# 파일이 없으면 생성하고, 있으면 덮어쓰기함
file=data_dir / "example.txt"
file.write_text("Hello 파이썬", encoding="utf-8")

# 파일 상태 확인
print(file.is_dir())
print(file.is_file())

print(file.exists())
# file=data_dir / "test2.txt"
# print(file.exists())
print(file.stat().st_size)

print("하위 폴더 검색하기")
for dir in home.iterdir() : 
    print(dir)

print("파일 검색하기 -> 패턴으로..")

for f in current_path.glob("v01*.py") : 
    print(f)

print(file.stat().st_mode)

# 파일명 변경하기
# (data_dir / "test.txt").rename(data_dir/"mydata.txt")

# 파일 삭제
# (data_dir/"mydata.txt").unlink()

# 폴더 삭제하기 -> 폴더가 비어있을때만 가능
# data_dir.rmdir()

# read_text()함수를 이용해서 파일에 저장된 내용을 가져올 수 있음
file=data_dir / "example.txt"
content=file.read_text(encoding="utf-8")
print(content)


# os모듈이용
# os.path를 이용해서 경로 가져오기
import os
current_dir=os.getcwd()
print(current_path)
# 절대경로를 생성하기
file_path=os.path.join(current_dir,"demo.txt")
print(file_path)

if os.path.exists(file_path) : 
    print("파일이 존재합니다.")
else : 
    print("파일이 존재하지 않습니다")

print(os.path.isdir(file_path))

# os.mkdir() # 한개 폴더생성
# os.makedirs() # 다수 폴더를 생성

result=os.listdir(current_dir)
print(result)
# os.remove()
# os.removedirs()

# os.removedirs(os.path.join(current_dir,"data")) # 파일이 있으면 삭제 불가능

# shutil모듈 이용해서 파일다루기
import shutil

data_dir2=Path("shutil_test/source_dir")
os.makedirs(data_dir2,exist_ok=True)
os.makedirs("shutil_test/target_dir",exist_ok=True)

# 파일생성하기
(data_dir2 / "file_to_copy.txt").write_text("복사테스트")
(data_dir2 / "file_to_move.txt").write_text("이동테스트")

# 파일복사하기
# shutil.copy()
shutil.copy(
    'shutil_test/source_dir/file_to_copy.txt',
    'shutil_test/target_dir/file_to_copy.txt'
)
shutil.move(
    'shutil_test/source_dir/file_to_move.txt',
    'shutil_test/target_dir/file_to_move.txt'
)

# 폴더를 통째로 복사하기
# copytree()함수를 이용

# os.makedirs('shutil_test/copied_tree', exist_ok=True)
# shutil.copytree(
#     'shutil_test/target_dir',
#     'shutil_test/copied_tree'
# )

# shutil.rmtree() -> 폴더 통째로 삭제
# try : 
#     shutil.rmtree('shutil_test/copied_tree')
# except OSError as e : 
#     print(e)

# 파일입출력
# open함수를 이용해서 입출력하기
# 파일을 열어서 읽고, 쓰기를 간편하게 할 수 있는 함수 -> 반환형 파일객체
# 매개변수
# file경로, mode(r,w), encode
# with open() as f : 
try :
    with open("data/poem.txt", mode="r",encoding="UTF-8") as f : 
        # print(f.read())
        # print(type(f.read()))
        # 개행을 기준으로 데이터를 가져오기
        # print(f.readline())
        while True : 
            newdata=f.readline()
            if not newdata : 
                break
            print(newdata.strip())
        f.seek(0)
        poem_list=f.readlines()
        # poem_list=list(map(lambda s:s.strip(),poem_list))
        poem_list=[s.strip() for s in poem_list if len(s)>1]
        print(poem_list)
except FileNotFoundError as e : 
    print(e)
except Exception as e : 
    print(e)

from dataclasses import dataclass
import datetime
order=[]
@dataclass
class OrderDetail : 
    order_id:int
    customer_name:str
    product:str
    quantity:int
    price:int
    order_date:datetime.datetime
    status:str

try : 
    with open("data/test.csv","r",encoding="utf-8") as f : 
        row_list=[o.strip() for o in f.readlines()][1:]
        print(row_list)
        for row in row_list: 
            data=row.split(",")
            if len(data) == 7 : 
                try : 
                    od=OrderDetail(int(data[0]),
                                   data[1],data[2],
                                   int(data[3]),
                                   int(data[4]),
                                datetime.datetime.strptime(data[5],'%Y-%m-%d'),
                                data[6])
                except (ValueError,TypeError) as e : 
                    print(e)
                    print("[경고] 데이터 변환 중 에러가 발생했습니다.")
                else : 
                    order.append(od)
except FileNotFoundError as e : 
    print(e)
except Exception as e : 
    print(e)

for o in order : 
    print(o)

try : 
    with open("data/test.jpg", mode="rb") as f : 
        img_data=f.read()
    with open("data/test3.jpg", mode="wb") as f :
        f.write(img_data)
except  FileNotFoundError as e :
    print(e) 
target="1011,유병승,강남 아파트,2,12000,2025-12-03,배송완료"
try : 
    with open("data/test.csv",mode="a",encoding="UTF-8") as f : 
        f.write(target)
except  FileNotFoundError as e :
    print(e) 