import csv
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'

plt.rcParams['axes.unicode_minus'] =False 
plt.rc('font', size=7)

f = open("C:\Lesson_Python\starbucks_suwon\data.csv")
data = csv.reader(f) # csv파일은 콤마로 구분
next(data) # 타이틀 안보이게 함

dong = ["영통동",
    "원천동",
    "망포동",
    "신동",
    "서둔동",
    "세류동",
    "권선동",
    "평동",
    "금곡동",
    "송죽동",
    "정자동",
    "율천동",
    "파장동",
    "연무동",
    "인계동",
    "우만동",
    "매산동"
    ]

customer_for_starbucks =[]
for row in data :
    if (row[4] != "") :
        customer_for_starbucks.append(float(row[4]))

plt.title("수원시 행정구역 별 스타벅스 지점에 할당된 인구")
plt.plot(dong, customer_for_starbucks)
plt.scatter(dong, customer_for_starbucks)
plt.show()
