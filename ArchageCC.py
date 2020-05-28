from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.chrome.options import Options
import time
import requests
import pyautogui

# driver.get('https://archeage.xlgames.com/play/worldinfo/GARDEN')
driver = webdriver.Chrome('C:/Users/descenteuser/AppData/Local/Programs/Python/chromedriver.exe')

driver.get('https://search.naver.com/search.naver?ie=UTF-8&query=%EC%95%84%ED%82%A4%EC%97%90%EC%9D%B4%EC%A7%80&sm=chr_hty')


driver.find_element_by_xpath('//*[@id="main_pack"]/div[2]/div[2]/div[1]/div[2]/div[2]/dl[1]/dd[3]/a[1]').click()
print(driver.window_handles)
driver.get('https://member.xlgames.com/user/login/form?forwardUrl=https://archeage.xlgames.com/')
driver.switch_to.window(driver.window_handles[1])
driver.close()

driver.switch_to.window(driver.window_handles[0])

driver.find_element_by_name('j_username').send_keys('#')
driver.find_element_by_name('j_password').send_keys('#')

driver.find_element_by_xpath('//*[@id="loginButton"]').click()

time.sleep(2)

driver.get('https://archeage.xlgames.com/promotions/2020/05/dice')
driver.find_element_by_xpath('//*[@id="dice-roll"]/button').click()

driver.get('https://archeage.xlgames.com/events/running/679')
 
driver.execute_script("window.scrollTo(0, 2500);")

pyautogui.click(x= 489, y= 493) #마우스 커서 위치 확인

driver.get('https://xlcash.xlgames.com/Web/Coupon/EnableList.aspx')

driver.find_element_by_xpath('//*[@id="characters"]').click()
driver.find_element_by_xpath('//*[@id="characters"]/option[7]').click() #캐릭터 선택확인(@정원)

driver.find_element_by_xpath('//*[@id="chbAll"]').click()
print("!!!!!!")
driver.find_element_by_xpath('//*[@id="container"]/div/section[3]/button').click()
print("######")				  

alert = driver.switch_to.alert
alert.accept()

driver.close()
