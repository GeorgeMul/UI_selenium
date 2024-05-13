# testgeorge870126@gmail.com
# ttest870126

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 使用WebDriver開始瀏覽器會話
driver.get("https://trello.com/")

time.sleep(1)

# 在這裡添加更多網頁自動化操作...
# 打開trello網頁並進入登入介面
driver.find_element(By.CLASS_NAME, "Buttonsstyles__Button-sc-1jwidxo-0").click()

# 等待時間
driver.implicitly_wait(10)

# 輸入帳號
driver.find_element(By.ID, "username").send_keys("testgeorge870126@gmail.com")

# 等待時間
driver.implicitly_wait(10)

# 輸入密碼
driver.find_element(By.CLASS_NAME, "css-178ag6o").click()
driver.implicitly_wait(10)
driver.find_element(By.ID, "password").send_keys("ttest870126")
driver.implicitly_wait(10)

# 登入
driver.find_element(By.CLASS_NAME, "css-178ag6o").click()


time.sleep(10)
# 關閉瀏覽器
driver.quit()