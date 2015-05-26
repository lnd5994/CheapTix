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
	def __init__(self, name, cprice, rprice, city, dtp, popularity, availtix, classification):
		self.name = name
		self.cprice = cprice
		self.rprice = rprice
		self.city = city
		self.dtp = dtp # Days until performance
		self.popularity = popularity
		self.availtix = availtix
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
		elif key == "popularity":
			return self.popularity
		elif key == "availtix":
			return self.availtix
		elif key == "classification":
			return self.classification
		else:
			raise AttributeError




def NearestNeighbor(train):
	Event_input = Event('test',10,25,'New York',10,10,10,'test_class')

	dataFrame = pd.read_csv(train, na_values=["?"])

	attributes = list(dataFrame.columns.values)
	classification_label = attributes[len(attributes) - 1]

	events = []

	for row in range(len(dataFrame)):
		events.append(Event(dataFrame.iloc[row][0], dataFrame.iloc[row][1], dataFrame.iloc[row][2], dataFrame.iloc[row][3], dataFrame.iloc[row][4], dataFrame.iloc[row][5], dataFrame.iloc[row][6], dataFrame.iloc[row][7]))

	first_event = events[0]
	lowest_dist=distance(Event_input, first_event)

	for event in events:
		dist = distance(event, Event_input)
		if dist <= lowest_dist:
			lowest_dist = dist
			choice = event

	Event_input.classification = choice.classification

	return Event_input.classification




def ThreeNearestNeighbor(train):
	Event_input = Event('test',10,25,'New York',10,10,10,'test_class')

	dataFrame = pd.read_csv(train, na_values=["?"])

	attributes = list(dataFrame.columns.values)
	classification_label = attributes[len(attributes) - 1]

	events = []

	for row in range(len(dataFrame)):
		events.append(Event(dataFrame.iloc[row][0], dataFrame.iloc[row][1], dataFrame.iloc[row][2], dataFrame.iloc[row][3], dataFrame.iloc[row][4], dataFrame.iloc[row][5], dataFrame.iloc[row][6], dataFrame.iloc[row][7]))
	
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
	d4 = math.pow((event1.popularity - event2.popularity),2)
	d5 = math.pow((event1.availtix - event2.availtix),2)
	# d6 = (event1.city == event2.city)^2


	return math.sqrt(d1 + d2 + d3 + d4 + d5)







