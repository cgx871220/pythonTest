from selenium import webdriver              #webdriver
from selenium.webdriver.common.by import By #By
from datetime import datetime               #現在時間
import time                                 #短暫暫停使用


driver = webdriver.Chrome()
driver.get("https://disp.cc/b/main")

time.sleep(1)
a_text = driver.find_elements(By.CSS_SELECTOR, '.ht_title a') 



# btn.click()  or tag.send_keys(keys.ENTER)
with open('save.txt',mode="a",encoding='utf-8') as file:
    file.write("現在時間")
    file.write(str(datetime.now()))
    file.write("\n")
    for i in a_text:
        file.write(i.text)
        file.write('\n')
    file.write("\n")
print('請按任意鍵結束')
