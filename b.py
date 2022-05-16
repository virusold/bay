# -*- coding: utf -*-
from requests import session
from json import load,loads,dumps,dump
from io import open as  aa
from random import randint,choice,randrange
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from multiprocessing import Process
from threading import Thread
from hmac import new
from threading import Thread
from sys import argv
from uuid import uuid4
from hashlib import sha256
from hmac import new
from os import system,getpid
from requests import session
from time import sleep





from uuid import uuid4
from hashlib import sha256
from hmac import new
from random import randrange
from getpass import getpass
from json import loads


s=session()
a=session()




ll=loads(open("info.json","r").read().strip())

token=ll['token']

pro=ll['user_id']





#############################
guid="{}-{}-{}-{}-{}".format(uuid4().hex[:8],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:12])
device_id="{}".format(uuid4().hex[:16])
xxx=randrange(0,999)
sig=new('b4a23f5e39b5929e0666ac5de94c89d1618a2916'.encode('utf-8'), str(xxx).encode('utf-8'), sha256).hexdigest()



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
        print( info.cookies)
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
# device_id='dc04727bc4aacd8a'
# device_id='ad7e18bb40554e47'
guid="{}-{}-{}-{}-{}".format(uuid4().hex[:8],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:12])
guid2="{}-{}-{}-{}-{}".format(uuid4().hex[:8],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:12])
device_id="{}".format(uuid4().hex[:16])
xxx=randrange(0,999)
sig=new('b4a23f5e39b5929e0666ac5de94c89d1618a2916'.encode('utf-8'), str(xxx).encode('utf-8'), sha256).hexdigest()




# print(unquote(r'choice=0&is_bloks_web=False&bk_client_context=%7B%22bloks_version%22%3A%22927f06374b80864ae6a0b04757048065714dc50ff15d2b8b3de8d0b6de961649%22%2C%22styles_id%22%3A%22instagram%22%7D&challenge_context=%7B%22step_name%22%3A+%22%22%2C+%22nonce_code%22%3A+%22xvMrd0Se1O%22%2C+%22user_id%22%3A+2173260796%2C+%22cni%22%3A+18224646292076797%2C+%22is_stateless%22%3A+false%2C+%22challenge_type_enum%22%3A+%22UNKNOWN%22%7D&bloks_versioning_id=927f06374b80864ae6a0b04757048065714dc50ff15d2b8b3de8d0b6de961649'))
# exit()
# exit()
# LOGIN

# proxy=[]
# for _ in open("proxy.txt",'r').readlines():
# 	proxy.append(_.strip())

retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
s.mount('http://', adapter)
s.mount('https://', adapter)
a.mount('http://', adapter)
a.mount('https://', adapter)




######################### get info #########################


headers={"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0",'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5',"Accept-Encoding": "gzip, deflate","cookie":"Cookie: ig_did=F146FA19-645F-4284-919A-6D3EBAE67461; mid=X11J2gAEAAEwBxMfA6SNdIDyc1mq; datr=kbNzX76XFOwPnHNZoStB8DfF; ig_nrcb=1; shbid=13522; shbts=1613692365.749425; ig_direct_region_hint=ASH; ds_user_id=45911023783; rur=FRC"}
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
    if "html" in mid:
        s=session()
        info=s.get("https://i.instagram.com/accounts/login/",headers=headers)
        print( info.cookies)
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


url="https://api.telegram.org/bot"+token+"/"
update_id=12697509

class Checker():
	def __init__(self,s,a,user,url):
		self.s=s
		self.a=a
		self.user=user
		self.url=url
	def sendMessage(self,mess,chat_id,mes_id=0):

		self.s.get(self.url+"sendMessage?text="+str(mess)+"&chat_id="+str(chat_id)+"&reply_to_message_id="+str(mes_id))
		return
	def sentToall(self,mess,chat_id):
		self.s.get(self.url+"sendMessage?text="+str(mess)+"&chat_id="+str(chat_id))
	def isJoined(self,user_id):
		content=self.s.get(self.url+"getChatMember?chat_id=-1001289767169&user_id="+str(user_id)).json()
		if content['ok']==False:
			return False
		elif content['ok']==True:
			if content['result']['status']=="left":
				return True
			else:
				return True
		else:
			print(content.content)


