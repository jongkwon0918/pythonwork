import csv
from pathlib import Path

csv_path=Path.cwd() / "data/test.csv"

with open(csv_path,'r',encoding="utf-8") as f : 
    reader=csv.reader(f)
    for row in reader : 
        print(row)

rows=[
    ["name","age","city"],
    ["김태우","25","경남 창원시"],
    ["박종권","25","경남 창원시"],
]
with open((Path.cwd() / "csv/people.csv"),'w',encoding="utf-8") as f : 
    writer=csv.writer(f)
    writer.writerows(rows)

users=[
    {"id":"admin","pw" : "1234","name":"관리자"},
    {"id":"admin","pw" : "1234","name":"관리자"},
    {"id":"admin","pw" : "1234","name":"관리자"}
]
with open("csv/user.csv","w",newline="",encoding="utf-8") as f : 
    field_name=["id","pw","name"]
    writer=csv.DictWriter(f,field_name)

    writer.writeheader()
    writer.writerows(users)

with open("csv/user.csv","r",newline="",encoding="utf-8") as f : 
    reader=csv.DictReader(f,fieldnames=["i","p","n"])
    for row in reader : 
        print(row)

# sniffer객체이용하기 -> 추론해서 데이터 분기처리를 함.