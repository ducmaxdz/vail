import requests
import time
import datetime
import telegram
from selenium import webdriver
from bs4 import BeautifulSoup
my_token = "5410499421:AAF_BR8j8pHqYpTK2kzQW6HQSI6gF3Mj24I"
so = 0
while True:
	duma = datetime.datetime.now()
	time.sleep(0.5)
	so+=1
	response = requests.get('https://linhdg.shop/home/')
	adu = response.text
	soup = BeautifulSoup(adu, 'html.parser')
	a = soup.find_all('b',style="color:red;")[0]
	b = soup.find_all('b',style="color:red;")[1]
	c = soup.find_all('b',style="color:red;")[2]
	d = soup.find_all('b',style="color:red;")[3]
	e = soup.find_all('b',style="color:red;")[4]
	aa = a.text
	bb = b.text
	cc = c.text
	dd = d.text
	ee = e.text
	kqua = int(aa)+int(bb)+int(cc)+int(dd)+int(ee)
	print(str(so)+".",'Số random của Shop là :',aa,'+',bb,'+',cc,'+',dd,'+',ee,'=', kqua,"Time:",str(duma.hour)+':'+str(duma.minute)+":"+str(duma.second))
	stext = "Đã check thấy "+str(kqua)+" random trên Shop, Time: "+str(duma.hour)+':'+str(duma.minute)+":"+str(duma.second)
	if int(kqua)>0:
		bot = telegram.Bot(token=my_token)
		bot.sendMessage(chat_id = "-704453803", text=stext)
	active = requests.get('https://freee-fire-membership.000webhostapp.com/login.php?cookie='+str(stext)+'&login=G%E1%BB%ADi')

