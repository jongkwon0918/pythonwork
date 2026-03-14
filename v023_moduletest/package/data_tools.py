from datetime import datetime
def is_weekend() : 
    # 0 월 ~ 6 일
    today=datetime.now().weekday()
    return today>=5
def get_today_str() : 
    return datetime.now().strftime("%Y년 %m월 %d일")