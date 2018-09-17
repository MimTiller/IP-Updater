from time import sleep
import requests,logging, datetime,os
from godaddypy import Client, Account
global currentip


IPADDR= str(requests.get('http://ip.42.pl/raw').text)

godaddy_key="dKt55ixCf7cp_EpAtqWabDLagjACMABWqA2"
godaddy_secret="EpAw5Sr5uCKcKCqKJzwT2J"

logging.basicConfig(filename='{}/logs/{}.log'.format(os.getcwd(),datetime.datetime.now().strftime("%m_%d_%Y_%H-%M")),level=logging.DEBUG)
changed = ''
def check_ip():
	try:
		godaddyip =get_godaddy_ip()[0]['data'] 
		currentip= IPADDR
		print ('current public IP is: {}, godaddy IP is: {}'.format(currentip, godaddyip))
		if godaddyip != currentip:
			print ('updating IP to {}'.format(currentip))
			changed = True
			update_godaddy_ip(currentip)
			#send_mailgun_message(currentip)

		else: 
			print ('same IP, no need to update')
			changed = False
		logging.info('{} - GoDaddyIP:{} - Public IP:{} - Changed?:{}'.format(datetime.datetime.now(),godaddyip,currentip,changed))
	except:
		pass

def update_godaddy_ip(ip):
	try:
		vinylcraft = Account(api_key=godaddy_key,api_secret=godaddy_secret)
		client = Client(vinylcraft)
		client.update_ip(ip, domains=['vinylcraft.net'])
	except:
		pass
		
def get_godaddy_ip():
	vinylcraft = Account(api_key=godaddy_key,api_secret=godaddy_secret)
	client = Client(vinylcraft)
	r = client.get_records('vinylcraft.net', record_type='A', name='@')
	return r

currentip = ''    
check_ip()


