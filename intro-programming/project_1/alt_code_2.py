
import csv
import sys
from sys import argv
import math
import statistics


filename = 'LBMA-GOLD_final_1.csv'

raw_file = open(filename)

file_reader = csv.DictReader(raw_file, delimiter=',')


def inputs():
	while True:
		try:
			x = int(input("Please enter year number in 4 digits:"))
			break
		except ValueError:
			print("Seriously, numbers...")
	return x



def yearly_stats(y):
	closing_prices=[]
	diff_values=[]
	for row in file_reader:
		row=dict((k, float(v)) for k, v in row.items() if k!='Date')  
		if inputs==int(row['Year']):
			closing_prices.append(row['USD_PM'])
			diff_pm_am=row['USD_PM']-row['USD_AM']
			diff_values.append(diff_pm_am)
	num_values=len(closing_prices)
	total= sum(closing_prices)
	avg=math.ceil(total/num_values)
	stand_dev=math.ceil(statistics.stdev(closing_prices))
	max_diff=math.ceil(max(diff_values))
	print('Statistics for year '+str(inputs))
	print('Average Price: $'+str(avg))
	print('Standard Dev: '+str(stand_dev))
	print('Max. difference in opening and closing prices: $'+str(max_diff))




if __name__ =="__main__":
	inputs=inputs()
	yearly_stats(inputs)
	

