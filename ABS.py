import discord
import asyncio
# import requests
# from bs4 import BeautifulSoup
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
	print("@#@#@#@#@#@#@")
	
@client.event
async def on_message(message):
	if message.author.bot:
		return None

	if message.content.startswith("!만든사람"):
		await message.channel.send("Hs")
		
	if message.content.startswith("!명령어"):
		embed = discord.Embed(title="이건뭐죠?", description="archeage 푸른소금상회 채권봇입니다.", color=0x62c1cc)
		embed.add_field(name="명령어", value="!만든사람, !채권, !수려한, !복권", inline=True)
		embed.set_footer(text="업데이트 있으면 하겠습니다.")
		print("!help")
		await message.channel.send("Hs", embed=embed)
	
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
		# embed.add_field(name='최소수량', value=cornjs3, inline=True) #20개 포인트
		await message.channel.send(client, embed=embed)
		
	if message.content.startswith("!수려한"):
		
		n = 1 					#수려한 n개
		
		StrengthIron = 40		#강도높은 주괴 = 40
		CrescenticCrystal = 70  #초승돌결정 = 70
		
		i = n * StrengthIron
		cc = n * CrescenticCrystal
		
		Blacklight = 3			#흑빛 아키움 정수 = 3
		Royalazalea = 20		#철쭉 = 20
		Narcissus = 20			#수선화 = 20
		Iron = 8				#철주괴 = 8
		Copper = 1				#구리 주괴 = 1
		Silver = 1				#은괴 = 1

		embed = discord.Embed(
			title = "초승돌 제작",
			description = "",
			colour = discord.Color.blue()
		)
		
		embed.add_field(name = '수려한 초승돌', value = n, inline=False)
		embed.add_field(name = '초승돌 결정', value = cc, inline=False)
		embed.add_field(name = '강도높은주괴', value = StrengthIron * n, inline=False)
		embed.add_field(name = '흑빛아키움정수', value = Blacklight * i, inline=False)
		embed.add_field(name = '철쭉', value = Royalazalea * i, inline=False)
		embed.add_field(name = '수선화', value = Narcissus * i, inline=False)
		embed.add_field(name = '철주괴', value = Iron * i, inline=False)
		embed.add_field(name = '구리주괴', value = Copper * i, inline=False)
		embed.add_field(name = '은괴', value = Silver * i, inline=False)
		
		print("수려한", n, "개")
		print("초승돌결정",cc,"개")
		print("강높주",StrengthIron * n,"개")
		print("흑빛",Blacklight * i,"개")
		print("철쭉",Royalazalea * i,"개")
		print("수선화",Narcissus * i,"개")
		print("철주괴",Iron * i,"개")
		print("구리",Copper * i,"개")
		print("은괴",Silver * i,"개")
		
		await message.channel.send(client, embed=embed)
		
		
		
	if message.content.startswith("!복권"):
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
				title="복권 숫자!",
				description=Text.strip(),
				colour=discord.Color.red()
			)
			await message.channel.send(client, embed=embed)
		
		

# async def on_message(message):
	# response = requests.get('https://archeage.xlgames.com/play/worldinfo/GARDEN')
	# html = response.text
	
	# soup = BeautifulSoup(html, 'html.parser') #html.parser를 사용해서 soup에 넣겠다
	
	# for tag in soup.select('li[class=point]'):
		# print(tag.text.strip())
	
	
	# for tag in soup.select('div[class=bond-info]'):	 
		# print(tag.text)
		
	
# for tag in soup.select('table[class=table-bond]'):
	# print(tag.text)	
	

	
		
client.run('!!')
		    
# 1kMIUT_StqojUciQvoTm-SzfIlRC89FT

