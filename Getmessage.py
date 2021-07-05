import requests
import json
import time
def Getdata(url):
    try:
        data = requests.get(url=url).text
        DataNo = json.loads(data)
        if DataNo == []:
            print('回傳資料為空,請確認資料來源')
        else:
            for i in range(len(DataNo)):
                datas=DataNo[i]
                Allkey=[]
                Allvalues=[]
                for key in datas.keys():
                    Allkey.append(key)
                for value in datas.values():
                    Allvalues.append(value)
                with open('data'+str(i)+'.txt','w') as file:
                    for namber in range(len(Allkey)):
                        f=file.write(str(Allkey[namber])+':')
                        f=file.write(str(Allvalues[namber])+'\n')
    except:
        pass
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
url="http://127.0.0.1:8000/api/musics/"
if __name__ == '__main__':
    time_start=time.time()
    Getdata(url)
    time_end=time.time()
    time_c=time_end-time_start
    print("執行時間：%f 秒" % (time_c))