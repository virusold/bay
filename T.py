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
import requests
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

pro=ll['user_id'][0]


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

x=s.get('https://www.instagram.com/accounts/login/?__a=1')
csrftoken=x.cookies['csrftoken']
mid=x.cookies['mid']

headers={
	'User-Agent': 'Instagram 27.0.0.7.97 Android',
	'X-CSRFToken': csrftoken,
	'Cookie': 'mid={}; csrftoken={}'.format(mid,csrftoken)
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
	while 1:
		b=0
		data={"username":user}
		# data='{"_csrftoken":"0","username":"'+user+'","guid":"'+guid+'","device_id":"android-'+device_id+'","email":"'+email+'","password":"'+passwd+'"}'
		# data={"signed_body":"{}.{}".format(sig,data),"ig_sig_key_version":"4"}
		# check=s.post(_,
		# 		data=data,
		# 		headers=headers,

		# 		proxies={"http":  "socks5://127.0.0.1:9050","https": "socks5://127.0.0.1:9050"}

		# 		).content

		ch=s.post("https://i.instagram.com/api/v1/users/check_username/",data=data,headers={"User-Agent":"Instagram 27.0.0.7.97 Android"},proxies={"http":  "socks5://127.0.0.1:9050","https": "socks5://127.0.0.1:9050"})
		if 'cwjqkcjkcsqcwq463627789' in user:
			print(ch.content)
		if '''"available":false,"existing_user_password":false,"error":"This username isn't available.","status":"ok","error_type":"username_is_taken"''' in ch.content:
			if user in r:
				pass
			else:
				startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
				startzone=startzone[0:-13]
				requests.get(te_url+'sendMessage?text=14day\n@{}\n{}&chat_id={}'.format(user,startzone,pro))
			print(14,user)
			controller(user,1)
			break
		elif 'wait' in ch.content:
			print("Please Wait",1)
		else:
			if user in r:
				print("Hi",user)
				controller(user,0)
				startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
				startzone=startzone[0:-13]
				s.get(te_url+'sendMessage?text=skip 14day\n@{}\n{}&chat_id={}'.format(user,startzone,pro))
				break
			else:
				print("pass",user,)
				break
			break
		# if 'check_username' in _:
		# 	break
		# 	if "wait" in check:
		# 		print("Please Wait",1)
		# 		# system("killall -HUP tor")
		# 	elif 'suggestions' in check:
		# 		if user in r:
		# 			print("Hi",user)
		# 			controller(user,0)
		# 		else:
		# 			# print("pass",user)
		# 			pass

		# 		controller
		# 	else:
		# 		print(user)

		# 		controller(user,1)

		# else:


		# 	if 'username_held_by_others' in check:
		# 		if user in r:
		# 			pass
		# 		else:
		# 			startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
		# 			startzone=startzone[0:-13]
		# 			requests.get(te_url+'sendMessage?text=14day\n@{}\n{}&chat_id={}'.format(user,startzone,pro))
		# 		print(14,user)
		# 		controller(user,1)
		# 		break
		# 	elif 'username_is_taken' in check:
		# 		if user in r:
		# 			print("Hi",user)
		# 			controller(user,0)
		# 			startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
		# 			startzone=startzone[0:-13]
		# 			s.get(te_url+'sendMessage?text=skip 14day\n@{}\n{}&chat_id={}'.format(user,startzone,pro))
		# 			break
		# 		else:
		# 			print("pass",user,)
		# 			break
		# 		break

		# 	elif "wait" in check:
		# 		print("Please Wait",_,b)
		# 		system("killall -HUP tor")
		# 		break
		# 		b+=1
		# 	else:
		# 		print(check)
		# 		break
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
	


	
