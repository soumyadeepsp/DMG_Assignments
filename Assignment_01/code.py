print('2018055 and 2018104') # Please put this first
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import json
from datetime import date
import requests


def months(m):
	if (m=='Jan'):
		return 1
	if (m=='Feb'):
		return 2
	if (m=='Mar'):
		return 3
	if (m=='Apr'):
		return 4
	if (m=='May'):
		return 5
	if (m=='Jun'):
		return 6
	if (m=='Jul'):
		return 7
	if (m=='Aug'):
		return 8
	if (m=='Sep'):
		return 9
	if (m=='Oct'):
		return 10
	if (m=='Nov'):
		return 11
	if (m=='Dec'):
		return 12

def Q1_1(json_file_path, start_date, end_date):
	data = (requests.get(url = "https://api.covid19india.org/states_daily.json")).json()
	data = data['states_daily']
	confirmed_count = 0
	recovered_count = 0
	deceased_count = 0
	for i in data:
		if (i['status']=='Confirmed'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						confirmed_count = confirmed_count + int(i[j])
		if (i['status']=='Recovered'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						recovered_count = recovered_count + int(i[j])
		if (i['status']=='Deceased'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						deceased_count = deceased_count + int(i[j])
	print ("--------------------------------------------------")
	print ("ANSWER TO Q1_1")
	print('confirmed_count: ',confirmed_count, 'recovered_count: ',recovered_count, 'deceased_count: ',deceased_count)
	return confirmed_count, recovered_count, deceased_count

def Q1_2(json_file_path, start_date, end_date):
	data = (requests.get(url = "https://api.covid19india.org/states_daily.json")).json()
	data = data['states_daily']
	confirmed_count = 0
	recovered_count = 0
	deceased_count = 0
	for i in data:
		if (i['status']=='Confirmed'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				confirmed_count = confirmed_count + int(i['dl'])
		if (i['status']=='Recovered'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				recovered_count = recovered_count + int(i['dl'])
		if (i['status']=='Deceased'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				deceased_count = deceased_count + int(i['dl'])
	print ("--------------------------------------------------")
	print ("ANSWER TO Q1_2")
	print('confirmed_count: ',confirmed_count, 'recovered_count: ',recovered_count, 'deceased_count: ',deceased_count)
	return confirmed_count, recovered_count, deceased_count

def Q1_3(json_file_path, start_date, end_date):
	data = (requests.get(url = "https://api.covid19india.org/states_daily.json")).json()
	data = data['states_daily']
	confirmed_count = 0
	recovered_count = 0
	deceased_count = 0
	for i in data:
		if (i['status']=='Confirmed'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				confirmed_count = confirmed_count + int(i['dl']) + int(i['mh'])
		if (i['status']=='Recovered'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				recovered_count = recovered_count + int(i['dl']) + int(i['mh'])
		if (i['status']=='Deceased'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				deceased_count = deceased_count + int(i['dl']) + int(i['mh'])
	print ("--------------------------------------------------")
	print ("ANSWER TO Q1_3")
	print('confirmed_count: ',confirmed_count, 'recovered_count: ',recovered_count, 'deceased_count: ',deceased_count)
	return confirmed_count, recovered_count, deceased_count

def Q1_4(json_file_path, start_date, end_date):
	data = (requests.get(url = "https://api.covid19india.org/states_daily.json")).json()
	data = data['states_daily']
	confirmed_count = {'an': 0, 'ap': 0, 'ar': 0, 'as': 0, 'br': 0, 'ch': 0, 'ct': 0, 'dd': 0, 'dn': 0, 'dl': 0, 'ga': 0, 'gj': 0, 'hp': 0, 'hr': 0, 'jh': 0, 'jk': 0, 'ka': 0, 'kl': 0, 'la': 0, 'ld': 0, 'mh': 0, 'ml': 0, 'mn': 0, 'mp': 0, 'mz': 0, 'nl': 0, 'or': 0, 'pb': 0, 'py': 0, 'rj': 0, 'sk': 0, 'tg': 0, 'tn': 0, 'tr': 0, 'tt': 0, 'un': 0, 'up': 0, 'ut': 0, 'wb': 0}
	recovered_count = {'an': 0, 'ap': 0, 'ar': 0, 'as': 0, 'br': 0, 'ch': 0, 'ct': 0, 'dd': 0, 'dn': 0, 'dl': 0, 'ga': 0, 'gj': 0, 'hp': 0, 'hr': 0, 'jh': 0, 'jk': 0, 'ka': 0, 'kl': 0, 'la': 0, 'ld': 0, 'mh': 0, 'ml': 0, 'mn': 0, 'mp': 0, 'mz': 0, 'nl': 0, 'or': 0, 'pb': 0, 'py': 0, 'rj': 0, 'sk': 0, 'tg': 0, 'tn': 0, 'tr': 0, 'tt': 0, 'un': 0, 'up': 0, 'ut': 0, 'wb': 0}
	deceased_count = {'an': 0, 'ap': 0, 'ar': 0, 'as': 0, 'br': 0, 'ch': 0, 'ct': 0, 'dd': 0, 'dn': 0, 'dl': 0, 'ga': 0, 'gj': 0, 'hp': 0, 'hr': 0, 'jh': 0, 'jk': 0, 'ka': 0, 'kl': 0, 'la': 0, 'ld': 0, 'mh': 0, 'ml': 0, 'mn': 0, 'mp': 0, 'mz': 0, 'nl': 0, 'or': 0, 'pb': 0, 'py': 0, 'rj': 0, 'sk': 0, 'tg': 0, 'tn': 0, 'tr': 0, 'tt': 0, 'un': 0, 'up': 0, 'ut': 0, 'wb': 0}
	for i in data:
		if (i['status']=='Confirmed'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						confirmed_count[j] = confirmed_count[j] + int(i[j])
		if (i['status']=='Recovered'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						recovered_count[j] = recovered_count[j] + int(i[j])
		if (i['status']=='Deceased'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						deceased_count[j] = deceased_count[j] + int(i[j])
	confirmed_count_max = max(confirmed_count, key=confirmed_count.get)
	recovered_count_max = max(recovered_count, key=recovered_count.get)
	deceased_count_max = max(deceased_count, key=deceased_count.get)
	print ("--------------------------------------------------")
	print ("ANSWER TO Q1_4")
	print('Confirmed')
	print('Highest affected State is: ', confirmed_count_max)
	print('Highest affected State count is: ', confirmed_count[confirmed_count_max])
	print('\nRecovered')
	print('Highest affected State is: ', recovered_count_max)
	print('Highest affected State count is: ', recovered_count[recovered_count_max])
	print('\nDeceased')
	print('Highest affected State is: ', deceased_count_max)
	print('Highest affected State count is: ', deceased_count[deceased_count_max])


def Q1_5(json_file_path, start_date, end_date):
	data = (requests.get(url = "https://api.covid19india.org/states_daily.json")).json()
	data = data['states_daily']
	confirmed_count = {'an': 0, 'ap': 0, 'ar': 0, 'as': 0, 'br': 0, 'ch': 0, 'ct': 0, 'dd': 0, 'dn': 0, 'dl': 0, 'ga': 0, 'gj': 0, 'hp': 0, 'hr': 0, 'jh': 0, 'jk': 0, 'ka': 0, 'kl': 0, 'la': 0, 'ld': 0, 'mh': 0, 'ml': 0, 'mn': 0, 'mp': 0, 'mz': 0, 'nl': 0, 'or': 0, 'pb': 0, 'py': 0, 'rj': 0, 'sk': 0, 'tg': 0, 'tn': 0, 'tr': 0, 'tt': 0, 'un': 0, 'up': 0, 'ut': 0, 'wb': 0}
	recovered_count = {'an': 0, 'ap': 0, 'ar': 0, 'as': 0, 'br': 0, 'ch': 0, 'ct': 0, 'dd': 0, 'dn': 0, 'dl': 0, 'ga': 0, 'gj': 0, 'hp': 0, 'hr': 0, 'jh': 0, 'jk': 0, 'ka': 0, 'kl': 0, 'la': 0, 'ld': 0, 'mh': 0, 'ml': 0, 'mn': 0, 'mp': 0, 'mz': 0, 'nl': 0, 'or': 0, 'pb': 0, 'py': 0, 'rj': 0, 'sk': 0, 'tg': 0, 'tn': 0, 'tr': 0, 'tt': 0, 'un': 0, 'up': 0, 'ut': 0, 'wb': 0}
	deceased_count = {'an': 0, 'ap': 0, 'ar': 0, 'as': 0, 'br': 0, 'ch': 0, 'ct': 0, 'dd': 0, 'dn': 0, 'dl': 0, 'ga': 0, 'gj': 0, 'hp': 0, 'hr': 0, 'jh': 0, 'jk': 0, 'ka': 0, 'kl': 0, 'la': 0, 'ld': 0, 'mh': 0, 'ml': 0, 'mn': 0, 'mp': 0, 'mz': 0, 'nl': 0, 'or': 0, 'pb': 0, 'py': 0, 'rj': 0, 'sk': 0, 'tg': 0, 'tn': 0, 'tr': 0, 'tt': 0, 'un': 0, 'up': 0, 'ut': 0, 'wb': 0}
	for i in data:
		if (i['status']=='Confirmed'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						confirmed_count[j] = confirmed_count[j] + int(i[j])
		if (i['status']=='Recovered'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						recovered_count[j] = recovered_count[j] + int(i[j])
		if (i['status']=='Deceased'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						deceased_count[j] = deceased_count[j] + int(i[j])
	confirmed_count_min = min(confirmed_count, key=confirmed_count.get)
	recovered_count_min = min(recovered_count, key=recovered_count.get)
	deceased_count_min = min(deceased_count, key=deceased_count.get)
	print ("--------------------------------------------------")
	print ("ANSWER TO Q1_5")
	print('Confirmed')
	print('Lowest affected State is: ', confirmed_count_min)
	print('Lowest affected State count is: ', confirmed_count[confirmed_count_min])
	print('\nRecovered')
	print('Lowest affected State is: ', recovered_count_min)
	print('Lowest affected State count is: ', recovered_count[recovered_count_min])
	print('\nDeceased')
	print('Lowest affected State is: ', deceased_count_min)
	print('Lowest affected State count is: ', deceased_count[deceased_count_min])


def Q1_6(json_file_path, start_date, end_date):
	data = (requests.get(url = "https://api.covid19india.org/states_daily.json")).json()
	data = data['states_daily']
	confirmed_count_spike = 0
	recovered_count_spike = 0
	deceased_count_spike = 0
	for i in range(len(data)):
		if (data[i]['status']=='Confirmed'):
			d = data[i]['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				if (i>=2):
					temp_spike = int(data[i]['dl'])
					if (temp_spike > confirmed_count_spike):
						confirmed_count_spike = temp_spike
						confirmed_count_spike_day = data[i]['date']
		if (data[i]['status']=='Recovered'):
			d = data[i]['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				if (i>=2):
					temp_spike = int(data[i]['dl'])
					if (temp_spike > recovered_count_spike):
						recovered_count_spike = temp_spike
						recovered_count_spike_day = data[i]['date']
		if (data[i]['status']=='Deceased'):
			d = data[i]['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				if (i>=2):
					temp_spike = int(data[i]['dl'])
					if (temp_spike > deceased_count_spike):
						deceased_count_spike = temp_spike
						deceased_count_spike_day = data[i]['date']
	print ("--------------------------------------------------")
	print ("ANSWER TO Q1_6")
	print('Confirmed')
	print('Day: ',confirmed_count_spike_day)
	print('Count: ',confirmed_count_spike)
	print('\nRecovered')
	print('Day: ',recovered_count_spike_day)
	print('Count: ',recovered_count_spike)
	print('\nDeceased')
	print('Day: ',deceased_count_spike_day)
	print('Count: ',deceased_count_spike)


def Q1_7(json_file_path, start_date, end_date):
	data = (requests.get(url = "https://api.covid19india.org/states_daily.json")).json()
	data = data['states_daily']
	confirmed_count_spike = 0
	recovered_count_spike = 0
	deceased_count_spike = 0
	active = {'an': 0, 'ap': 0, 'ar': 0, 'as': 0, 'br': 0, 'ch': 0, 'ct': 0, 'dd': 0, 'dn': 0, 'dl': 0, 'ga': 0, 'gj': 0, 'hp': 0, 'hr': 0, 'jh': 0, 'jk': 0, 'ka': 0, 'kl': 0, 'la': 0, 'ld': 0, 'mh': 0, 'ml': 0, 'mn': 0, 'mp': 0, 'mz': 0, 'nl': 0, 'or': 0, 'pb': 0, 'py': 0, 'rj': 0, 'sk': 0, 'tg': 0, 'tn': 0, 'tr': 0, 'tt': 0, 'un': 0, 'up': 0, 'ut': 0, 'wb': 0}
	for i in data:
		if (i['status']=='Confirmed'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt' and j!='tt' and j!='tt'):
						active[j] = active[j] + int(i[j])
		if (i['status']=='Recovered'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt' and j!='tt'):
						active[j] = active[j] - int(i[j])
		if (i['status']=='Deceased'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						active[j] = active[j] - int(i[j])
	print ("--------------------------------------------------")
	print ("ANSWER TO Q1_7")
	for i in active:
		print ("Number of Active cases in ",i," are : ",active[i])


def Q2_1(json_file_path, start_date, end_date):
	data = (requests.get(url = "https://api.covid19india.org/states_daily.json")).json()
	data = data['states_daily']
	confirmed_count_array = []
	recovered_count_array = []
	deceased_count_array = []
	confirmed_count = 0
	recovered_count = 0
	deceased_count = 0
	x_axis = []
	c = 0
	dates = []
	for i in data:
		if (i['status']=='Confirmed'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						confirmed_count = confirmed_count + int(i[j])
				confirmed_count_array.append(confirmed_count)
				if (d not in dates):
					dates.append(d)
					x_axis.append(c)
					c = c+1
		if (i['status']=='Recovered'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						recovered_count = recovered_count + int(i[j])
				recovered_count_array.append(recovered_count)
				if (d not in dates):
					dates.append(d)
					x_axis.append(c)
					c = c+1
		if (i['status']=='Deceased'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				for j in i:
					if (j!='status' and j!='date' and j!='tt'):
						deceased_count = deceased_count + int(i[j])
				deceased_count_array.append(deceased_count)
				if (d not in dates):
					dates.append(d)
					x_axis.append(c)
					c = c+1
	plt.plot(x_axis, confirmed_count_array)
	plt.plot(x_axis, recovered_count_array)
	plt.plot(x_axis, deceased_count_array)
	plt.show()
	#plt.save()

def Q2_2(json_file_path, start_date, end_date):
	data = (requests.get(url = "https://api.covid19india.org/states_daily.json")).json()
	data = data['states_daily']
	confirmed_count_array = []
	recovered_count_array = []
	deceased_count_array = []
	confirmed_count = 0
	recovered_count = 0
	deceased_count = 0
	x_axis = []
	c = 0
	dates = []
	for i in data:
		if (i['status']=='Confirmed'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				confirmed_count = confirmed_count + int(i['dl'])
				confirmed_count_array.append(confirmed_count)
				if (d not in dates):
					dates.append(d)
					x_axis.append(c)
					c = c+1
		if (i['status']=='Recovered'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				recovered_count = recovered_count + int(i['dl'])
				recovered_count_array.append(recovered_count)
				if (d not in dates):
					dates.append(d)
					x_axis.append(c)
					c = c+1
		if (i['status']=='Deceased'):
			d = i['date']
			sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
			ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
			cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
			if ((cd-sd).days>=0 and (cd-ed).days<=0):
				deceased_count = deceased_count + int(i['dl'])
				deceased_count_array.append(deceased_count)
				if (d not in dates):
					dates.append(d)
					x_axis.append(c)
					c = c+1
	df = pd.DataFrame()
	df["Confirmed"] = confirmed_count_array
	df["Recovered"] = recovered_count_array
	df["Deceased"] = deceased_count_array
	df.plot(kind="area",stacked=False,figsize=(16,6))
	plt.ylabel("Cases in State DELHI")
	plt.show()
	#plt.save()


def Q2_3(json_file_path, start_date, end_date):
	data = (requests.get(url = "https://api.covid19india.org/states_daily.json")).json()
	data = data['states_daily']
	active = []
	temp = 0
	x_axis = []
	c = 0
	dates = []
	for i in range(0,len(data),3):
		d = data[i]['date']
		sd = date(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10])) #start_date
		ed = date(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10])) #end_Date
		cd = date(int('20'+d[7:9]), int(months(d[3:6])), int(d[0:2])) #current_date
		if ((cd-sd).days>=0 and (cd-ed).days<=0):
			for j in data[i]:
				if (j!='status' and j!='date' and j!='tt'):
					temp = temp + int(data[i][j])
					temp = temp - int(data[i+1][j])
					temp = temp - int(data[i+2][j])
			active.append(temp)
			x_axis.append(c)
			c = c+1
	plt.plot(x_axis, active)
	plt.show()
	#plt.save()

#defining hypothesis 
def hypothesis(theta, x):
	return theta[0] + theta[1]*x

# defining update rule 
def gradient(x,y,theta):
	grad = np.array([0.0,0.0])
	m = x.shape[0]
	for i in range(m):
		grad[0] += (hypothesis(theta,x[i]) - y[i])
		grad[1] += (hypothesis(theta,x[i]) - y[i])*x[i]
	return grad

#applying gradient_descent
def gradient_descent(x,y,learning_rate,maxIter):
	theta = np.array([0.0,0.0])
	for i in range(maxIter):
		grad = gradient(x,y,theta)
		theta[0] = theta[0] - learning_rate*grad[0]
		theta[1] = theta[1] - learning_rate*grad[1] 
	return theta

def normal_equation(x, y):
	return np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(x),x)),np.transpose(x)),y)

def Q3(json_file_path, start_date, end_date):
	data = (requests.get(url = "https://api.covid19india.org/states_daily.json")).json()
	data = data['states_daily']
	cx = []
	cy = []
	rx = []
	ry = []
	dx = []
	dy = []
	for i in data:
		if (i['status']=='Confirmed'):
			din = i['date']
			day = int(din[0:2])
			month = int(months(din[3:6]))
			year = int('20'+din[7:9])
			f_date = date(2020, 3, 14)
			l_date = date(year, month, day)
			delta = l_date - f_date
			cx.append(delta.days)
			cy.append(i['dl'])
		elif (i['status']=='Recovered'):
			din = i['date']
			day = int(din[0:2])
			month = int(months(din[3:6]))
			year = int('20'+din[7:9])
			f_date = date(2020, 3, 14)
			l_date = date(year, month, day)
			delta = l_date - f_date
			rx.append(delta.days)
			ry.append(i['dl'])
		else:
			din = i['date']
			day = int(din[0:2])
			month = int(months(din[3:6]))
			year = int('20'+din[7:9])
			f_date = date(2020, 3, 14)
			l_date = date(year, month, day)
			delta = l_date - f_date
			dx.append(delta.days)
			dy.append(i['dl'])


	cx = np.array(cx)
	cy = np.array(cy)
	cx = cx.astype('int64')
	cy = cy.astype('int64')
	x = cx
	y = cy

	
	# theta = gradient_descent(x,y,learning_rate=0.0000001,maxIter=10000)
	x = np.reshape(x,(-1,1))
	x = np.concatenate((x,np.ones((len(x),1))),axis=1) # Adding a column of 1s to X array. Example - "To take care of c in case of y = mx + c"
	y = np.reshape(y,(-1,1)) # Conversion of 1D array to 2D
	theta = normal_equation(x,y)
	print ("--------------------------------------------------")
	print ("ANSWER TO Q3")
	print ("Intercept and Slope for Confirmed : ")
	print(theta[1][0], theta[0][0])
	# plt.scatter(x,y, color='g', label='data')
	# plt.plot(x,hypothesis(theta,x), color='r', label='prediction')
	# plt.legend()
	# plt.show()
	confirmed_intercept = theta[0]
	confirmed_slope = theta[1]

	rx = np.array(rx)
	ry = np.array(ry)
	rx = rx.astype('int64')
	ry = ry.astype('int64')
	x = rx
	y = ry
	# theta = gradient_descent(x,y,learning_rate=0.00000001,maxIter=10000)
	x = np.reshape(x,(-1,1))
	x = np.concatenate((x,np.ones((len(x),1))),axis=1) # Adding a column of 1s to X array. Example - "To take care of c in case of y = mx + c"
	y = np.reshape(y,(-1,1)) # Conversion of 1D array to 2D
	theta = normal_equation(x,y)
	print ("Intercept and Slope for Recovered : ")
	print(theta[1][0], theta[0][0])
	# plt.scatter(x,y, color='g', label='data')
	# plt.plot(x,hypothesis(theta,x), color='r', label='prediction')
	# plt.legend()
	# plt.show()
	recovered_intercept = theta[0]
	recovered_slope = theta[1]

	dx = np.array(dx)
	dy = np.array(dy)
	dx = dx.astype('int64')
	dy = dy.astype('int64')
	x = dx
	y = dy
	# theta = gradient_descent(x,y,learning_rate=0.00000001,maxIter=10000)
	x = np.reshape(x,(-1,1))
	x = np.concatenate((x,np.ones((len(x),1))),axis=1) # Adding a column of 1s to X array. Example - "To take care of c in case of y = mx + c"
	y = np.reshape(y,(-1,1)) # Conversion of 1D array to 2D
	theta = normal_equation(x,y)
	print ("Intercept and Slope for Deceased : ")
	print(theta[1][0], theta[0][0])
	deceased_intercept = theta[0]
	deceased_slope = theta[1]
	# plt.scatter(x,y, color='g', label='data')
	# plt.plot(x,hypothesis(theta,x), color='r', label='prediction')
	# plt.legend()
	# plt.show()

	return confirmed_intercept, confirmed_slope, recovered_intercept, recovered_slope, deceased_intercept, deceased_slope


correct_date = True
while (not correct_date):
	print ("Enter the start date in the format yyyy-mm-dd")
	sd = input().split("-")
	if len(sd)!=3:
		print ("WRONG DATE !!!!!!!!")
		print ("Please enter correct start Date")
		continue
	try:
		start_date = date(int(sd[0]),int(sd[1]),int(sd[2]))
	except:
		print ("WRONG DATE !!!!!!!!")
		print ("Please enter correct start Date")
		continue
	correct_date = True

correct_date = True
while (not correct_date):
	print ("Enter the end date in the format yyyy-mm-dd")
	ed = input().split("-") #take input
	if len(ed)!=3:
		print ("WRONG DATE !!!!!!!!")
		print ("Please enter correct end date")
		continue
	try:
		end_date = date(int(ed[0]),int(ed[1]),int(ed[2]))
	except:
		print ("WRONG DATE !!!!!!!!")
		print ("Please enter correct end date")
		continue

	start_date = sd[0]+"-"+sd[1]+"-"+sd[2]
	end_date = ed[0]+"-"+ed[1]+"-"+ed[2]

	print ("Enter the file name for json data")
	json_file_path = "data.json" #take input
	if (json_file_path != 'data.json'):
		print ("The file path/name is wrong but don't worry we'll fetch data from internet")
	correct_date = True



start_date = "2020-03-14"
end_date = "2020-09-05"
# Q1_1('file_path.json', start_date, end_date)
# Q1_2('file_path.json', start_date, end_date)
# Q1_3('file_path.json', start_date, end_date)
# Q1_4('file_path.json', start_date, end_date)
# Q1_5('file_path.json', start_date, end_date)
# Q1_6('file_path.json', start_date, end_date)
# Q1_7('file_path.json', start_date, end_date)
Q2_1('file_path.json', start_date, end_date)
Q2_2('file_path.json', start_date, end_date)
Q2_3('file_path.json', start_date, end_date)
# Q3('file_path.json', start_date, end_date)
