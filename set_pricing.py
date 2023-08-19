# 代匯公式:   代購價 ＝ (商品價格*代匯匯費＋包裝費(10~50)＋運輸（國際）)*代購服務費 
# (代匯不會有匯率)   
# 常變變數:
#  商品價格
#  運輸(國際)

# 少變變數:
#  包裝費(30)
#  匯率:1:1
#  代匯匯費:10%
#  代購服務費:10%

# --------------------------------------------------------------------------------
# 刷卡公式 : 代購價 ＝ (商品價格*信用卡手續費*匯率＋包裝費(30)＋運輸（國際) )*代購服務費 
# 常變變數:
#  商品價格
#  運輸(國際)

# 少變變數:
#  包裝費(30)
#  匯率:1:1
#  刷卡手續費:1.5%
#  代購服務費:10%

import json

with open('parameter.json') as f:
    data = json.load(f)
parameter = list(data.keys())
value = list(data.values())
# for i in range(len(parameter)):
#     print(i,"->",parameter[i],":",value[i])
    # 0 包裝費 ->"package": 30,
    # 1 匯率 -> "exchange_rate": 1,
    # 2 服務費 -> "service_fee": 1.1,
    # 3 代匯匯費 ->"Remittance_fee": 1.1,
    # 4 信用卡費 -> "card_fee": 1.015
#  代匯公式:   代購價 ＝ (商品價格*代匯匯費＋包裝費(10~50)＋運輸（國際）)*代購服務費
# 刷卡公式 : 代購價 ＝ (商品價格*信用卡手續費*匯率＋包裝費(30)＋運輸（國際) )*代購服務費
mode=int(input("若是代匯請輸入1，刷卡請輸入2:"))
price_orig=int(input("請輸入商品原先價錢:"))
delivery_fee=int(input("國際運費:"))
if mode==1:
    selling_price=(price_orig*value[3]+value[0]+delivery_fee)*value[2]
    # print(" 代購價＝(商品價格*代匯匯費＋包裝費(10~50)＋運輸（國際）)*代購服務費=",selling_price)
    print("代購價＝(商品價格(",price_orig,")*",parameter[3],"(",value[3],")+",parameter[0],"(",value[0],")＋國際運費(",delivery_fee,"))*",parameter[2],"(",value[2],")=",selling_price)
    print("(",price_orig,"*",value[3],"+",value[0],"+",delivery_fee,")*",value[2],"=",selling_price)
elif mode==2:
    selling_price=(price_orig*value[4]*value[1]+value[0]+delivery_fee)*value[2]
    # 刷卡公式 : 代購價 ＝ (商品價格*信用卡手續費*匯率＋包裝費(30)＋運輸（國際) )*代購服務費
    print("代購價＝(商品價格(",price_orig,")*",parameter[4],"(",value[4],")*",parameter[1],"(",value[1],")+",parameter[0],"(",value[0],")＋國際運費(",delivery_fee,"))*",parameter[2],"(",value[2],")=",selling_price)
    print("(",price_orig,"*",value[4],"*",value[1],"+",value[0],"+",delivery_fee,")*",value[2],"=",selling_price)
else:
    print("上述參數有誤，請確認")
    
