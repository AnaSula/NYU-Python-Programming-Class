#!/usr/bin/env python3

import json
import csv
import yaml
import pprint



#read csv input file (created manually) as dictionary

input_dict = csv.DictReader(open("io_input.csv"))


#create list from dictreader

dict_list=[]

for row in input_dict:
	dict_list.append(row)


#dump to JSON

input_json="input.json"

with open(input_json, 'w') as file_json:
	json.dump(dict_list,file_json)


#dump to YAML

input_yaml="input.yaml"

with open(input_yaml, 'w') as file_yaml:
	output = yaml.dump(dict_list, default_flow_style=True, explicit_start=True)
	yaml.dump(output,file_yaml)


#read csv file as a whole string

with open("io_input.csv") as csv_file:
    data_csv = csv_file.read()
    

#read json file as a whole string

with open("input.json", 'r') as json_file:
	data_json = json.load(json_file)
	

#read yaml file as a whole string

with open("input.yaml", 'r') as yaml_file:
	data_yaml = yaml.load(yaml_file)
	

#create a super dictionary 

super_dict={'csv':data_csv, 'json': data_json, 'yaml':data_yaml}

print(super_dict)
	
