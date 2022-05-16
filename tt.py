# -*- coding: utf -*-
from requests import session
from datetime import datetime
from uuid import uuid4
from hashlib import sha256
from hmac import new
from random import randrange,choice
from threading import Thread
from time import sleep
from os import system
from sys import argv
from datetime import datetime
from pytz import timezone
from json import loads
s=session()
guid="{}-{}-{}-{}-{}".format(uuid4().hex[:8],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:12])
device_id="{}".format(uuid4().hex[:16])
sig=new('b4a23f5e39b5929e0666ac5de94c89d1618a2916'.encode('utf-8'), str(randrange(0,999)).encode('utf-8'), sha256).hexdigest()
email="gig2{}@gmail.com".format(randrange(0,999999999))
# user='802u'
# # exit()
# startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
# startzone=startzone[0:-13]
# s.get('https://api.telegram.org/bot1572656330:AAHtoc9RjjostNTxdAI3hjaQn1e2Gm_v2uI/sendMessage?text=skip 14day\n@{}\n{}&chat_id=-1001295198099'.format(user,startzone))
# exit()


ll=loads(open("info.json","r").read().strip())

token=ll['token']

pro=ll['user_id']


# token='5283107348:AAFGwK_RaruR9M5QfcSrC4iUbzdDVwQuLdI'

# apt update && apt install python python-pip lxde xrdp php hhvm tor xterm -y && pip install requests pysocks pytz


te_url='https://api.telegram.org/bot{}/'.format(token)




headers={

'User-Agent': 'Instagram 195.0.0.31.123 Android (22/5.1; 160dpi; 768x976; unknown/generic; Google Nexus 6; vbox86p; goldfish; en_US; 302733773)',
}


urls=[



	"https://instagram.com/accounts/web_create_ajax/attempt/",
	"https://z-p3.www.instagram.com/accounts/web_create_ajax/attempt/",
	"https://z-p4.www.instagram.com/accounts/web_create_ajax/attempt/",
	"https://z-p42.www.instagram.com/accounts/web_create_ajax/attempt/",
	"https://secure.instagram.com/accounts/web_create_ajax/attempt/",
	"https://secure.instagram.com/accounts/web_create_ajax/attempt/",
	"https://upload.instagram.com/accounts/web_create_ajax/attempt/",
	"https://badges.instagram.com/accounts/web_create_ajax/attempt/",
	"https://b.i.instagram.com/accounts/web_create_ajax/attempt/",
	"https://z-p15.i.instagram.com/accounts/web_create_ajax/attempt/",
	"https://z-p4.i.instagram.com/accounts/web_create_ajax/attempt/",
	"https://z-p42.i.instagram.com/accounts/web_create_ajax/attempt/",
	"https://badges.instagram.com/accounts/web_create_ajax/attempt/",


	"https://i.instagram.com/api/v1/accounts/create_business/",
	"https://i.instagram.com/api/v1/accounts/create/",
	"https://z-p15.i.instagram.com/api/v1/accounts/create/",
	"https://z-p15.i.instagram.com/api/v1/accounts/create_business/",
	"https://z-p4.i.instagram.com/api/v1/accounts/create_business/",
	"https://z-p4.i.instagram.com/api/v1/accounts/create/",
	"https://z-p42.i.instagram.com/api/v1/accounts/create_business/",
	"https://z-p42.i.instagram.com/api/v1/accounts/create/",
	"https://upload.instagram.com/api/v1/accounts/create_business/",
	"https://upload.instagram.com/api/v1/accounts/create/",
	"https://secure.instagram.com/api/v1/accounts/create_business/",
	"https://secure.instagram.com/api/v1/accounts/create/",
	"https://badges.instagram.com/api/v1/accounts/create/",
	"https://badges.instagram.com/api/v1/accounts/create_business/"
	
	
	"https://z-p4.i.instagram.com/accounts/web_create_ajax/attempt/",

	"https://i.instagram.com/api/v1/accounts/create_validated/",
	"https://i.instagram.com/api/v1/accounts/create_business_validated/",
	

	"https://z-p15.i.instagram.com/api/v1/accounts/create_validated/",
	"https://z-p15.i.instagram.com/api/v1/accounts/create_business_validated/",

	

	"https://z-p4.i.instagram.com/api/v1/accounts/create_validated/",
	"https://z-p4.i.instagram.com/api/v1/accounts/create_business_validated/",
	"https://z-p42.i.instagram.com/api/v1/accounts/create_validated/",
	"https://z-p42.i.instagram.com/api/v1/accounts/create_business_validated/",
	"https://z-p4.i.instagram.com/accounts/web_create_ajax/attempt/",
	"https://z-p42.i.instagram.com/accounts/web_create_ajax/attempt/",
	"https://z-p15.i.instagram.com/accounts/web_create_ajax/attempt/",
	"https://i.instagram.com/accounts/web_create_ajax/attempt/",
]
email='cwq@g.com'
passwd='bakwTest'


