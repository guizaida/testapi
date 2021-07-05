import requests,winreg,zipfile,re,os
url='http://npm.taobao.org/mirrors/chromedriver/' # chromedriver download link

def get_Chrome_version():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Google\Chrome\BLBeacon')
    version, types = winreg.QueryValueEx(key, 'version')
    return version

def get_latest_version(url):
    '''查詢最新的Chromedriver版本'''
    rep = requests.get(url).text
    time_list = []                                          # 用來存放版本時間
    time_version_dict = {}                                  # 用來存放版本與時間對應關係
    result = re.compile(r'\d.*?/</a>.*?Z').findall(rep)     # 匹配文件夾（版本號）和時間
    for i in result:
        time = i[-24:-1]                                    # 提取時間
        version = re.compile(r'.*?/').findall(i)[0]         # 提取版本號
        time_version_dict[time] = version                   # 構建時間和版本號的對應關係，形成字典
        time_list.append(time)                              # 形成時間列表
    latest_version = time_version_dict[max(time_list)][:-1] # 用最大（新）時間去字典中獲取最新的版本號
    return latest_version

def get_server_chrome_versions():
    '''return all versions list'''
    versionList=[]
    url="http://npm.taobao.org/mirrors/chromedriver/"
    rep = requests.get(url).text
    result = re.compile(r'\d.*?/</a>.*?Z').findall(rep)
    for i in result:                                 # 提取時間
        version = re.compile(r'.*?/').findall(i)[0]         # 提取版本號
        versionList.append(version[:-1])                  # 將所有版本存入列表
    return versionList


def download_driver(download_url):
    '''下載文件'''
    file = requests.get(download_url)
    with open("chromedriver.zip", 'wb') as zip_file:        # 保存文件到腳本所在目錄
        zip_file.write(file.content)
        print('下載成功')

def get_version():
    '''查詢系統內的Chromedriver版本'''
    outstd2 = os.popen('chromedriver --version').read()
    return outstd2.split(' ')[1]


def unzip_driver(path):
    '''解壓Chromedriver壓縮包到指定目錄'''
    f = zipfile.ZipFile("chromedriver.zip",'r')
    for file in f.namelist():
        f.extract(file, path)
def get_path(): 
    outstd1 = os.popen('where chromedriver').read() 
    fpath, fname = os.path.split(outstd1) 
    return fpath
def check_update_chromedriver():
    chromeVersion=get_Chrome_version()
    chrome_main_version=int(chromeVersion.split(".")[0]) # chrome主版本號
    driverVersion=get_version()
    driver_main_version=int(driverVersion.split(".")[0]) # chromedriver主版本號
    download_url=""
    if driver_main_version!=chrome_main_version:
        print("chromedriver版本與chrome瀏覽器不兼容，更新中>>>")
        versionList=get_server_chrome_versions()
        if chromeVersion in versionList:
            download_url=f"{url}{chromeVersion}/chromedriver_win32.zip"
        else:
            for version in versionList:
                if version.startswith(str(chrome_main_version)):
                    download_url=f"{url}{version}/chromedriver_win32.zip"
                    break
            if download_url=="":
                print("暫無法找到與chrome兼容的chromedriver版本，請在http://npm.taobao.org/mirrors/chromedriver/ 覈實。")

        download_driver(download_url=download_url)
        path = get_path()
        unzip_driver(path)
        os.remove("chromedriver.zip")
        print('更新後的Chromedriver版本爲：', get_version())
    else:
       print("Chromedriver版本與Chrome瀏覽器相兼容，無需更新Chromedriver版本！") 

if __name__=="__main__":
    check_update_chromedriver()