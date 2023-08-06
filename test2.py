name = input("請輸入姓名:")
age = int(input("請輸入年齡:"))
if age >= 60:
     print("你已達退休年齡!")
elif age < 60:
    print(f'距離你退休年齡還有: {60 - age} 年')

