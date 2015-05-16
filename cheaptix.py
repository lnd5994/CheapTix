

import csv
import pandas as pd
import math
import numpy as np
import scipy.stats as stats
from collections import Counter




class Event(object):
	def __setattr__(self, name, value):
		self.__dict__[name] = value
	def __init__(self, name, classification, cprice, rprice, city, dtp, popularity, availtix):
		self.cprice = cprice
		self.rprice = rprice
		self.city = city
		self.dtp = dtp # Days until performance
		self.popularity = popularity
		self.availtix = availtix
	def __getattr__(self, key):
		if key == "classification":
			return self.classification
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
		else:
			raise AttributeError




def NearestNeighbor(train, Event):
	dataFrame = pd.read_csv(train, na_values=["?"])
	dataFrameValidate = pd.read_csv(validate)

	attributes = list(dataFrame.columns.values)
	classification_label = attributes[len(attributes) - 1]

	events = # here we need to make a vector of events from the csv file

	first_event = events(1)
	lowest_dist=distance(Event, first_event)

	for event in events:
		dist = distance(event, Event)
		if dist < lowest_dist:
			lowest_dist = dist
			choice = event

	Event.classification = choice.classification

	return Event.classification




	def ThreeNearestNeighbor(train, Event):
	dataFrame = pd.read_csv(train, na_values=["?"])
	dataFrameValidate = pd.read_csv(validate)

	attributes = list(dataFrame.columns.values)
	classification_label = attributes[len(attributes) - 1]

	events = # here we need to make a vector of events from the csv file
	
	lowest_dist=10000000000

	neighbors = []

	for i in range(3):
		for event in events:
			dist = distance(event, Event)
			if dist < lowest_dist:
				lowest_dist = dist
				choice = event
		neighbors.append(choice)
		events.remove(choice)

		lowest_dist=10000000000

	neighbor_classifications = []

	for i in rage(len(neighbors)):
		n = neighbors(i)
		c = n.classification
		neighbor_classifications.append(c)

	data=Counter(neighbor_classifications)

	Event.classification = data.most_common(1)

	return Event.classification




def distance(event1, event2):
	d1 = (event1.cprice - event2.cprice)^2
	d2 = (event1.rprice - event2.rprice)^2
	d3 = (event1.dtp - event2.dtp)^2
	d4 = (event1.popularity - event2.popularity)^2
	d5 = (event1.availtix - event2.availtix)^2
	d6 = # distance between two cities

	return sqrt(d1 + d2 + d3 + d4 + d5 + d6)