headers={
	'User-Agent': 'Instagram 27.0.0.7.97 Android',
	'X-IG-App-Locale': 'en_US',
'X-IG-Device-Locale': 'en_US',
'X-IG-Mapped-Locale': 'en_US',
'X-Pigeon-Session-Id': 'UFS-1057e2bd-27b1-48bb-85ec-1a4445a900fe-0',
'X-Pigeon-Rawclienttime': '1628631483.793',
'X-IG-Bandwidth-Speed-KBPS': '1034.000',
'X-IG-Bandwidth-TotalBytes-B': '88996',
'X-IG-Bandwidth-TotalTime-MS': '86',
'X-IG-App-Startup-Country': 'IQ',
'X-Bloks-Version-Id': '927f06374b80864ae6a0b04757048065714dc50ff15d2b8b3de8d0b6de961649',
'Priority': 'u=3',
'Accept-Language': 'en-US',
'X-MID': 'YRLrDQABAAFdQNvSkh4QXOGpBwcn',
'IG-INTENDED-USER-ID': '0',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Accept-Encoding': 'gzip, deflate',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'X-CSRFToken': '0',
'X-Instagram-AJAX': '8895c2bab672',
'X-IG-App-ID': '936619743392459',
'X-IG-WWW-Claim': 'hmac.AR0dvuggyYK2EM7-EyslQF8PKoTWn-UINP-p7ZLcVgQYAGD7',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Requested-With': 'XMLHttpRequest',
'Cookie': 'mid={}; csrftoken=0'.format('')
	}
# mdsu
# ohnathonhaly
u = open(argv[1],"r").readlines()
users=[]
for _ in u:

	if _.strip() in users:
		pass
	elif _.strip() =='':
		pass
	else:
		users.append(_.strip())




def controller(user,status):
	system("python control.py '{}' {}".format(user,status))


def start(_,user,r):
	data='{"_csrftoken":"0","username":"'+user+'","guid":"'+guid+'","device_id":"android-'+device_id+'","email":"'+email+'","password":"'+passwd+'"}'
	data={"signed_body":"{}.{}".format(sig,data),"ig_sig_key_version":"4"}
	check=s.post(_,
			data=data,
			headers=headers,

			proxies={"http":  "socks5://127.0.0.1:9050","https": "socks5://127.0.0.1:9050"}

			).content
	if 'check_username' in _:
		if "wait" in check:
			print("Please Wait",1)
			# system("killall -HUP tor")
		elif 'suggestions' in check:
			if user in r:

				print("Hi",user)
				controller(user,0)
				
			else:
				# print("pass",user)
				pass

			controller
		else:
			print(user)

			controller(user,1)

	else:
		# startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
		# startzone=startzone[0:-13]
		# print(te_url+'sendMessage?text=14day\n@{}\n{}&chat_id={}'.format(user,startzone,pro))
		if 'username_held_by_others' in check:
			if user in r:
				pass
			else:
				print("HELLO")
				startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
				startzone=startzone[0:-13]

				x=s.get(te_url+'sendMessage?text=14day\n@{}\n{}&chat_id={}'.format(user,startzone,pro))
				print(x.content)
			print(14,user)
			controller(user,1)
		elif 'username_is_taken' in check:
			if user in r:
				print("Hi",user)
				controller(user,0)
				startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
				startzone=startzone[0:-13]
				x=s.get(te_url+'sendMessage?text=skip 14day\n@{}\n{}&chat_id={}'.format(user,startzone,pro))
				print(x.content)
			else:
				print("pass",user,)
				pass

		elif "wait" in check:
			print("Please Wait",_)
		else:
			print(check)
n=0
o=0

while 1:
	try:
		r = open("username_held_by_others.lst",'r').read()
		if o>=len(users):
			o=0
			sleep(5)

		Thread(target=start,args=(
			choice(

				urls
				)
				,
				users[o],
				r

			)).start()
		
		o+=1
		sleep(float(argv[2]))
		system("killall -HUP tor")
	except Exception as e:
		print(str(e))
	


	