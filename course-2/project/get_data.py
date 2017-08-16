import pysolr
import requests
import codecs
import pandas as pd


class GetData:

	conn = pysolr.Solr('https://cabidx1:Jkxkk3-POIO08723_eWWXeei1078TRw,6QI@aws-ec2-va-solr-4-10-cabinet.opensolr.com/solr/cab1')

	def __init__(self):
		self.tids=['1772']

	def get_train_data(self):
		for tid in self.tids:
			self.positives_train = GetData.conn.search('*:*',fq='im_field_regulated_activities:%s' % tid, fl='entity_id, label,content', sort='entity_id asc', start=0, rows=300)
			self.negatives_train = GetData.conn.search('*:*',fq='-im_field_regulated_activities:%s' % tid, fl='entity_id, label,content', sort='entity_id asc', start=0, rows=300)

		self.d_train = []

		for p in self.positives_train:
			self.content= p['label']+ p['content']
			self.entity_id = p['entity_id']
			self.d_train.append((self.entity_id, self.content, 1))

		for n in self.negatives_train:
 			self.content= n['label']+n['content']
 			self.entity_id=n['entity_id']
 			self.d_train.append((self.entity_id, self.content, 0))
		
		self.data_train = pd.DataFrame(self.d_train, columns=('entity_id', 'content', 'target'))
		return self.data_train



	def get_valid_data(self):
		for tid in self.tids:
			self.positives_valid = GetData.conn.search('*:*',fq='im_field_regulated_activities:%s' % tid, fl='entity_id, label,content', sort='entity_id asc', start=301, rows=182)
			self.negatives_valid = GetData.conn.search('*:*',fq='-im_field_regulated_activities:%s' % tid, fl='entity_id, label,content', sort='entity_id asc', start=301, rows=200)

		self.d_valid = []

		for p in self.positives_valid:
			self.content= p['label']+ p['content']
			self.entity_id = p['entity_id']
			self.d_valid.append((self.entity_id, self.content, 1))

		for n in self.negatives_valid:
 			self.content= n['label']+n['content']
 			self.entity_id=n['entity_id']
 			self.d_valid.append((self.entity_id, self.content, 0))
		
		self.data_valid = pd.DataFrame(self.d_valid, columns=('entity_id', 'content', 'target'))
		return self.data_valid
		


if __name__=="__main__":
	get=GetData()
	train_data=get.get_train_data()
	train_data.to_csv("~/desktop/project_data/train_data.csv", sep=',', header=	True, encoding='utf-8')
	valid_data=get.get_valid_data()
	valid_data.to_csv("~/desktop/project_data/valid_data.csv", sep=',', header=	True, encoding='utf-8')
