from requests import session
from random import randrange,choice
from hashlib import sha256
from hmac import new

sig=new('b4a23f5e39b5929e0666ac5de94c89d1618a2916'.encode('utf-8'), str(randrange(0,999)).encode('utf-8'), sha256).hexdigest()
s=session()

headers={
	'User-Agent': 'Instagram 195.0.0.31.123 Android (22/5.1; 160dpi; 768x976; unknown/generic; Google Nexus 6; vbox86p; goldfish; en_US; 302733773)',
	"cookie":'sessionid='+"460047347:HQA7osR8PH2AP1:10"
}
__content=s.post("https://i.instagram.com/api/v1/accounts/edit_profile/",data={"signed_body":"{}.{}".format(sig,str(r'{"username":"jwckqjcwqxjaq538009805","biography":"","email":"olomonemlpe@gmail.com","phone_number":""}')),"ig_sig_key_version":"5"},headers=headers,proxies={"http":  "socks5://127.0.0.1:9050","https": "socks5://127.0.0.1:9050"}).json()
print(__content)
_content=s.post("https://i.instagram.com/api/v1/accounts/set_username/",data={"signed_body":"{}.{}".format(sig,str(r'{"username":"jwckqjcwqxjaq538009805","biography":""}')),"ig_sig_key_version":"5"},headers=headers,proxies={"http":  "socks5://127.0.0.1:9050","https": "socks5://127.0.0.1:9050"}).json()
print(_content)