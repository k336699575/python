# dic={"a":3,"x":5}
# for key in dic:
#     print(key)
#     print(dic[key])
# result=max([10,5,30,100])
# print(result)
# result=max("xaz")
# print(result)
# result=max({10,200,30,1})
# print(result)
# result=max({"x":3,"a":4})
# print(result)
# sorted(內建由小到大排序)
# result=sorted("cba")
# print(result)
# result=sorted({-5,10,200,-7})
# print(result)
#建立生成器函式 (yield)
# def test():
#     print("階段一")
#     yield 9
#     print("階段二")
#     yield 20
# #呼叫並回傳生成器    
# gen=test()
# #搭配 for 迴圈使用
# for d in gen:
#     print(d)    
# def even (maxnumber):#設定一個最大數字停止迴圈執行
#     number=0
#     while number<=maxnumber:
#         yield number
#         number+=3

# gen=even(100)
# for data in gen:
#      print(data)        
# def add(n1,n2,cb):
#     cb(n1+n2)
# def handle(result):
#     print("結果是",result)
# def handle2(result):
#     print("Result of Add is",result)    

# add(3,4,handle)    
# add(5,7,handle)
# add(2,9,handle2 )
def time():
    for i in range(1,10):
     for c in range(1,10):
       print("%1dX%1d=%d" %(i,c,i*c),end=" ")
    print()
time()            