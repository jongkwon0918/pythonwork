import json
import os

os.makedirs("json", exist_ok=True)

user_config={
    "username":"admin",
    "theme":"black",
    "version":1.2
}

with open("json/config.json","w",encoding="UTF-8") as f : 
    # json형태로 dict데이터를 저장
    json.dump(user_config,f)

# json파일에 저장된 데이터 불러오기
with open("json/config.json", 'r',encoding="UTF-8") as f : 
    json_data=json.load(f)
    print(json_data)

api_stringjson="""
    {
        "status":"success",
        "request_id":"req-12345",
        "data":{
            "user_id":1002,
            "email":"test@test.com",
            "updated_at":"2025-11-17T10:06:00Z"
        }
    }
"""
# 문자열형태로 가져온 JSON을 가져올 수 있음
response_data=json.loads(api_stringjson)
print(response_data, type(response_data))

str_response=json.dumps(response_data)
print(str_response,type(str_response))
