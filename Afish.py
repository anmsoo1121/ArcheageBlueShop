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
	
