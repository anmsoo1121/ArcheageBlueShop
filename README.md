# ArcheageBlueShop
Python archeage blueShop

20.04.07 추가<br> 
-1,2,3단계 염료 제작 갯수 추가-<br>

20.04.08 추가<br>
-이미지 추가 및 랜덤요소 추가<br>
※!염료 검색시 염료 이미지는 랜덤으로 생성<br>

20.05.13 추가<br>
-열쇠 제작법 추가<br>
-로또 번호 기능추가<br>
-김가네 장점 크롤링 추가<br>

20.05.21<br>
-패피 출석 자동화 기능 추가<br>

20.06 추가 예정<br>
 - 채권 이미지 저장 후 불러오기 식으로 변경

import pyautogui

screenWidth, screenHeigt = pyautogui.size()
print('{0},{1}'.format(screenWidth, screenHeigt))

currentMouseX, currentMouseY = pyautogui.position()
print('{0},{1}'.format(currentMouseX, currentMouseY))
