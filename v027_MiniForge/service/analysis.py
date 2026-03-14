import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

import csv

# 그래프 한글깨지미 해결하기
from matplotlib import font_manager, rc
import platform

def data_analisis() : 
    BASE_DIR=Path(__file__).resolve().parents[2]
    print(BASE_DIR)
    DATA_PATH=BASE_DIR / 'v027_MiniForge' / 'data' / "sales.csv"
    month_per_price={}
    try:
        with open(DATA_PATH,'r',encoding="UTF-8") as f :
            reader=csv.reader(f)
            next(reader) # 해더 처리하기
            for data in reader : 
                year_month=data[0]
                pre_price=month_per_price.get(year_month,0)
                per_price=int(data[1])
                month_per_price[year_month]=pre_price+per_price
    except FileNotFoundError as e : 
        print(e)

    print(f"월별 매출 : {month_per_price}")

    # 데이터 분석
    df=pd.read_csv(DATA_PATH,dtype={"total_sales_krw":"int64"})
    print(df.head())

    # 그래프에서 한글깨짐 방지
    if platform.system() == 'Windows' : 
        font_path="C:/Windows/Fonts/malgun.ttf"
    elif platform.system() == "Darwin" : 
        font_path="/System/Linbrary/Fonts/Supplemental/AppleGothic.ttf"

    font_name=font_manager.FontProperties(fname=font_path).get_name()
    plt.rc("font",family=font_name)

    # font_list=[f.name for f in font_manager.fontManager.ttflist if "Nanum" in f.name or "Gothic" in f.name]

    # if font_list : 
    #     plt.rcParams['font.family']=font_list[0]
    # plt.rcParams['axes.unicode_minus']=False

    plt.figure()

    plt.plot(df['month'],df['total_sales_krw'],marker='o')
    plt.title("월별 매출추이")
    plt.xlabel("날짜")
    plt.ylabel("금액")

    plt.tight_layout()

    plt.show()
