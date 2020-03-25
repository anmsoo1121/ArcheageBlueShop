import discord
import asyncio
# import requests
# from bs4 import BeautifulSoup
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

	if message.content.startswith("!만든사람"):
		await message.channel.send("Hs")
		
	if message.content.startswith("!help"):
		embed = discord.Embed(title="이건뭐죠?", description="archeage 푸른소금상회 채권봇입니다.", color=0x62c1cc)
		embed.add_field(name="왜 만들었죠?", value="그냥 심심해서요", inline=True)
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
	

	
		
client.run('NjkwMDk0MDkxMTAyNTg0ODMy.XnQdPQ.0dY4ZO1lt-Grvc_2QeKzwpHSbIU')


 
