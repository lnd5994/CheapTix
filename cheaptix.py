import csv
# import seat_geek.py
import pandas as pd
import math
import numpy as np
import scipy.stats as stats
from collections import Counter




class Event(object):
	def __setattr__(self, name, value):
		self.__dict__[name] = value
	def __init__(self, name, cprice, rprice, city, dtp, vencap, classification):
		self.name = name
		self.cprice = cprice
		self.rprice = rprice
		self.city = city
		self.dtp = dtp # Days until performance
		self.vencap = vencap
		self.classification = classification
	def __getattr__(self, key):
		if key == "name":
			return self.name
		elif key == "cprice":
			return self.cprice
		elif key == "rprice":
			return self.rprice
		elif key == "city":
			return self.city
		elif key == "dtp":
			return self.dtp
		elif key == "vencap":
			return self.vencap
		elif key == "classification":
			return self.classification
		else:
			raise AttributeError


def RunNN(train, information):
	dataFrame = pd.read_csv(information, na_values=["?"])
	attributes = list(dataFrame.columns.values)
	classification_label = attributes[len(attributes) - 1]
	events = []
	for row in range(len(dataFrame)):
		events.append(Event(dataFrame.iloc[row][0], dataFrame.iloc[row][1], dataFrame.iloc[row][2], dataFrame.iloc[row][3], dataFrame.iloc[row][4], dataFrame.iloc[row][5], dataFrame.iloc[row][6]))
	i=0
	for each in events:
		print each.name, ': ', NearestNeighbor(train, each)
	# 	dataFrame.iloc[i][6] = NearestNeighbor(train, each)
	# 	i=i+1
	# dataFrame.to_csv('out.csv')
	# information = 'out.csv'

	return 1

def Run3NN(train, information):
	dataFrame = pd.read_csv(information, na_values=["?"])
	attributes = list(dataFrame.columns.values)
	classification_label = attributes[len(attributes) - 1]
	events = []
	for row in range(len(dataFrame)):
		events.append(Event(dataFrame.iloc[row][0], dataFrame.iloc[row][1], dataFrame.iloc[row][2], dataFrame.iloc[row][3], dataFrame.iloc[row][4], dataFrame.iloc[row][5], dataFrame.iloc[row][6]))
	i=0
	for each in events:
		dataFrame.iloc[i][6] = ThreeNearestNeighbor(train, each)
		i=i+1
	dataFrame.to_csv('out.csv', sep='/t')
	information = 'out.csv'

def CSV2event(inputline):
	dataFrame = pd.read_csv(inputline, na_values=["?"])
	attributes = list(dataFrame.columns.values)
	classification_label = attributes[len(attributes) - 1]
	event = Event(dataFrame.iloc[0][0], dataFrame.iloc[0][1], dataFrame.iloc[0][2], dataFrame.iloc[0][3], dataFrame.iloc[0][4], dataFrame.iloc[0][5], dataFrame.iloc[0][6])
	print event.classification
	return event

def NearestNeighbor(train, Event_input):
	dataFrame = pd.read_csv(train, na_values=["?"])

	attributes = list(dataFrame.columns.values)
	classification_label = attributes[len(attributes) - 1]

	events = []

	for row in range(len(dataFrame)):
		events.append(Event(dataFrame.iloc[row][0], dataFrame.iloc[row][1], dataFrame.iloc[row][2], dataFrame.iloc[row][3], dataFrame.iloc[row][4], dataFrame.iloc[row][5], dataFrame.iloc[row][6]))

	first_event = events[0]
	lowest_dist=distance(Event_input, first_event)

	for event in events:
		dist = distance(event, Event_input)
		if dist <= lowest_dist:
			lowest_dist = dist
			choice = event

	Event_input.classification = choice.classification

	return Event_input.classification




def ThreeNearestNeighbor(train, Event_input):

	dataFrame = pd.read_csv(train, na_values=["?"])

	attributes = list(dataFrame.columns.values)
	classification_label = attributes[len(attributes) - 1]

	events = []

	for row in range(len(dataFrame)):
		events.append(Event(dataFrame.iloc[row][0], dataFrame.iloc[row][1], dataFrame.iloc[row][2], dataFrame.iloc[row][3], dataFrame.iloc[row][4], dataFrame.iloc[row][5], dataFrame.iloc[row][6]))
	
	first_event = events[0]
	lowest_dist=distance(first_event, Event_input)

	neighbors = []

	for i in range(3):
		for event in events:
			dist = distance(event, Event_input)
			if dist <= lowest_dist:
				lowest_dist = dist
				choice = event
		neighbors.append(choice)
		events.remove(choice)
		first_event = events[0]
		lowest_dist=distance(first_event, Event_input)

	neighbor_classifications = []

	for i in range(len(neighbors)):
		n = neighbors[i]
		c = n.classification
		neighbor_classifications.append(c)

	data=Counter(neighbor_classifications)

	temp = data.most_common(1)

	Event_input.classification = temp[0][0]

	return Event_input.classification




def distance(event1, event2):
	# d0 = (event1.name == event2.name)^2
	d1 = math.pow((event1.cprice - event2.cprice),2)
	d2 = math.pow((event1.rprice - event2.rprice),2)
	d3 = math.pow((event1.dtp - event2.dtp),2)
	d4 = math.pow((event1.vencap - event2.vencap),2)
	# d6 = (event1.city == event2.city)^2


	return math.sqrt(d1 + d2 + d3 + d4)







