import discord
import asyncio
# import requests
# from bs4 import BeautifulSoup
from discord.ext import commands
import bs4
from urllib.request import urlopen, Request
import urllib
import urllib.request

client = discord.Client()

@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("@#@#@#@#@#@#@")
	
@client.event
async def on_message(message):
	if message.author.bot:
		return None
	
	id = str(message.author.id)
	channel = message.channel
		
	if message.content.startswith("!만든사람"):
		await message.channel.send("Hs")
		
	if message.content.startswith("!강해지는법"):
		await message.channel.send("<@" + id + "> 돈을쓰세요 :D")		
	
	if message.content.startswith("!일안하고 돈벌기"):
		await message.channel.send("<@" + id + "> 수저를 잘 물고 태어나셨어야죠 :D")	
	
	if message.content.startswith("!도움"):
		embed = discord.Embed(title="이건뭐죠?", description="archeage 푸른소금상회 채권봇입니다.", color=0x62c1cc)
		embed.add_field(name="왜 만들었죠?", value="그냥 심심해서요", inline=True)
		embed.set_footer(text="업데이트 있으면 하겠습니다.")
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
			colour = discord.Color.blue()
		)
		
		embed.set_thumbnail(url="https://i.imgur.com/SD4k1fc.jpg")
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
		# print("초승돌결정",cc,"개")
		# print("강높주",StrengthIron * n,"개")
		# print("흑빛",Blacklight * i,"개")
		# print("철쭉",Royalazalea * i,"개")
		# print("수선화",Narcissus * i,"개")
		# print("철주괴",Iron * i,"개")
		# print("구리",Copper * i,"개")
		# print("은괴",Silver * i,"개")
		
		await message.channel.send(client, embed=embed)
		
	if message.content.startswith("!초승돌 강화"):
		awit	message.channel.send("초승돌 강화" + message.content[7:] + "개 만드는 재료")
		
		userInput = message.content[7:]
		n = int(userInput)
		
		
		CrescentStone2 = 2			#2단계 강화
		CrescenticCrystal2 = 3
		
		CrescentStone3 = 3			#3단계 강화
		CrescenticCrystal2 = 5
		
		CrescentStone4 = 4			#4단계 강화
		CrescenticCrystal2 = 8
		
		CrescentStone5 = 5			#5단계 강화
		CrescenticCrystal2 = 15
		
		CrescentStone6 = 6			#6단계 강화
		CrescenticCrystal2 = 20
		
		embed = discord.Embed(
			title = "초승돌 강화",
			description = "",
			colour = discord.Color.red()
		)
		
		embed.add_field(name = '초승돌 강화석 2단계', value = CrescentStone2 * n, inline=True)
		embed.add_field(name = '초승돌 강화석 2단계', value = CrescenticCrystal2 * n, inline=True)
		embed.add_field(name = '초승돌 강화석 3단계', value = CrescentStone2 * n, inline=True)
		embed.add_field(name = '초승돌 강화석 3단계', value = CrescenticCrystal2 * n, inline=True)		
		embed.add_field(name = '초승돌 강화석 4단계', value = CrescentStone2 * n, inline=True)
		embed.add_field(name = '초승돌 강화석 4단계', value = CrescenticCrystal2 * n, inline=True)
		embed.add_field(name = '초승돌 강화석 5단계', value = CrescentStone2 * n, inline=True)
		embed.add_field(name = '초승돌 강화석 5단계', value = CrescenticCrystal2 * n, inline=True)		
		embed.add_field(name = '초승돌 강화석 6단계', value = CrescentStone2 * n, inline=True)
		embed.add_field(name = '초승돌 강화석 6단계', value = CrescenticCrystal2 * n, inline=True)
		embed.add_field(name = '초승돌 강화석 6단계', value = CrescentStone2 * n, inline=True)
		
		
		
	if message.content.startswith("!보름돌"):
			await message.channel.send("악세 보름돌" + message.content[4:] + "개 만드는 재료")
			
			userInput = message.content[4:]
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
			
			# embed.set_thumbnail
			embed.add_field(name = '추적,투지 보름돌', value = n, inline=True)
			embed.add_field(name = '사랑,초월 보름돌', value = n, inline=True)
			embed.add_field(name = '신비한 달의 정수', value = n * MoonEssence, inline=False)
			embed.add_field(name = '정원의 신비한 가루', value = n * YardPowder, inline=False)
			embed.add_field(name = '투명한 가루가 섞인 기름', value = n * Dye, inline=True)
			embed.add_field(name = '부드러운 줄기 염료', value = n * Dye, inline=True)
			embed.add_field(name = '푸른색 산호조각', value = n * BlueCoral, inline=False)
			
			print("보름돌", n, "개")
			
			await message.channel.send(client, embed=embed)
			
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
		cornjs3 = bsObj.select('li[class=point]')	#20개 포인트
		cornjsR = bsObj.find('table', {'class': 'table-bond right'})
		cornjs2 = cornjs.text
		cornjs4 = cornjsR.text
		cornjs6 = cornjs3.text #20개 포인트
		
		embed.set_thumbnail(url="https://i.imgur.com/SD4k1fc.jpg")
		embed.add_field(name='대륙', value=cornjs2, inline=True)
		embed.add_field(name='대륙', value=cornjs4, inline=True)
		embed.set_footer(text="업데이트예정", icon_url="https://i.imgur.com/SD4k1fc.jpg")
		embed.add_field(name='최소수량', value=cornjs6, inline=True) #20개 포인트
		await message.channel.send(client, embed=embed)		
			
	

	
		
client.run('token')


 
