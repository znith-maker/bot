from selenium import webdriver
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://youtu.be/aWyg3xeo8C0")
print(driver.title)
i = 1
while i < 3:
    time.sleep(30)
    driver.refresh()
# driver.quit()