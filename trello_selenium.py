# testgeorge870126@gmail.com
# ttest870126

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

action = ActionChains(driver)

# 使用WebDriver開始瀏覽器會話
driver.get("https://trello.com/")

time.sleep(1)

# 在這裡添加更多網頁自動化操作...
# 打開trello網頁並進入登入介面
driver.find_element(By.CSS_SELECTOR, ".Buttonsstyles__Button-sc-1jwidxo-0").click()

# 等待時間
driver.implicitly_wait(10)

# 輸入帳號
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("testgeorge870126@gmail.com")

# 等待時間
driver.implicitly_wait(10)

# 輸入密碼
driver.find_element(By.CSS_SELECTOR, ".css-178ag6o").click()
driver.implicitly_wait(10)
driver.find_element(By.ID, "password").send_keys("ttest870126")
driver.implicitly_wait(10)

# 登入
driver.find_element(By.CSS_SELECTOR, ".css-178ag6o").click()
driver.implicitly_wait(10)

# 建立看板
driver.find_element(By.CSS_SELECTOR, ".board-tile").click()
driver.find_element(By.CSS_SELECTOR, ".nch-textfield__input").send_keys("test")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".hY6kPzdkHFJhfG").click()
driver.implicitly_wait(10)

# 新增列表
driver.find_element(By.CSS_SELECTOR, ".frrHNIWnTojsww.CSwccJ0PrMROzz").click()
elemL = driver.find_element(By.CSS_SELECTOR, ".oe8RymzptORQ7h")
elemL.send_keys("hello1")
driver.implicitly_wait(10)
elemL.send_keys(Keys.ENTER)
driver.implicitly_wait(10)

# 新增卡片
driver.find_element(By.CSS_SELECTOR, ".O9vivwyDxMqo3q.bxgKMAm3lq5BpA").click()
elemC = driver.find_element(By.CSS_SELECTOR, ".qJv26NWQGVKzI9")
elemC.send_keys("card1")
driver.implicitly_wait(10)
elemC.send_keys(Keys.ENTER)
time.sleep(2)

# 複製卡片到hello列表
driver.find_element(By.CSS_SELECTOR, ".x7x105F0Ex0A7R.bxgKMAm3lq5BpA").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//*[@id='chrome-container']/div[4]/div/div[2]/div/div/div/ul[2]/li[1]/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='chrome-container']/div[4]/div/div[2]/div/div/div/form/ul/li[4]/a").click()
time.sleep(2)

# 更改名稱part1,對名稱點擊左鍵
changeName = driver.find_element(By.CSS_SELECTOR, ".NdQKKfeqJDDdX3")
action.context_click(changeName).perform()

# 更改名稱park2,輸入新名稱
elemN = driver.find_element(By.CSS_SELECTOR, ".rZbD0IuG2SfEkv")
elemN.send_keys("updateCard")
elemN.send_keys(Keys.ENTER)
time.sleep(2)

# 拖移目標到新位置
moveCard = driver.find_element(By.CSS_SELECTOR, ".amUfYqLTZOvGsn")
newList = driver.find_element(By.XPATH, '//*[@id="board"]/li[3]/div/div[3]/button[1]')
action.drag_and_drop(moveCard, newList).perform()

# 更改最後位置的列表名稱
lestName = driver.find_element(By.XPATH, '//*[@id="board"]/li[3]/div/div[1]/div/h2')
listName = driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="完成"].XmUgdJ5MepKUCB')
lestName.click()
listName.send_keys("final")
listName.send_keys(Keys.ENTER)

# 刪除卡片先定位在刪除
card = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="card-name"].NdQKKfeqJDDdX3')
action.context_click(card).perform()
deleteCard = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="quick-card-editor-archive"].BppQGb2j7TfyB5')
deleteCard.click()


# 刪除列表
driver.find_element(By.XPATH, '//*[@id="board"]/li[3]/div/div[1]/button').click()
driver.find_element(By.XPATH, '//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/ul[3]/li/a').click()

# 刪除看板
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div[1]/div/span[2]/button[2]').click()
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[2]/div/div/div/div[2]/div/ul/li[17]/a').click()
driver.find_element(By.XPATH, '//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/input').click()
# 關閉瀏覽器
time.sleep(3)
driver.quit()