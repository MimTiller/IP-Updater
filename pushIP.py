from time import sleep
import requests,logging, datetime,os
from godaddypy import Client, Account
global currentip


domain = ""

#Get public IP address
IPADDR= str(requests.get('http://ip.42.pl/raw').text)


#Godaddy keys: https://developer.godaddy.com/getstarted
godaddy_key=""
godaddy_secret=""

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

        else:
            print ('same IP, no need to update')
            changed = False
        logging.info('{} - GoDaddyIP:{} - Public IP:{} - Changed?:{}'.format(datetime.datetime.now(),godaddyip,currentip,changed))
    except:
        pass

def update_godaddy_ip(ip):
    try:
        domain = Account(api_key=godaddy_key,api_secret=godaddy_secret)
        client = Client(domain)
        client.update_ip(ip, domains=[domain])
    except:
        pass

def get_godaddy_ip():
    vinylcraft = Account(api_key=godaddy_key,api_secret=godaddy_secret)
    client = Client(vinylcraft)
    r = client.get_records(domain, record_type='A', name='@')
    return r

currentip = ''
check_ip()
