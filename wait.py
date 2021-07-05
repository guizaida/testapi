from selenium import webdriver  
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By
import time
from threading import Thread
import ChromeDriverAutoUpdata as cdaup
def seleniumpage(url):
    globals()['driver'] = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)
    locator=(By.XPATH,'//*[@id="banner-blm"]/h3/a[2]')
    WebDriverWait(driver,10,1).until(EC.presence_of_element_located(locator))
def pythonpage(url):
    globals()['driver1'] = webdriver.Chrome("./chromedriver.exe")
    driver1.get(url)
    locator=(By.XPATH,'//*[@id="dive-into-python"]/ol/li[1]/a')
    WebDriverWait(driver1,10,1).until(EC.presence_of_element_located(locator))
def pypipage(url):
    globals()['driver2'] = webdriver.Chrome("./chromedriver.exe")
    driver2.get(url)
    locator=(By.XPATH,'//*[@id="introduction"]/table/tbody/tr[1]/td[2]/a')
    WebDriverWait(driver2,10,1).until(EC.presence_of_element_located(locator))
def driverquit():
    driver.quit()
    driver1.quit()
    driver2.quit()
def run():
    time_start=time.time()
    cdaup.check_update_chromedriver()
    ThreadA=[]
    ThreadB=[]
    ThreadC=[]
    url=['https://www.selenium.dev/','https://www.python.org/','https://pypi.org/project/selenium/']
    for i in range(1):
        ThreadA.append(Thread(target = seleniumpage,args=(url[0],)))
        ThreadB.append(Thread(target = pythonpage,args=(url[1],)))
        ThreadC.append(Thread(target = pypipage,args=(url[2],)))
        ThreadA[i].start()
        ThreadB[i].start()
        ThreadC[i].start()
    for i in range(1):
        ThreadA[i].join()
        ThreadB[i].join()
        ThreadC[i].join()
    for i in range(10):
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S ", localtime)
        print(result)
        time.sleep(1)
    driverquit()
    time_end=time.time()
    time_c=time_end-time_start
    print("執行時間：%f 秒" % (time_c))

if __name__ == '__main__':
    run()
