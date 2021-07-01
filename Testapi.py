import requests
import json
import time

def Postchack(i,url):
    try:
        datas={
            "song": "song"+str(i),
            "singer": "singer"+str(i)
        }
        headers={'Content-Type':'application/json'}
        updata=requests.post(url=url,headers=headers,data=json.dumps(datas))
        data = requests.get(url=url).text
        DataNo = json.loads(data)
        if DataNo['song'] == "song"+str(i):
            if DataNo['singer'] == "singer"+str(i):
                print('更新資料正常')
        else:
            print('更新資料異常,請確認資料格式是否有誤,或者資料庫是否正常運行')
    except:
        pass
def Getdata(url):
    try:
        data = requests.get(url=url).text
        DataNo = json.loads(data)
        if DataNo == []:
            print('回傳資料為空,請確認資料來源')
        else:
            print(DataNo)
    except:
        pass
def Definite_time_run(url):
    while True:
        Getdata(url)
        time.sleep(30)#間隔30秒執行一次get
def Fixed_time_run(url,Start_time):
    status = False
    while status != True:
        localtime = time.localtime()  # 讀取電腦時間
        result = time.strftime("%I:%M:%S", localtime)  # 時間顯示方式
        if result == Start_time:
            status = True
            Getdata(url)
            break
Start_time=input('請輸入啟動時間:')
url = "http://127.0.0.1:8000/api/musics/"

