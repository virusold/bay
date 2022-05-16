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
import subprocess
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
	
	'https://i.instagram.com/api/v1/users/check_username/',
	'https://z-p3.www.instagram.com/api/v1/users/check_username/',
	'https://z-p4.www.instagram.com/api/v1/users/check_username/',
	'https://z-p42.www.instagram.com/api/v1/users/check_username/',
	'https://secure.instagram.com/api/v1/users/check_username/',
	'https://upload.instagram.com/api/v1/users/check_username/',
	'https://badges.instagram.com/api/v1/users/check_username/',
	'https://b.i.instagram.com/api/v1/users/check_username/',
	'https://z-p15.i.instagram.com/api/v1/users/check_username/',
	'https://z-p4.i.instagram.com/api/v1/users/check_username/',
	'https://z-p42.i.instagram.com/api/v1/users/check_username/',

]
email='cwq@g.com'
passwd='bakwTest'


######################### get info #########################


headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0",
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
"Accept-Encoding": "gzip, deflate",
"cookie":"Cookie: ig_did=F146FA19-645F-4284-919A-6D3EBAE67461; mid=X11J2gAEAAEwBxMfA6SNdIDyc1mq; datr=kbNzX76XFOwPnHNZoStB8DfF; ig_nrcb=1; shbid=13522; shbts=1613692365.749425; ig_direct_region_hint=ASH; ds_user_id=45911023783; rur=FRC"}
xx=s.get("https://www.instagram.com/",headers=headers)
xx=s.get("https://www.instagram.com/accounts/login/",headers=headers)
xx=s.get("https://www.instagram.com/accounts/login/ajax/",headers=headers)
xx=s.get("https://www.instagram.com/accounts/login/",headers=headers)
xx= s.get("https://www.instagram.com/web/__mid/?__a=1",headers=headers)
# print(xx.cookies)
try:
    mid=xx.cookies['mid']
    csrftoken=xx.cookies['csrftoken']
    # mid=xx.text.strip()
except Exception as e:
    info=s.get("https://i.instagram.com/accounts/login/ajax/",headers=headers)
    try:
        csrftoken=info.cookies['csrftoken']
    except Exception as e:
        pass
    mid=s.get("https://www.instagram.com/web/__mid/",headers=headers).text
    if "html" in mid:
        s=session()
        info=s.get("https://i.instagram.com/accounts/login/",headers=headers)
        # print( info.cookies)
        try:
            csrftoken=info.cookies['csrftoken']
            mid=info.cookies['mid']
        except Exception as e:
            csrftoken="H4HMZcIZRvlzRQcVCewR7kFEcFrOM0pu"
        if 'mid' in str(info.cookies):
            mid=info.cookies['mid']
        else:
            exit("banned")

######################### get info #########################


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

proxy=[]
for _ in open("proxy.txt","r").readlines():
	proxy.append(_.strip())


def controller(user,status):
	system("python control.py '{}' {}".format(user,status))
