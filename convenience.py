#convenience.py
import numpy as np
import pandas as pd


def month_year(months=[], years=[]):
	"""gets month and year lists and merges and returns array of date times"""
	#test
	#months=cyclists_per_month.month
	#years=cyclists_per_month.year
	#test
	
	#convert months to nummer if in string format
	if isinstance(months[0], basestring):	
		month_dict1={"january":1, "february":2, "march":3, "april":4, "may":5, "june":6,
			 "july":7, "august":8, "september":9, "october":10, "november":11, "december":12}
		months=months.apply(lambda x: x.lower())
		month_num=[]
		for i in months:
			month_num.append(month_dict1[i])

	#now join with year
	month_year={"month_num":month_num, "years":years}
	month_year= pd.DataFrame(data=month_year)
	month_year["month_year"]=month_year.apply(lambda x: "%s-%s" % (x["month_num"], x["years"]), axis=1)
	return pd.to_datetime(month_year["month_year"], format="%m-%Y")