import json

num=998
print("當前的值如下:")
print("--------------------------------")
with open('parameter.json') as f:
    data = json.load(f)
parameter = list(data.keys())
value = list(data.values())
for i in range(len(parameter)):
    print(i,'->',parameter[i],':',value[i])

while(num!=999):
    num=int(input("請輸入需要改的變數代號(0~4)，若無需變更請輸入999:"))
    if(num<5 and num>=0):
        print("需要改的變數:",data[parameter[num]])
        new_value=int(input("請輸入"+parameter[num]+"新的值:"))
        print(parameter[num],":",value[num],"->",new_value)
        data[parameter[num]]=new_value
        value[num]=new_value
    else:
        print("參數錯誤，請重新輸入")
print("修改後參數如下:")
print("--------------------------------")
for i in range(len(parameter)):
    print(i,'->',parameter[i],':',value[i])

with open('parameter.json','w') as f:
    json.dump(data,f,indent=2)