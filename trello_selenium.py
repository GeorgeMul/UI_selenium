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
driver.implicitly_wait(10)

# 建立看板
driver.find_element(By.CLASS_NAME, "board-tile").click()
driver.find_element(By.CLASS_NAME, "nch-textfield__input").send_keys("test")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "hY6kPzdkHFJhfG").click()
driver.implicitly_wait(10)

# 新增列表
driver.find_element(By.CLASS_NAME, "frrHNIWnTojsww.CSwccJ0PrMROzz").click()
elemL = driver.find_element(By.CLASS_NAME, "oe8RymzptORQ7h")
elemL.send_keys("hello1")
driver.implicitly_wait(10)
elemL.send_keys(Keys.ENTER)
driver.implicitly_wait(10)

# 新增卡片
driver.find_element(By.CLASS_NAME, "O9vivwyDxMqo3q.bxgKMAm3lq5BpA").click()
elemC = driver.find_element(By.CLASS_NAME, "qJv26NWQGVKzI9")
elemC.send_keys("card1")
driver.implicitly_wait(10)
elemC.send_keys(Keys.ENTER)
time.sleep(2)

# 複製卡片到hello列表
driver.find_element(By.CLASS_NAME, "o0opcYgoysGMA4.bxgKMAm3lq5BpA").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "button[data-testid='quick-card-editor-move']").click()
time.sleep(5)

# 無法定位
driver.find_element(By.X, "js-autofocus").send_keys("card2")
driver.implicitly_wait(10)
elemU = driver.find_element(By.CLASS_NAME, "js-select-list")
driver.implicitly_wait(10)
elemU.click()
elemU.send_keys(Keys.DOWN)
elemU.send_keys(Keys.DOWN)
elemU.send_keys(Keys.DOWN)
elemU.send_keys(Keys.ENTER)
driver.find_element(By.CLASS_NAME, "nch-button").click()
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME, "css-snhnyn").click()

time.sleep(10)
# 關閉瀏覽器
driver.quit()