a=session()
def req(user,r):
	b=5555555555555555555
	while 1:
		_=choice(urls)
		data='{"_csrftoken":"0","username":"'+user+'","guid":"'+guid+'","device_id":"android-'+device_id+'","email":"'+email+'","password":"'+passwd+'"}'
		data={"signed_body":"{}.{}".format(sig,data),"ig_sig_key_version":"4"}
		prx=choice(proxy)
		try:
			check=s.post(_,
				data=data,
				headers=headers,
				# https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all
				# proxies={"http":  "{}".format(prx),"https": "{}".format(prx)}
				# proxies={"http":  "{}".format(prx),"https": "{}".format(prx)}
				# proxies={"http":  "socks5://{}".format(prx),"https": "socks5://{}".format(prx)}
				proxies={"http":  "socks4://{}".format(prx),"https": "socks4://{}".format(prx)}

				).content
		except Exception as e:
			return
		
		
		if 'check_username' in _:
			print("DN")
			if '''"available":false,"existing_user_password":false,"error":"This username isn't available.","status":"ok","error_type":"username_is_taken"''' in check:
				if user in r:
					pass
				else:
					startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
					startzone=startzone[0:-13]
					a.get(te_url+'sendMessage?text=14day\n@{}\n{}\nBy @G0x3a&chat_id={}'.format(user,startzone,pro))
				print(14,user)
				controller(user,1)
				break
			elif 'username_is_taken' in check:
				if user in r:
					print("Hi",user)
					controller(user,0)
					startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
					startzone=startzone[0:-13]
					a.get(te_url+'sendMessage?text=skip 14day\n@{}\n{}\nBy @G0x3a&chat_id={}'.format(user,startzone,pro))
					break
				else:
					print("pass",user,)
					break
				break

			elif "wait" in check:
				# print("Please Wait",b)
				b+=1
			else:
				print(check)
				break
			

		else:
			print("DN")

			if 'username_held_by_others' in check:
				if user in r:
					pass
				else:
					startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
					startzone=startzone[0:-13]
					a.get(te_url+'sendMessage?text=14day\n@{}\n{}\nBy @G0x3a&chat_id={}'.format(user,startzone,pro))
				print(14,user)
				controller(user,1)
				break
			elif 'username_is_taken' in check:
				if user in r:
					print("Hi",user)
					controller(user,0)
					startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
					startzone=startzone[0:-13]
					a.get(te_url+'sendMessage?text=skip 14day\n@{}\n{}\nBy @G0x3a&chat_id={}'.format(user,startzone,pro))
					break
				else:
					print("pass",user,)
					break
				break

			elif "wait" in check:
				# print("Please Wait",b)
				b+=1
			else:
				print(check)
				break
def start(_,user):
	b=0
	r = subprocess.check_output("cat username_held_by_others.lst", shell=True)
	data='{"_csrftoken":"0","username":"'+user+'","guid":"'+guid+'","device_id":"android-'+device_id+'","email":"'+email+'","password":"'+passwd+'"}'
	data={"signed_body":"{}.{}".format(sig,data),"ig_sig_key_version":"4"}
	check=s.post(_,
			data=data,
			headers=headers
			,proxies={"http":  "socks5://127.0.0.1:9050","https": "socks5://127.0.0.1:9050"}
			).content
	if 'check_username' in _:
		if '''"available":false,"existing_user_password":false,"error":"This username isn't available.","status":"ok","error_type":"username_is_taken"''' in check:
			if user in r:
				pass
			else:
				startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
				startzone=startzone[0:-13]
				requests.get(te_url+'sendMessage?text=14day\n@{}\n{}\nBy @G0x3a&chat_id={}'.format(user,startzone,pro))
			print(14,user)
			controller(user,1)
		elif 'username_is_taken' in check:
			if user in r:
				print("Hi",user)
				controller(user,0)
				startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
				startzone=startzone[0:-13]
				s.get(te_url+'sendMessage?text=skip 14day\n@{}\n{}\nBy @G0x3a&chat_id={}'.format(user,startzone,pro))
			else:
				print("pass",user,)

		elif "wait" in check:
			# print("Please Wait",b)
			req(user,r)
			b+=1
		else:
			print(check)
		

	else:


		if 'username_held_by_others' in check:
			if user in r:
				pass
			else:
				startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
				startzone=startzone[0:-13]
				requests.get(te_url+'sendMessage?text=14day\n@{}\n{}\nBy @G0x3a&chat_id={}'.format(user,startzone,pro))
			print(14,user)
			controller(user,1)
			
		elif 'username_is_taken' in check:
			if user in r:
				print("Hi",user)
				controller(user,0)
				startzone="{}".format(datetime.now(timezone("Asia/Baghdad")))
				startzone=startzone[0:-13]
				s.get(te_url+'sendMessage?text=skip 14day\n@{}\n{}\nBy @G0x3a&chat_id={}'.format(user,startzone,pro))
				
			else:
				print("pass",user,)
				
			

		elif "wait" in check:
			# print("Please Wait",b)
			req(user,r)
			b+=1
		else:
			print(check)
			
n=0
o=0

while 1:
	try:
		if o>=len(users):
			o=0
			sleep(5)

		Thread(target=start,args=(
			
			choice(

				urls
				)
				,
				users[o],

			)).start()
		
		o+=1
		sleep(float(argv[2]))
		system("killall -HUP tor")
	except Exception as e:
		print(str(e))
	


	

