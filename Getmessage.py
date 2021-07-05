import requests
import json
import time
def Getdata(url):
    try:
        data = requests.get(url=url)
        print(data)
        if str(data.status_code) == '200':
            DataNo = json.loads(data.text)
            if DataNo == []:
                print('回傳資料為空,請確認資料來源')
            else:
                for i in range(len(DataNo)):
                    datas=DataNo[i]
                    Alldata=[[],[]]
                    for key in datas.keys():
                        Alldata[0].append(key)
                    for value in datas.values():
                        Alldata[1].append(value)
                    with open('data'+str(i)+'.txt','w') as file:
                        for namber in range(len(Alldata[0])):
                            f=file.write(str(Alldata[0][namber])+':')
                            f=file.write(str(Alldata[1][namber])+'\n')
        else:
            print('連線失敗','錯誤代碼為:',data.status_code)
    except:
        pass
def run(url):
    time_start=time.time()
    Getdata(url)
    time_end=time.time()
    time_c=time_end-time_start
    print("執行時間：%f 秒" % (time_c))
url="http://127.0.0.1:8000/api/musics/"
if __name__ == '__main__':
    run(url)
