# import pandas as pd
# data=pd.Series([5,4,3,-1,6],index=["a","b","c","d","e"])
# print("資料的索引",data.index)
# print("資料的型態",data.dtype)
# print("資料的數量",data.size)
# print("最大值",data.max())
# print("總和",data.sum())
# print("標準差",data.std())
# print("中位數",data.median())
# print("最大的三位數",data.nlargest(3))
# data=pd.Series(["您好","Python","Pandas"])
# print(data.str.lower())#全部變小寫,中文不改變
# print(data.str.len())#字串長度
# print(data.str.cat(sep="'"))#把字串串起來,可以自訂串接的符號
# print(data.str.contains("好"))#判斷每個字串是否包含特定的字元
# print(data.str.replace("您好","Hello"))#取代字串
# data=pd.DataFrame({
#     "name":["Amy","Bob","Tom"],
#     "salary":[30000,50000,70000]
# },index=["a","b","c"])
# print(data)
# print("============================")
# print("取得第二列",data.iloc[1], sep="\n")
# print("============================")
# print("取得第c列",data.loc["c"],sep="\n")
# print("取得name欄位",data["name"],sep="\n")
# names=data["name"]
# print("把name全部變大寫",names.str.upper(),sep="\n")
# salaries=data["salary"]
# data["revenue"]=[300001,500001,700001] #data[新欄位的名稱]
# data["CC"]=["rr","qq","dd"]
# data["rank"]=pd.Series([3,6,9],index=["a","b","c"])
# data["cp"]=data["revenue"]/data["salary"]
# print(data)
# data=pd.Series([30,15,20])
# contition=data>18
# print(contition)
# condition=[True,False,True]
# filteredData=data[condition]
# print(filteredData)
# data=pd.Series(["您好","Python","Pandas"])
# condition=data.str.contains("P")
# print(condition)
# filteredData=data[condition]
# print(filteredData)
# data=pd.DataFrame({
#     "name":["Amy","Bob","Tom"],
#     "salary":[30000,50000,40000]
# })
# # print(data)
# con=data["name"]=="Amy"
# print(con)
# fil=data[con]
# print(fil)
# data=pd.read_csv("googleplaystore.csv")
# print("資料數量",data.shape)
# print(" 資料欄位",data.columns)
# print("=====================================")
#分析資料:評分的各種統計數據
# cc=data["Rating"]<=5
# data=data[cc]
# print("平均數",data["Rating"].mean())
# print("中位數",data["Rating"].median())
# print("取得前1000個應用程式的平均數",data["Rating"].nlargest(1000).mean())
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[, +]"," ").replace("Free"," "))
# print(data["Installs"])
# keyword=input("請輸入關鍵字:")
# con=data["App"].str.contains(keyword,case=False)#case=False(忽略大小寫)
# print("包含關鍵字的應用程式數量",data[con].shape[0])
import email.message
msg=email.message.EmailMessage()
msg["From"]="k606090857@gmail.com"
msg["To"]="k606090857@gmail.com"
msg["Subject"]="你好.澎澎"
msg.set_content("測試看看")
import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("k606090857@gmail.com","B00705ap")
server.send_message(msg)
server.close()