import discord
# from discord.ext.commands import Bot
# from discord.ext import commands
import asyncio
import requests
from bs4 import BeautifulSoup
import bs4
from urllib.request import urlopen, Request
import urllib
import urllib.request
import random



client = discord.Client()

@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("==================")
	await client.change_presence(status=discord.Status.online, activity=discord.Game("뭐가 뭔지모를땐 !도움 입력하세요."))
	# await client.change_resence(game=discord.Game(name="!도움"))
	

	
@client.event
async def on_message(message):
	if message.author.bot:
		return None
	
	id = str(message.author.id)
	channel = message.channel
		
	if message.content.startswith("!만든사람"):
		await message.channel.send("여울이")
	
	if message.content.startswith("!업데이트"):
		await message.channel.send("20.05.12 열쇠제작법 추가")
	
	if message.content.startswith("!보름돌"):
		await message.channel.send("<@" + id + "> ex)!불굴의 보름돌 이라고 입력하쇼")
		
	if message.content.startswith("!염료"):
		await message.channel.send("<@" + id + "> ex)!1단계 염료 22 라고 입력하쇼")
	
	if message.content.startswith("!수려한"):
		await message.channel.send("<@" + id + "> ex)갯수 입력 부탁드립니다. :D")

	if message.content.startswith("!계정"):
		userid = "#"
		userpw = "#"
		
		embed = discord.Embed(
			title = '김짜증 계정',
			description = '',
			colour = discord.Color.red()
		)
		print("id : " + userid + "입니다.")
		print("pw : " + userpw + "입니다.")
		
		embed.add_field(name = 'id', value = userid, inline = True)
		embed.add_field(name = 'pw', value = userpw, inline = True)
		
		await message.channel.send("계정", embed=embed)
	
	if message.content.startswith("!도움"):
	
		embed = discord.Embed(
			title="명령어",
			description="archeage 푸른소금상회 봇 명령어 모음입니다.", 
			color=0x62c1cc)
			
		embed.add_field(name="!채권", value="!채권 입력시 현재시간 기준 자원비축재료를 가져옵니다.", inline=False)
		embed.add_field(name="!수려한", value="수려한 초승돌 제작시 필요개수 표시해줍니다. ex)!수려한 7", inline=False)
		embed.add_field(name="!보름돌", value="불굴의 초월,사랑,추적,투지 보름돌 제작시 필요개수를 표시해줍니다.", inline=False)
		embed.add_field(name="!초승돌 강화", value="명점 초승돌 강화시 필요개수를 표시해줍니다.", inline=False)
		embed.add_field(name = "!캐리명", value="캐릭터의 장점을 표시합니다.", inline=False)
		embed.set_footer(text="경매장 검색은은 추후 업데이트 예정입니다.")
		
		print("!help")
		await message.channel.send("Hs", embed=embed)
		
		
	
	if message.content.startswith("!수려한"):
		await message.channel.send("수려한" + message.content[4:] + "개 만드는 재료")
			
		userInput = message.content[4:]
		n = int(userInput)		#수려한 n개
		
		StrengthIron = 40		#강도높은 주괴 = 40
		CrescenticCrystal = 70  #초승돌결정 = 70
		
		i = n * StrengthIron
		cc = n * CrescenticCrystal
		
		Blacklight = 3			#흑빛 아키움 정수 = 3
		Royalazalea = 20		#철쭉 = 20
		Narcissus = 20			#수선화 = 20
		Iron = 8				#철주괴 = 8
		IronOres = 40			#철광석 = 40
		Copper = 1				#구리 주괴 = 1
		CopperOres = 5			#구리 광석 = 5
		Silver = 1				#은괴 = 1
		SilverOres = 5			#은광석 = 5
		
		embed = discord.Embed(
			title = "초승돌 제작",
			description = "",
			colour = discord.Color.red()
		)
		
		embed.set_thumbnail(url="https://i.imgur.com/t3pHqis.jpg?1")
		embed.add_field(name = '수려한 초승돌', value = n, inline=False)
		embed.add_field(name = '초승돌 결정', value = cc, inline=False)
		embed.add_field(name = '강도높은주괴', value = StrengthIron * n, inline=False)
		embed.add_field(name = '흑빛아키움정수', value = Blacklight * i, inline=False)
		embed.add_field(name = '철쭉', value = Royalazalea * i, inline=True)
		embed.add_field(name = '수선화', value = Narcissus * i, inline=True)
		embed.add_field(name = '_', value = "_", inline=False)
		embed.add_field(name = '철주괴', value = Iron * i, inline=True)
		embed.add_field(name = '철광석', value = IronOres * i, inline=True)
		embed.add_field(name = '_', value = "_", inline=False)
		embed.add_field(name = '구리주괴', value = Copper * i, inline=True)
		embed.add_field(name = '구리광석', value = CopperOres * i, inline=True)
		embed.add_field(name = "_", value = "_", inline=False)
		embed.add_field(name = '은괴', value = Silver * i, inline=True)
		embed.add_field(name = '은광석', value = SilverOres * i, inline=True)
		
		print("수려한", n, "개")
		
		await message.channel.send(client, embed=embed)
		
	if message.content.startswith("!초승돌 강화"):
		await message.channel.send("초승돌 강화" + message.content[7:] + "개 만드는 재료")
		
		
		userInput = message.content[7:]
		n = int(userInput)
		
		
		CrescentStone2 = 2			#2단계 강화
		CrescenticCrystal2 = 3
		
		CrescentStone3 = 3			#3단계 강화
		CrescenticCrystal3 = 5
		
		CrescentStone4 = 4			#4단계 강화
		CrescenticCrystal4 = 8
		
		CrescentStone5 = 5			#5단계 강화
		CrescenticCrystal5 = 15
		
		CrescentStone6 = 6			#6단계 강화
		CrescenticCrystal6 = 20
		
		
		#초승돌 합 구하기
		C1 = CrescentStone2 + CrescentStone3 + CrescentStone4 + CrescentStone5 + CrescentStone6 	#초강합
		C2 = CrescenticCrystal2 + CrescenticCrystal3 + CrescenticCrystal4 + CrescenticCrystal5 + CrescenticCrystal6		#초결 합
		
		embed = discord.Embed(
			title = "초승돌 강화",
			description = "",
			colour = discord.Color.red()
		)
		
		embed.set_thumbnail(url='https://i.imgur.com/M1SGJIu.jpg')
		embed.add_field(name = '_', value = '_2단계_', inline=False)
		embed.add_field(name = '| 초승돌 강화석 1단계|', value = CrescentStone2 * n, inline=True)
		embed.add_field(name = '초승돌 결정', value = CrescenticCrystal2 * n, inline=True)
		embed.add_field(name = '_', value = '_3단계_', inline=False)
		embed.add_field(name = '| 초승돌 강화석 1단계|', value = CrescentStone3 * n, inline=True)
		embed.add_field(name = '초승돌 결정', value = CrescenticCrystal3 * n, inline=True)		
		embed.add_field(name = '_', value = '_4단계_', inline=False)
		embed.add_field(name = '| 초승돌 강화석 1단계|', value = CrescentStone4 * n, inline=True)
		embed.add_field(name = '초승돌 결정', value = CrescenticCrystal4 * n, inline=True)
		embed.add_field(name = '_', value = '_5단계_', inline=False)
		embed.add_field(name = '| 초승돌 강화석 1단계|', value = CrescentStone5 * n, inline=True)
		embed.add_field(name = '초승돌 결정', value = CrescenticCrystal5 * n, inline=True)		
		embed.add_field(name = '_', value = '_6단계_', inline=False)
		embed.add_field(name = '| 초승돌 강화석 1단계|', value = CrescentStone6 * n, inline=True)
		embed.add_field(name = '초승돌 결정', value = CrescenticCrystal6 * n, inline=True)
		embed.add_field(name = '_', value = '_총합_', inline=False)
		embed.add_field(name = '초승돌 강화석 합', value = C1 * n, inline=True)
		embed.add_field(name = '초승돌 결정 합', value = C2 * n, inline=True)
		
		
		await message.channel.send(client, embed=embed)
		
	if message.content.startswith("!불굴의 보름돌"):
			await message.channel.send("악세 보름돌" + message.content[8:] + "개 만드는 재료")
			
			userInput = message.content[8:]
			n = int(userInput)
			
			MoonEssence = 40	#신비한 달의 정수
			YardPowder = 50		#정원의 신비한 가루
			Dye = 10			#염료
			BlueCoral = 100		#푸른색 산호조각
			
			embed = discord.Embed(
				title = "보름돌 제작",
				description = "",
				colour = discord.Color.purple()
			)
			
			a = 'https://i.imgur.com/dAY4n0T.jpg' #투지
			b = 'https://i.imgur.com/UDQ4Wj6.jpg' #추적
			c = 'https://i.imgur.com/FknjgYv.jpg' #초월
			d = 'https://i.imgur.com/4XwQVeb.jpg' #사랑

			imgur = a, b, c, d
			
			random.choice(imgur)
			
			embed.set_thumbnail(url = random.choice(imgur))
			
			embed.add_field(name = '추적,투지 보름돌', value = n, inline=True)
			embed.add_field(name = '사랑,초월 보름돌', value = n, inline=True)
			embed.add_field(name = '신비한 달의 정수', value = n * MoonEssence, inline=False)
			embed.add_field(name = '정원의 신비한 가루', value = n * YardPowder, inline=False)
			embed.add_field(name = '투명한 가루가 섞인 기름', value = n * Dye, inline=True)
			embed.add_field(name = '부드러운 줄기 염료', value = n * Dye, inline=True)
			embed.add_field(name = '푸른색 산호조각', value = n * BlueCoral, inline=False)
			
			print("보름돌", n, "개")
			
			await message.channel.send(client, embed=embed)
			
	
		# """ 
		# 1,2,3 단계 염료
		# """
	
	if message.content.startswith("!1단계 염료"):
		await message.channel.send("1단계 염료,기름,연마제" + message.content[7:] + "개 만드는 재료")
		
		userInput = message.content[7:]
		n = int(userInput)
		
		Blacklight1 = 3		#1단계 흑빛아키움
		Blacklight2 = 5		#2단계 흑빛아키움
		Blacklight3 = 9		#3단계 흑빛아키움
		clover = 20			#1단계
		rose = 20			#1단계	
		peanut = 30			#2단계
		wheat = 30			#2단계
		RedCoral = 20 		#2단계
		bean = 40			#3단계
		rye = 40			#3단계
		pearl = 20			#3단계
		vanilla = 5			#3단계

		embed = discord.Embed(
			title = "염료제작",
			description = "",
			colour = discord.Color.red()
		)
		
		a  = 'https://i.imgur.com/Wmw8txM.jpg'	   #1_염료 
		b  = 'https://i.imgur.com/zjUsJCM.jpg'     #1_연마제
		c  = 'https://i.imgur.com/scFJwIb.jpg'     #1_기름
	
		imgur = a, b, c
		
		random.choice(imgur)
		
		embed.set_thumbnail(url = random.choice(imgur))
		
		embed.add_field(name = "1단계 염료", value = "잔뿌리 염료", inline=True)
		embed.add_field(name = "1단계 연마제", value = "불투명한 연마제", inline=True)
		embed.add_field(name = "1단계 기름", value = "조그만 씨눈 기름", inline=True)
		embed.add_field(name = "흑빛아키움 정수", value = Blacklight1 * n, inline=True)
		embed.add_field(name = "흑빛아키움 정수", value = Blacklight1 * n, inline=True)
		embed.add_field(name = "흑빛아키움 정수", value = Blacklight1 * n, inline=True)
		embed.add_field(name = "토끼풀", value = clover * n, inline=True)
		embed.add_field(name = "수선화", value = clover * n, inline=True)
		embed.add_field(name = "옥수수", value = clover * n, inline=True)
		embed.add_field(name = "장미", value = rose * n, inline=True)
		embed.add_field(name = "철쭉", value = rose * n, inline=True)
		embed.add_field(name = "쌀", value = rose * n, inline=True)
		embed.set_footer(text = '※이미지는 랜덤입니다.')
		
		print("1단계 염료", n , "개")
		
		await message.channel.send(client, embed=embed)
		
		
	if message.content.startswith("!2단계 염료"):
		await message.channel.send("2단게 염료,기름,연마제" + message.content[7:] + "개 만드는 재료")
		
		userInput = message.content[7:]
		n = int(userInput)
		
		
		Blacklight2 = 5		#2단계 흑빛아키움
		peanut = 30			#2단계
		wheat = 30			#2단계
		RedCoral = 20 		#2단계
		first = 1
			
		embed = discord.Embed(
			title = "염료제작",
			description = "",
			colour = discord.Color.red()
		)
		
		a = 'https://i.imgur.com/Wys4w0H.jpg' #2_연마제
		b = 'https://i.imgur.com/6qVN4mD.jpg' #2_염료
		c = 'https://i.imgur.com/vTjuami.jpg' #2_기름
		
		imgur = a, b, c
		
		random.choice(imgur)
	
		embed.set_thumbnail(url = random.choice(imgur))
		
		embed.add_field(name = "2단계 염료", value = "작은 잎사귀 염료", inline=True)
		embed.add_field(name = "2단계 연마제", value = "거친 입자의 연마제", inline=True)
		embed.add_field(name = "2단계 기름", value = "윤기 있는 진한 기름", inline=True)
		embed.add_field(name = "잔뿌리 염료", value = first * n, inline=True)
		embed.add_field(name = "불투명한 연마제", value = first * n, inline=True)
		embed.add_field(name = "조그만 씨눈 기름", value = first * n, inline=True)
		embed.add_field(name = "흑빛아키움 정수", value = Blacklight2 * n, inline=True)
		embed.add_field(name = "흑빛아키움 정수", value = Blacklight2 * n, inline=True)
		embed.add_field(name = "흑빛아키움 정수", value = Blacklight2 * n, inline=True)
		embed.add_field(name = "수레국화", value = peanut * n, inline=True)
		embed.add_field(name = "연꽃", value = peanut * n, inline=True)
		embed.add_field(name = "땅콩", value = peanut * n, inline=True)
		embed.add_field(name = "백합", value = wheat * n, inline=True)
		embed.add_field(name = "귀리", value = wheat * n, inline=True)
		embed.add_field(name = "밀", value = wheat * n, inline=True)
		embed.add_field(name = "녹색 산호초", value = RedCoral * n, inline=True)
		embed.add_field(name = "사슴뿔형 산호초", value = RedCoral * n, inline=True)
		embed.add_field(name = "붉은색 산호초", value = RedCoral * n, inline=True)
		embed.set_footer(text = '※이미지는 랜덤입니다.')
		print("2단계 염료", n , "개")
		
		await message.channel.send(client, embed=embed)	
		
		
	if message.content.startswith("!3단계 염료"):
		await message.channel.send("3단계 염료,기름,연마제" + message.content[7:] + "개 만드는 재료")
		
		userInput = message.content[7:]
		n = int(userInput)
		
		Blacklight3 = 9		#3단계 흑빛아키움
		bean = 40			#3단계
		rye = 40			#3단계
		pearl = 20			#3단계
		vanilla = 5			#3단계
		second = 1
		
		embed = discord.Embed(
			title = "염료제작",
			description = "",
			colour = discord.Color.red()
		)
		
		a = 'https://i.imgur.com/dVPMHSk.jpg'	#3_기름
		b = 'https://i.imgur.com/mr1nF8G.jpg'	#3_연마제
		c = 'https://i.imgur.com/WoS6dPm.jpg'	#3_염료
		
		imgur = a, b, c
		
		random.choice(imgur)
		
		embed.set_thumbnail(url = random.choice(imgur))
		
		
		embed.add_field(name = "3단계 염료", value = "부드러운 줄기 염료", inline=True)
		embed.add_field(name = "3단계 연마제", value = "끈적임 없는 연마제", inline=True)
		embed.add_field(name = "3단계 기름", value = "투명한 가루가 섞인 기름", inline=True)
		
		embed.add_field(name = "작은 잎사귀 염료", value = second * n, inline=True)
		embed.add_field(name = "거친 입자의 연마제", value = second * n, inline=True)
		embed.add_field(name = "윤기 있는 진한 기름", value = second * n, inline=True)
		
		embed.add_field(name = "흑빛아키움 정수", value = Blacklight3 * n, inline=True)
		embed.add_field(name = "흑빛아키움 정수", value = Blacklight3 * n, inline=True)
		embed.add_field(name = "흑빛아키움 정수", value = Blacklight3 * n, inline=True)
		
		embed.add_field(name = "선인장", value = bean * n, inline=True)
		embed.add_field(name = "고추", value = bean * n, inline=True)
		embed.add_field(name = "콩", value = bean * n, inline=True)
		
		embed.add_field(name = "박하", value = rye * n, inline=True)
		embed.add_field(name = "로즈마리", value = rye * n, inline=True)
		embed.add_field(name = "호밀", value = rye * n, inline=True)
		
		embed.add_field(name = "진주", value = pearl * n, inline=True)
		embed.add_field(name = "진주", value = pearl * n, inline=True)
		embed.add_field(name = "진주", value = pearl * n, inline=True)
		
		embed.add_field(name = "후추", value = vanilla * n, inline=True)
		embed.add_field(name = "블루베리", value = vanilla * n, inline=True)
		embed.add_field(name = "바닐라", value = vanilla * n, inline=True)

		print("3단계 염료", n , "개")
		
		await message.channel.send(client, embed=embed)
		
	if message.content.startswith("!열쇠"):
			#열쇠는 5개 씩
		userInput = message.content[4:]
		n = int(userInput)
		a = n * 5
		
		Copper = 1				#구리 주괴 = 1
		CopperOres = 5			#구리 광석 = 5
		Silver = 1				#은괴 = 1
		SilverOres = 5			#은광석 = 5
		Gold = 1				#금괴 = 1
		GoldOres = 5			#금광석 = 5
		

		CopperKey = Copper * 2
		CopperA = Copper * 0.6
		SilverA = Silver * 0.6
		GoldA = Gold * 3
		SilverKey = Silver * 2
		
		# SilverKey = CopperKey * (Copper * 0.6) * Silver
		# GoldKey =  SilverKey * Copper * (Silver * 0.6) * Gold * 3
		#2, 0.6, 1
		
		embed = discord.Embed(
			title = "열쇠",
			description = " ",
			colour = discord.Color.green()
		)
		
		embed.add_field(name = "구리열쇠", value = "아래 재료" , inline=False)
		embed.add_field(name = "구리주괴", value = CopperKey * a , inline=True)
		embed.add_field(name = "은열쇠" , value = "아래 재료" , inline=False)
		embed.add_field(name = "구리열쇠" , value = CopperKey * a , inline=True)
		embed.add_field(name = "구리주괴" , value = CopperA * a , inline=True)
		embed.add_field(name = "은괴" , value = Silver , inline=True)
		embed.add_field(name = "금열쇠" , value = "아래 재료" , inline=False)
		embed.add_field(name = "은열쇠" , value = SilverKey * a , inline=True)
		embed.add_field(name = "구리주괴" , value = Copper * a , inline=True)
		embed.add_field(name = "은괴" , value = SilverA * a , inline=True)
		embed.add_field(name = "금괴" , value = GoldA * a , inline=True)
		embed.set_footer(text="열쇠는 1 = 5 개입니다.")
		
		print("열쇠", a , "개")
		
		await message.channel.send(client, embed=embed)
		
		# """ 
		# 채권 탭
		# """
		
	if message.content.startswith("!채권"):
		
		embed = discord.Embed(
            title = "오늘의 채권",
            description = " ",
            colour= discord.Color.red()
        )
		hdr = {'User-Agent': 'Mozilla/5.0'}
		url = 'https://archeage.xlgames.com/play/worldinfo/GARDEN'
		print(url)
		req = Request(url, headers=hdr)
		html = urllib.request.urlopen(req)
		bsObj = bs4.BeautifulSoup(html, "html.parser")
		
		cornjs = bsObj.find('table', {'class': 'table-bond'})
		# cornjs3 = bsObj.select('li[class=point]')	#20개 포인트
		cornjsR = bsObj.find('table', {'class': 'table-bond right'})
		cornjs2 = cornjs.text
		cornjs4 = cornjsR.text
		# cornjs6 = cornjs3.text #20개 포인트
		
		embed.set_thumbnail(url="https://i.imgur.com/SD4k1fc.jpg")
		embed.add_field(name='대륙', value=cornjs2, inline=True)
		embed.add_field(name='대륙', value=cornjs4, inline=True)
		embed.set_footer(text="업데이트예정", icon_url="https://i.imgur.com/SD4k1fc.jpg")
		# embed.add_field(name='최소수량', value=cornjs6, inline=True) #20개 포인트
		await message.channel.send(client, embed=embed)		
			
		
		# """ 
		# 김가네 장점 가져오기
		# """
		
	if message.content.startswith("!김순딩"):
		
		embed = discord.Embed(
            title = "김가네 장점",
            description = " ",
            colour= discord.Color.red()
        )
		hdr = {'User-Agent': 'Mozilla/5.0'}
		 
		url = 'https://archeage.xlgames.com/characters/3CD2027B-C03A-4A48-979C-B320AE7C6A56' #김순딩
		print(url)
		
		req = Request(url, headers=hdr)
		html = urllib.request.urlopen(req)
		bsObj = bs4.BeautifulSoup(html, "html.parser")
		
		a = bsObj.select('.score')
		
		for score in a:
			print('김순딩' + score.text + '점')
		
		embed.set_thumbnail(url = 'https://i.imgur.com/ky4pgOY.jpg')
		embed.add_field(name = '김순딩', value = score.text + '점', inline = True)
		
		
		await message.channel.send(client, embed=embed)
		
		
	if message.content.startswith("!김짜증"):
	
		embed = discord.Embed(
			title = "김가네 장점",
			description = "",
			colour = discord.Color.red()
		)
		
		hdr = {'User-Agent': 'Mozilla/5.0'}
		
		url = 'https://archeage.xlgames.com/characters/F69B27C6-4798-490C-B50A-D4E459CCE8A5' #김짜증
		
		print(url)
		
		req = Request(url, headers=hdr)
		html = urllib.request.urlopen(req)
		bsObj = bs4.BeautifulSoup(html, "html.parser")
		
		a = bsObj.select('.score')
		
		for score in a:
			print('김짜증' + score.text + '점')	
		
		embed.set_thumbnail(url = 'https://i.imgur.com/QCn3HT5.png')
		embed.add_field(name = '김짜증', value = score.text + '점', inline = True)
		
		
		await message.channel.send(client, embed=embed)
		
	if message.content.startswith("!김버럭"):
	
		embed = discord.Embed(
			title = "김가네 장점",
			description = "",
			colour = discord.Color.red()
		)
		
		hdr = {'User-Agent': 'Mozilla/5.0'}
		
		url = 'https://archeage.xlgames.com/characters/3DDFB1A0-90AF-474F-AE26-D27F799D2679' #김버럭
		
		print(url)
		
		req = Request(url, headers=hdr)
		html = urllib.request.urlopen(req)
		bsObj = bs4.BeautifulSoup(html, "html.parser")
		
		a = bsObj.select('.score')
		
		for score in a:
			print('김버럭' + score.text + '점')	
		
		embed.set_thumbnail(url = 'https://i.imgur.com/5Licrh3.png')
		embed.add_field(name = '김버럭', value = score.text + '점', inline = True)
		
		
		await message.channel.send(client, embed=embed)
		
	if message.content.startswith("!김덤덤"):
	
		embed = discord.Embed(
			title = "김가네 장점",
			description = "",
			colour = discord.Color.red()
		)
		
		hdr = {'User-Agent': 'Mozilla/5.0'}
		
		url = 'https://archeage.xlgames.com/characters/8184B531-C3B9-4988-B987-13176949BBD5' #김덤덤
		
		print(url)
		
		req = Request(url, headers=hdr)
		html = urllib.request.urlopen(req)
		bsObj = bs4.BeautifulSoup(html, "html.parser")
		
		a = bsObj.select('.score')
		
		for score in a:
			print('김덤덤' + score.text + '점')	
		
		embed.set_thumbnail(url = 'https://i.imgur.com/8EfQtjD.jpg')
		embed.add_field(name = '김덤덤', value = score.text + '점', inline = True)
		
		
		await message.channel.send(client, embed=embed)
		
	if message.content.startswith("!김다정"):
	
		embed = discord.Embed(
			title = "김가네 장점",
			description = "",
			colour = discord.Color.red()
		)
		
		hdr = {'User-Agent': 'Mozilla/5.0'}
		
		url = 'https://archeage.xlgames.com/characters/02EF0662-5086-4910-95F2-E45C2B947778' #김다정
		
		print(url)
		
		req = Request(url, headers=hdr)
		html = urllib.request.urlopen(req)
		bsObj = bs4.BeautifulSoup(html, "html.parser")
		
		a = bsObj.select('.score')
		
		for score in a:
			print('김다정' + score.text + '점')	
		
		embed.set_thumbnail(url = 'https://i.imgur.com/rVgdqCI.jpg')
		embed.add_field(name = '김다정', value = score.text + '점', inline = True)
		
		
		await message.channel.send(client, embed=embed)
		
	if message.content.startswith("!로또"):
		# await message.channel.send("이시간 행운번호!")
			Text = ""
			number = [1, 2, 3, 4, 5, 6, 7]
			count = 0
			for i in range(0, 7):
				num = random.randrange(1, 46)
				number[i] = num
				if count >= 1:
					for i2 in range(0, i):
						if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
							numberText = number[i]
							print("작동 이전값 : " + str(numberText))
							number[i] = random.randrange(1, 46)
							numberText = number[i]
							print("작동 현재값 : " + str(numberText))
							if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
								numberText = number[i]
								print("작동 이전값 : " + str(numberText))
								number[i] = random.randrange(1, 46)
								numberText = number[i]
								print("작동 현재값 : " + str(numberText))
								if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
									numberText = number[i]
									print("작동 이전값 : " + str(numberText))
									number[i] = random.randrange(1, 46)
									numberText = number[i]
									print("작동 현재값 : " + str(numberText))
	
				count = count + 1
				Text = Text + "  " + str(number[i])
	
			print(Text.strip())
			embed = discord.Embed(
				title="오늘의 행운번호!",
				description=Text.strip(),
				colour=discord.Color.red()
			)
			await message.channel.send(client, embed=embed)
			
	if	message.content.startswith("!다나와"):
	
		Name = message.content[5:len(message.content)]
		# n = str(Name)
		
		# url = ("http://search.danawa.com/dsearch.php?query="+n)
		# print(url)
		
		req = requests.get("http://search.danawa.com/dsearch.php?query="+Name)
		print(req)
		html = req.text
		soup = BeautifulSoup(html, "html.parser")

		ram = soup.find('ul',{'class': 'product_list'})
		print(ram)
		# b = bsObj.find('a',{'class': 'click_log_product_standard_price_'})
		
		# c = a.text
		# d = b.text
		
		embed = discord.Embed(
			title = "다나와 검색",
			description = "",
			colour = discord.Color.red()
		)
		
		embed.add_field(name = "이름", value=ram, inline=True)
		# embed.add_field(name = "금액", value=b, inline=True)
		await message.channel.send(client, embed=embed)
		
		


client.run('#')
