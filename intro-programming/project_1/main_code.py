import csv
import math
import statistics

filename = 'LBMA-GOLD_final.csv'



def unique_years():
	with open(filename, newline='') as csvfile:
		file_reader = csv.reader(csvfile, delimiter=',')
		for row in file_reader:
			years.add(int(row[1]))





def yearly_avg_stdev():
	with open(filename, newline='') as csvfile:
		file_reader = csv.reader(csvfile, delimiter=',')
		for year in years:
			list_year=[year] 
			for row in file_reader:
				row=[float(x) for x in row[1:5]]
				row[0]=int(row[0])
				if year==row[0]:
					list_year.append(row[2])
			length=len(list_year)
			total=sum(list_year[1:length])	
			avg=total/length
			stand_dev=statistics.stdev(list_year[1:length])
			max_price=max(list_year[1:length])
			print('Year '+str(year)+' - '+'Avg. Price: '+str(avg)+' | '+'Std. Dev: '+str(stand_dev)+' | Max. Price: '+str(max_price))
			csvfile.seek(0)




def diff_pm_am():
	with open(filename, newline='') as csvfile:
		file_reader = csv.reader(csvfile, delimiter=',')
		diff_values={}
		for row in file_reader:
			date=row[0]
			row=[float(x) for x in row[1:5]]
			diff_value=row[2]-row[1]
			diff_values[date]=diff_value
		max_value=max(diff_values.items(), key=lambda x:x[1])
		day=max_value[0]
		value=max_value[1]
		print('\n'+'The highest difference between the closing and opening price over 50 years in the United States was $'+str(value)+' (closing>opening) on '+str(day))





if __name__=="__main__":
	years=set()
	unique_years()
	yearly_avg_stdev()
	diff_pm_am()

