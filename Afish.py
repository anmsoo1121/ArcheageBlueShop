import os
import time
import pyautogui as pag
import cv2

#fish icon
#범위값 지정 (left,top,width,height)
fish_icon_pos = {20,215,880,450} #물고기 상태창 범위

#이미지 폴더에서 이미지 찾기
# ('D:\hs\python\OpenCv_image\left_move.jpg')

down_img = cv2.imread('D:\\hs\\python\\OpenCv_image\\down.jpg')
left_img = cv2.imread('D:\\hs\\python\\OpenCv_image\\left_move.jpg')
right_img = cv2.imread('D:\\hs\\python\\OpenCv_image\\right_move.jpg')
run_img = cv2.imread('D:\\hs\\python\\OpenCv_image\\run.jpg')
up_img = cv2.imread('D:\\hs\\python\\OpenCv_image\\up.jpg')



#fishing icon
#좌표값 지정 (x, y)
down_button = ()
left_button = ()
right_button = ()
run_button = ()
up_button = ()



# with mss.mss()as sct:
	# down_img = np.array(sct.grab(down_icon))[:,:,:3]
	# left_img = np.array(sct.grab(left_icon))[:,:,:3]
	# right_img = np.array(sct.grab(right_icon))[:,:,:3]
	# run_img = np.array(sct.grab(run_icon))[:,:,:3]
	# up_img = np.array(sct.grab(up_icon))[:,:,:3]
	
	# cv2.imshow('OpenCV/Numpy normal', np.concatenate((left_img, right_img), axis = 1))
	# cv2.waitkey(0)

while True:
	# x,y = pag.position()
	# position_str = 'X : ' + str(x) + 'Y : '+ str(y)
	# print(position_str)
	
	if fish_icon_pos == down_img:
		click(down_button)
	elif fish_icon_pos == left_img:
		click(left_button)
	elif fish_icon_pos == right_img:
		click(right_button)
	elif fish_icon_pos == run_img:
		click(run_button)
	elif fish_icon_pos == up_img:
		click(up_button)
	else:
		break
	
	
	
###############################
from selenium import webdriver
#import pyautogui
import discord


if message.content.startwith("!"):
    await message.channel.send(message.content[1:])

    userInput1 = message.content[1:]
    userInput2 = message.content[2,3:]
    userInput3 = message.content[4,5:]
    userInput4 = message.content[6,7:]

    userInput5 = message.content[8:]
    userInput6 = message.content[9,10:]
    userInput7 = message.content[11,12:]
    userInput8 = message.content[13,14:]

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get('http://archeve.co.kr/map.do')


#input key 0,1: 2,3: 4,5:



userInput1 = 'W'
userInput5 = 'S'

if userInput1 == userInput1:
    driver.find_element_by_xpath('//*[@id="we"]/option[1]').click()
else:
    driver.find_element_by_xpath('//*[@id="we"]/option[2]').click()

driver.find_element_by_id('horFst').send_keys(userInput2)
driver.find_element_by_id('horScd').send_keys(userInput3)
driver.find_element_by_id('horThd').send_keys(userInput4)

if userInput5 == userInput5:
    driver.find_element_by_xpath('//*[@id="sn"]/option[1]').click()
else:
    driver.find_element_by_xpath('//*[@id="sn"]/option[2]').click()

driver.find_element_by_id('verFst').send_keys(userInput6)
driver.find_element_by_id('verScd').send_keys(userInput7)
driver.find_element_by_id('verThd').send_keys(userInput8)

driver.find_element_by_xpath('//*[@id="floatingMenu"]/div[3]/button[3]').click()

#pyautogui.screenshot('TT.png', region=(20, 215, 880, 450))




#//*[@id="horFst"]
