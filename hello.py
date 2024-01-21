from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.mangago.me/home/mangalist/661772/")

#driver.implicitly_wait(5)

title_classes = driver.find_elements(By.XPATH,"//div[@class='mangalist_item']")
title_list = []
for titles in title_classes:

    link=titles.find_element(By.XPATH,".//a[@class='left']").get_attribute("href")
    name=titles.find_element(By.XPATH,".//h3[@class='title']/a").text
    ratings = titles.find_element(By.XPATH,".//div[@style='display:inline-block']/span]").text
    title_list.append((name,link,ratings))
    # info = driver.find_element(By.XPATH,".//div[@class='info']")
    # print(info.find_element(By.XPATH,".//div[@style='display:inline-block']/span[@style='color:#FBFA7C;line-height:16px']").text)


# for i in range(2,21):
#     driver.find_element(By.XPATH,"//a[@title='Page "+str(i)+"']").click()
#     title_classes = driver.find_elements(By.XPATH,"//div[@class='mangalist_item']")
#     for titles in title_classes:
#         link=titles.find_element(By.XPATH,".//a[@class='left']").get_attribute("href")
#         name=titles.find_element(By.XPATH,".//h3[@class='title']/a").text
#         title_list.append((name,link))

for item in title_list:
    print(item)
#driver.implicitly_wait(10)
# p=p.get_attribute("href")
