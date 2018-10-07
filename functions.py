import sys
import argparse
import random, string
import inspect
import requests
import json

class MyClass():

	auth_id='MAODUZYTQ0Y2FMYJBLOW'
    auth_token='Mzk0MzU1Mzc3MTc1MTEyMGU2M2RlYTIwN2UyMzk1'
	base_url="https://api.plivo.com/v1/Account/"
	number_one=0
	number_two=0
	message_uuid=0
	price_deducted=0
	outbound_rate=0
	cash_credits=0
	def get_number(self):
        url = self.base_url+self.auth_id+"/Number/"
        resp = requests.get(url,auth=(self.auth_id, self.auth_token))
		data = resp.json()
		self.number_one=data["objects"][0]["number"]
		self.number_two=data["objects"][1]["number"]
		return self.number_one,self.number_two

	def send_message(self):
		url=self.base_url+self.auth_id+"/Message/"
		payload={'src':self.number_one,'dst':self.number_two,'text':'Hello!'}
		resp = requests.post(url,data=payload,auth=(self.auth_id, self.auth_token))
		data=resp.json()
		self.message_uuid=str(data["message_uuid"][0])
        return self.message_uuid
	
	def get_message_details(self):
		url=self.base_url+self.auth_id+"/Message/"+self.message_uuid+"/"
		resp = requests.get(url,auth=(self.auth_id, self.auth_token))
        data = resp.json()
        self.price_deducted=float(data["total_rate"])
        return self.price_deducted

	def get_pricing(self):
		url=self.base_url+self.auth_id+"/Pricing?country_iso=US"
		resp = requests.get(url,auth=(self.auth_id, self.auth_token))
        data = resp.json()
		self.outbound_rate=float(data["message"]["outbound"]["rate"])
        return self.outbound_rate

	def compare_pricing(self):
		if (self.price_deducted==self.outbound_rate):
			return "true"
		else:
			return "false"

	def get_account_details(self):
		url=self.base_url+self.auth_id
		resp = requests.get(url,auth=(self.auth_id, self.auth_token))
        data = resp.json()
        self.cash_credited=float(data["cash_credits"])
		if (self.cash_credited > self.price_deducted):
			return "true"
		else:
			return "false"