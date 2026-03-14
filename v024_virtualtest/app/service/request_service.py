import requests, json

def test_request(no) : 
    url=f"https://jsonplaceholder.typicode.com/posts/{no}"
    response=requests.get(url)
    if response.status_code==200 : 
        print("데이터 가져오기 성공")
        data=response.json() # dict
        print(data)
    else : 
        print(f"데이터 가져오기 실패 {response.status_code}")
