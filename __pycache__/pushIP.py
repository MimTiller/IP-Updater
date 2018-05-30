
from time import sleep
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('miller.allen.tim@gmail.com','S0crazy123')
IP = "192.168.0.1"
msg = 'your ip is {}'.format(IP)
server.sendmail('miller.allen.tim@gmail.com','4022140489@vtext.com',msg)




def check_keywords():
	pass

Running = True
while Running:
	check_keywords()
	sleep(60)
