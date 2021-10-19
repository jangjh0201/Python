from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import pyperclip

import schedule

class Mail:
    def __init__(self, url):
        self.url = url
        self.driver = None
    def getDriver(self):
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
        

        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

        try:
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)
        except:
            chromedriver_autoinstaller.install(True)
            driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=options)
        driver.implicitly_wait(10)

        driver.get(self.url)
        self.driver = driver

    def login(self):
        def clipInput(self, user_xpath, user_input):
                temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

                pyperclip.copy(user_input)
                self.driver.find_element_by_xpath(user_xpath).click()
                ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

                pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴

        login = {
            "id": "jangjh0201@gmail.com",
            "pw": "jangjh7917"
        }
        clipInput(self, '//*[@id="identifierId"]', login.get("id"))
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
        self.driver.implicitly_wait(20)

        clipInput(self, '//*[@id="password"]/div[1]/div/div[1]/input', login.get("pw"))
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/').click()
        self.driver.implicitly_wait(20)

    def getData(self):
        time = self.driver.find_element_by_xpath('//*[@id="app"]/div/main/div/section/section[1]/div[1]/div[1]/span').text
        print(time)
        for i in range(1, 3):
            for j in range(1, 6):
                num = self.driver.find_element_by_xpath(f'//*[@id="app"]/div/main/div/section/section[1]/div[2]/div[{i}]/div[{j}]/a/span[1]').text
                text = self.driver.find_element_by_xpath(f'//*[@id="app"]/div/main/div/section/section[1]/div[2]/div[{i}]/div[{j}]/a/span[2]').text
                print(num," : ", text)

if __name__ == '__main__':
    url = 'https://mail.google.com/mail/u/0/#search/from%3Agoogle+label%3Aunread'
    mail = Mail(url)
    mail.getDriver()
    mail.login()
    # getData(driver)
    # schedule.every(10).minutes.do(getData, driver)
    # while True:
    #     schedule.run_pending()