def login2(username,passwd):
	headers = {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded', 'cookie': 'mid=X_m5HAAEAAGsvSjAO2PKY1ERwxwz; csrftoken=H4HMZcIZRvlzRQcVCewR7kFEcFrOM0pu;', 'origin': 'https://www.instagram.com', 'referer': 'https://www.instagram.com/', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36', 'x-csrftoken': 'H4HMZcIZRvlzRQcVCewR7kFEcFrOM0pu', 'x-ig-app-id': '1217981644879628', 'x-ig-www-claim': '0', 'x-instagram-ajax': '180c154d218a', 'x-requested-with': 'XMLHttpRequest'}
	_data={"username":username,"enc_password":"#PWD_INSTAGRAM_BROWSER:0:&:{}".format(passwd),"device_id":"android-1e90afd8fdc64711"}

	login=s.post('https://www.instagram.com/accounts/login/ajax/',data=_data,headers=headers)
	print(login.content)
	headersChose=0
	if "sessionid" in login.cookies:
		print(login.cookies['sessionid'])
		return login.cookies['sessionid']
		o=1
	elif 'challenge' in login.text:
		
		return {"status":"challenge"}
	elif 'Please wait' in login.text:
		return {"status":"wait"}

	else:
		return {"status":str(login.content)}

def login(username,passwd):
	global guid,device_id,guid2,s,proxy
	headers={
	'X-IG-App-Locale': 'en_US',
	'X-IG-Device-Locale': 'en_US',
	'X-IG-Mapped-Locale': 'en_US',
	'X-Pigeon-Session-Id': 'UFS-498d260d-b100-46d9-be92-00f5113ea46f-0',
	'X-Pigeon-Rawclienttime': '1646432243.869',
	'X-IG-Bandwidth-Speed-KBPS': '476.000',
	'X-IG-Bandwidth-TotalBytes-B': '0',
	'X-IG-Bandwidth-TotalTime-MS': '0',
	'X-IG-App-Startup-Country': 'IQ',
	'X-Bloks-Version-Id': '7d5d5c3edda9c3c433f0b903ced68830addf7027827d1194d3fbec0c41de4e7d',
	'X-IG-WWW-Claim': '0',
	'X-Bloks-Is-Layout-RTL': 'false',
	'X-IG-Device-ID': 'b18abdcc-a663-470b-abab-4a22fbb4668e',
	'X-IG-Family-Device-ID': '399f4cee-33e0-4e9e-9432-b64a1d14dee7',
	'X-IG-Android-ID': 'android-2f11e5bf1d0644dd',
	'X-IG-Timezone-Offset': '0',
	'X-IG-Nav-Chain': 'BLI:self_profile:7:cold_start,BLI:self_profile:8:button,ProfileMediaTabFragment:self_profile:9:button,TRUNCATEDx12,3vd:login_landing:22,C8L:bloks_unknown:23,C8L:bloks_unknown:24,3vd:login_landing:25,C8L:bloks_unknown:26,C8L:bloks_unknown:27,3vd:login_landing:29',
	'X-IG-Connection-Type': 'WIFI',
	'X-IG-Capabilities': '3brTv10=',
	'X-IG-App-ID': '567067343352427',
	'Priority': 'u=3',
	'Accept-Language': 'en-US',

	'User-Agent': 'Instagram 219.0.0.12.117 Android (26/8.0.0; 320dpi; 768x1184; unknown/Android; GhOSt; vbox86p; vbox86; en_US; 346138365)',
	
	'X-MID': 'YiC-CQABAAF7ireJMUyOeVj3O-H5',
	'IG-INTENDED-USER-ID': '0',
	'Accept-Encoding': 'gzip, deflate',
	'X-FB-HTTP-Engine': 'Liger',
	'X-FB-Client-IP': 'True',
	'X-FB-Server-Cluster': 'True',
	}
	login_info=r'{"trustedDeviceRecords":{"465959066":{"nonce":"pZ3EsEL83ISeT8Dor0pXNiKgCcssSxkFENpAaMsMgT9ygLTnTW1rNHuqBumT7FqN","machine_id":"YdKA8AAEAAGm7N59l2WQ0VLRlhoQ"}},"jazoest":"22480","country_codes":"[{\"country_code\":\"1\",\"source\":[\"default\"]}]","phone_id":"399f4cee-33e0-4e9e-9432-b64a1d14dee7","enc_password":"#PWD_INSTAGRAM_BROWSER:0:&:'+passwd+'","username":"'+username+'","adid":"bbe5d22c-9dca-4a4e-aa6a-4734dab8a615","guid":"b18abdcc-a663-470b-abab-4a22fbb4668e","device_id":"android-1e90afd8fdc64711","google_tokens":"[]","login_attempt_count":"6"}'
	data={"signed_body":"{}.{}".format(sig,login_info),"ig_sig_key_version":"5"}
	login=s.post("https://i.instagram.com/api/v1/accounts/login/",data=data,headers=headers)
	print(login.content)

	if 'ig-set-authorization' in login.headers  and 'pk' in login.text:
		return login.headers['ig-set-authorization']
	elif 'challenge' in login.text:
		
		return {"status":"challenge"}
	elif 'Please wait' in login.text:
		return {"status":"wait"}

	else:
		return {"status":str(login.content)}
		


headers = {'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded', 'cookie': 'mid={}; csrftoken={};'.format(mid,csrftoken), 'origin': 'https://www.instagram.com', 'referer': 'https://www.instagram.com/', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Instagram 27.0.0.7.97 Android', 'x-csrftoken': csrftoken, 'x-ig-app-id': '1217981644879628', 'x-ig-www-claim': '0', 'x-instagram-ajax': '180c154d218a', 'x-requested-with': 'XMLHttpRequest'}
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


	
	
	# "https://z-p4.i.instagram.com/accounts/web_create_ajax/attempt/",






	
	"https://i.instagram.com/api/v1/accounts/create_validated/",
	"https://i.instagram.com/api/v1/accounts/create_business_validated/",
	# "https://i.instagram.com/api/v1/users/check_username/",
	

	



	"https://z-p15.i.instagram.com/api/v1/accounts/create_validated/",
	"https://z-p15.i.instagram.com/api/v1/accounts/create_business_validated/",
	# "https://z-p15.i.instagram.com/api/v1/users/check_username/",
	

	"https://z-p4.i.instagram.com/api/v1/accounts/create_validated/",
	"https://z-p4.i.instagram.com/api/v1/accounts/create_business_validated/",
	# "https://z-p4.i.instagram.com/api/v1/users/check_username/",
	



	"https://z-p42.i.instagram.com/api/v1/accounts/create_validated/",
	"https://z-p42.i.instagram.com/api/v1/accounts/create_business_validated/",
	# "https://z-p42.i.instagram.com/api/v1/users/check_username/",
	
	"https://z-p4.i.instagram.com/accounts/web_create_ajax/attempt/",
	"https://z-p42.i.instagram.com/accounts/web_create_ajax/attempt/",
	"https://z-p15.i.instagram.com/accounts/web_create_ajax/attempt/",
	"https://i.instagram.com/accounts/web_create_ajax/attempt/",



]
def sender(s,_text,_chat_id):
	s.get("https://api.telegram.org/bot5068868031:AAGCVAYbPpikcT79uUUXuzjvbO06uvMg7vo/sendMessage?text="+_text+"&chat_id="+str(_chat_id))




def tthread(text,chat_id,message_id):
	x=Thread(target=day14,args=(text,chat_id,message_id,))
	x.start()
	x.join()


while True:
	try:
		sleep(1)
		xdata=s.get(url+"getUpdates?offset="+str(update_id)).json()
		print("N")
		try:
			if not xdata['result']:
				pass
			else:
				for result in xdata['result']:
					if result['update_id']==update_id:
						pass
					else:
						update_id=result['update_id']
						if "edited_message" in str(result):
							pass
						elif "channel_post" in str(result):
							pass
						elif "'reply_to_message'" in str(result):
							pass
						elif "'allows_multiple_answers'" in str(result):
							pass
						elif "'pinned_message'" in str(result):
							pass
						else:
							try:
								if "'text':" in str(result):

									print("i")

									message_id=result['message']['message_id']
									chat_id=str(result['message']['chat']['id'])
									text=result['message']['text']
									user_id=result['message']['from']['id']
									
									try:
										if chat_id in pro:
											print(chat_id)
											if '/xnxx' in text:
												
													text=text.split("/xnxx ")[1]
													system("echo '{}'>> users.txt".format(text))
													#system(r"ps auxw | grep [p]ython | awk '{print $2}' | grep -v "+str(getpid())+" | xargs kill -9")
													system("killall xterm")
													Checker(s,a,text,url).sendMessage('Done Add',chat_id,message_id)
											elif '/rmxnxx' in text:
												text=text.split("/rmxnxx ")[1]
												system('grep -v "{}" users.txt > tmpfile && mv tmpfile users.txt'.format(text))
												system("killall xterm")
												Checker(s,a,text,url).sendMessage('Done Remove',chat_id,message_id)
											elif '/ml' in text:
												f=open('users.txt',"r").read()
												Checker(s,a,text,url).sendMessage(f,chat_id,message_id)
												#system(r"ps auxw | grep [p]ython | awk '{print $2}' | grep -v "+str(getpid())+" | xargs kill -9")
										else:
											print(chat_id)


									except Exception as e:
										print(str(e))
									


							except Exception as e:
								print(str(e))
		except Exception as e:
			print(str(e))
	except Exception as e:
		pass