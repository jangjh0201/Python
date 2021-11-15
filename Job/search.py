from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil


import schedule


def getDriver(url):
    def onDebugger (options, debugger):
        if debugger == True:
            try:
                shutil.rmtree(r"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
            except FileNotFoundError:
                pass
            subprocess.Popen(
                r'C:/Program Files (x86)/Google\Chrome/Application/chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/chrometemp"')  # 디버거 크롬 구동
            options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        else:
            options.add_argument('--headless')
        return options

    options = Options()
    options = onDebugger(options, True)
    # options.add_argument("--proxy-server=socks5://127.0.0.1:9050")
    
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

    try:
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)
    driver.implicitly_wait(10)

    driver.get(url)
    return driver

def getData(driver):
    time = driver.find_element_by_xpath('//*[@id="app"]/div/main/div/section/section[1]/div[1]/div[1]/span').text
    print(time)
    for i in range(1, 3):
        for j in range(1, 6):
            num = driver.find_element_by_xpath(f'//*[@id="app"]/div/main/div/section/section[1]/div[2]/div[{i}]/div[{j}]/a/span[1]').text
            text = driver.find_element_by_xpath(f'//*[@id="app"]/div/main/div/section/section[1]/div[2]/div[{i}]/div[{j}]/a/span[2]').text
            print(num," : ", text)

if __name__ == '__main__':
    url = 'http://icanhazip.com/'
    driver = getDriver(url)
    print(driver.page_source)

    driver.quit()
    # getData(driver)
    # schedule.every(10).minutes.do(getData, driver)
    # while True:
    #     schedule.run_pending()