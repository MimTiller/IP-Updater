from time import sleep
import requests
# current IP at home.... 97.119.199.176
mailgunkey = "key-48443ed3c2b3c32e3876e485bd774165"
mgrecipient = 'miller.allen.tim@gmail.com'
IPADDR= str(requests.get('http://ip.42.pl/raw').text)
from godaddypy import Client, Account
global currentip
godaddy_key="dKt55ixCf7cp_EpAtqWabDLagjACMABWqA2"
godaddy_secret="EpAw5Sr5uCKcKCqKJzwT2J"


def check_ip():
	godaddyip =get_godaddy_ip()[0]['data'] 
	currentip= str(requests.get('http://ip.42.pl/raw').text)
	print ('current public IP is: {}, godaddy IP is: {}'.format(currentip, godaddyip))
	if godaddyip != currentip:
		print ('updating IP to {}'.format(currentip))
		#update_godaddy_ip(currentip)
		#send_mailgun_message(currentip)
	else: 
		print ('same IP, no need to update')

def update_godaddy_ip(ip):
	vinylcraft = Account(api_key=godaddy_key,api_secret=godaddy_secret)
	client = Client(vinylcraft)
	client.update_ip(ip, domains=['vinylcraft.net'])
	
def get_godaddy_ip():
	vinylcraft = Account(api_key=godaddy_key,api_secret=godaddy_secret)
	client = Client(vinylcraft)
	r = client.get_records('vinylcraft.net', record_type='A', name='@')
	return r

def send_mailgun_message(ip):
    r = requests.post(
        "https://api.mailgun.net/v3/mg.vinylcraft.net/messages",
        auth=("api", mailgunkey),
        data={"from": "Subcake (MailGun) <subcake@mg.vinylcraft.net>",
              "to": recipient,
              "subject": "IP Update",
              "text": "Your IP is {}".format(ip)})
    data = r.json()
    print (data)

currentip = ''    
while True:
	check_ip()
	sleep(900) #sleep for 15 minutes and check again
