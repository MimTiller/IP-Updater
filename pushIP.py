#!/usr/bin/python3
from time import sleep
from datetime import datetime
import requests
from godaddypy import Client, Account
from datetime import datetime
global currentip

IPADDR= str(requests.get('http://ip.42.pl/raw').text)
godaddy_key="dKt55ixCf7cp_EpAtqWabDLagjACMABWqA2"
godaddy_secret="EpAw5Sr5uCKcKCqKJzwT2J"


time = datetime.now()


def check_ip():
        godaddyip =get_godaddy_ip()[0]['data']
        currentip= str(requests.get('http://ip.42.pl/raw').text)
        print ('current public IP is: {}, godaddy IP is: {}, time is: {}'.format(currentip, godaddyip,time))
        if godaddyip != currentip:
                print ('updating IP to {}'.format(currentip))
                update_godaddy_ip(currentip)
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

currentip = ''

check_ip()
