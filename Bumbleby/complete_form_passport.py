import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)

#open site
driver.get("https://qa.neapro.site/login/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys('natalia.gvozdikova@gmail.com')
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys('10101029')
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(4)
#Fill Pasport
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()

driver.find_element(By.ID, "surname").clear()
time.sleep(1)
driver.find_element(By.ID, "surname").send_keys("Мещерская")

driver.find_element(By.ID, "name").clear()
time.sleep(1)
driver.find_element(By.ID, "name").send_keys("Ольга")

driver.find_element(By.ID, "patronymic").clear()
time.sleep(1)
driver.find_element(By.ID, "patronymic").send_keys("Владимировна")

driver.find_element(By.ID, "birthday").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".mx-date-row:nth-child(2) > .cell:nth-child(4)").click()

driver.find_element(By.ID, "passportSeries").clear()
time.sleep(1)
driver.find_element(By.ID, "passportSeries").send_keys("9410")

driver.find_element(By.ID, "passportNumber").clear()
time.sleep(2)
driver.find_element(By.ID, "passportNumber").send_keys("118343")

driver.find_element(By.ID, "dateOfIssue").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".mx-date-row:nth-child(5) > .cell:nth-child(3)").click()

driver.find_element(By.ID, "code").clear()
time.sleep(2)
driver.find_element(By.ID, "code").send_keys("003080")

driver.find_element(By.ID, "cardId").clear()
time.sleep(2)
driver.find_element(By.ID, "cardId").send_keys("12312312312")

driver.find_element(By.ID, "issued").clear()
time.sleep(2)
driver.find_element(By.ID, "issued").send_keys("Отделом УФМС России по УР в Устиновском районе гор. Ижевска")

driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys(Keys.CONTROL+"a")
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("г Ижевск, ул Академика Павлова, д 43 кв 141")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".vue-dadata__suggestions-item").click()

driver.find_element(By.ID, "phone").clear()
time.sleep(2)
driver.find_element(By.ID, "phone").send_keys("9054894754")

driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys("C:\\Test\\2022-09-27_1.jpg")
driver.execute_script("window.scrollTo(0, 1080)")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".fill").click()






