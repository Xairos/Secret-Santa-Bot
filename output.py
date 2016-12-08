#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from email.mime.text import MIMEText
from string import Template
import smtplib

class Output:
	__metaclass__ = ABCMeta

	@abstractmethod
	def process(self, playerPairs):
		pass

class Debug(Output):
	def process(self, playerPairs):
		for gifter,receiver in playerPairs:
			print gifter.tostring() + " --> " + receiver.tostring()

class SMTP(Output):
	def __init__(self, email_address, password):
		self.email_address = email_address
		self.password = password

	def process(self, playerPairs):
		subject = "🎵It's beginning to feel a lot like Christmas!🎵"
		body_template = Template("""Hey $gfname, it's that time of year again!

You are $rname's Secret Santa! If you're lucky, $rfname might have put some wishes on the <a href="https://goo.gl/Ue1wYf">Christmas Wishlist</a>. And even if they didn't, consider helping them out by giving them some hints! 

Good luck, and Happy Holidays! 🎄
- Secret Santa Bot""")
		
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(self.email_address, self.password)
		for gifter,receiver in playerPairs:
			if ((gifter.getemail() == None) or (gifter.getemail() == "None")):
				print("WARN: No email listed for " + gifter.getname())
				continue

			body = body_template.substitute(gfname=gifter.getfirstname(), rfname=receiver.getfirstname(), rname=receiver.getname())

			send_this = MIMEText(body, 'html', 'utf-8')
			send_this['Subject'] = subject
			send_this['From'] = self.email_address
			send_this['To'] = gifter.getemail()

			print send_this.as_string()
			server.sendmail(self.email_address, gifter.getemail(), send_this.as_string())
		server.quit()