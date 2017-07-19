import csv
import math
import statistics
import re


#LBMA-GOLD_final

filename = 'LBMA-GOLD_final.csv'

#Get a set of unique year values from the file

def unique_years():
	years_raw=set()
	with open(filename, newline='') as csvfile:
		file_reader = csv.reader(csvfile, delimiter=',')
		for row in file_reader:
			years_raw.add(int(row[1]))
	years_raw=list(years_raw)
	years_raw.sort()
	years=[str(x) for x in years_raw]
	return years

	
#Make a new dictionary for year and closing price pair

def new_dict():
	with open(filename, newline='') as csvfile:
		file_reader = csv.reader(csvfile, delimiter=',')
		years_values={}
		for row in file_reader:
			years_values[row[0]]=[float(row[3]), (float(row[3])-float(row[2]))]
	return years_values





#Extract in a list values that have a particular year present thei keys 

def calcs():
	years=unique_years()
	years_values=new_dict()
	for y in years:
		cprices = [value[0] for key, value in years_values.items() if re.findall('[\d]{4}', key)==[y] ]
		max_price=max(cprices)
		avg = statistics.mean(cprices)
		stand_dev=statistics.stdev(cprices)
		print('Year '+str(y)+' - '+'Avg. Price: '+str(avg)+' | '+'Std. Dev: '+str(stand_dev)+' | Max. Price: '+str(max_price))
	diffs_all= {key:value[1] for key, value in years_values.items()}	
	max_diff_all=max(diffs_all.items(), key=lambda x:x[1])
	day_all=max_diff_all[0]
	value_all=max_diff_all[1]
	print('\n'+'The highest difference between the closing and opening price over 50 years in the United States was $'+str(value_all)+' (closing>opening) on '+str(day_all))
	return None

if __name__=="__main__":
	unique_years()
	new_dict()
	calcs()

	
	
