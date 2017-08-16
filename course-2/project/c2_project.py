import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sn



class ReadData():

	def __init__(self):
		self.file_train="~/desktop/project_data/train_data.csv"
		self.file_valid="~/desktop/project_data/valid_data.csv"
		self.train_data=pd.read_csv(self.file_train, sep=',')
		self.valid_data=pd.read_csv(self.file_valid, sep=',')
		



class ProcessData(ReadData):

	def __init__(self):
		super().__init__()
		self.test_prop=0.15

	def split_train(self):
		self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.train_data['content'], self.train_data['target'], test_size=self.test_prop, random_state=0)
		return [self.X_train, self.X_test, self.y_train, self.y_test]

	def split_valid(self):
		self.X_valid, self.X_empty, self.y_valid, self.y_empty = train_test_split(self.valid_data['content'], self.valid_data['target'], test_size=0.0, random_state=0)
		return [self.X_valid, self.y_valid]


	def vectorize_train(self): 
		self.X_train=self.split_train()[0]
		self.X_test=self.split_train()[1]
		self.count_vect = CountVectorizer(stop_words="english")
		self.X_train_counts = self.count_vect.fit_transform(self.X_train)
		self.tfidf_transformer = TfidfTransformer()
		self.X_train_tfidf = self.tfidf_transformer.fit_transform(self.X_train_counts)
		self.X_test_counts = self.count_vect.transform(self.X_test)
		self.X_test_tfidf = self.tfidf_transformer.transform(self.X_test_counts)
		return [self.X_train_tfidf, self.X_test_tfidf, self.count_vect, self.tfidf_transformer]

	
	def vectorize_valid(self):
		self.X_valid=self.split_valid()[0]
		self.count_vect=self.vectorize_train()[2]
		self.tfidf_transformer=self.vectorize_train()[3]
		self.X_valid_counts = self.count_vect.transform(self.X_valid)
		self.X_valid_tfidf = self.tfidf_transformer.transform(self.X_valid_counts)
		return self.X_valid_tfidf


class SVM(ProcessData):

	def __init__(self):
		super().__init__()


	def fit_svm(self):
		self.X_train_tfidf=self.vectorize_train()[0]
		self.y_train=self.split_train()[2]
		self.X_test_tfidf=self.vectorize_train()[1]
		self.y_test=self.split_train()[3]
		self.svm_clf = svm.LinearSVC(C=1.).fit(self.X_train_tfidf, self.y_train)
		self.pred_svm = self.svm_clf.predict(self.X_test_tfidf)
		self.recall_test=sklearn.metrics.recall_score(self.y_test, self.pred_svm)
		self.accuracy_test=sklearn.metrics.accuracy_score(self.y_test, self.pred_svm, normalize=True)
		return [self.recall_test, self.accuracy_test, self.svm_clf]

	def valid_svm(self):
		self.svm_clf=self.fit_svm()[2]
		self.X_valid_tfidf=self.vectorize_valid()
		self.pred_svm_valid = self.svm_clf.predict(self.X_valid_tfidf)
		self.recall_valid=sklearn.metrics.recall_score(self.y_valid, self.pred_svm_valid)
		self.accuracy_valid=sklearn.metrics.accuracy_score(self.y_valid, self.pred_svm_valid, normalize=True)
		return [self.recall_valid, self.accuracy_valid, self.pred_svm_valid]



	def cfm(self):
		self.predicted=self.valid_svm()[2]
		self.true=self.split_valid()[1]
		self.conf_matrix=confusion_matrix(self.true, self.predicted)
		self.index=['True Negative', 'True Positive']
		self.columns=['Pred Negative', 'Pred Positive']
		self.df_cm = pd.DataFrame(self.conf_matrix, index = [i for i in self.index], columns = [i for i in self.columns])
		self.plot=sn.heatmap(self.df_cm, annot=True, cbar=False, fmt='g')
		return [self.conf_matrix, self.plot]


	def output_data(self):
		self.result=pd.DataFrame(self.split_valid()[0])
		self.result['true_value']=self.split_valid()[1]
		self.preds=self.valid_svm()[2]
		self.result['predicted']=self.preds
		return self.result

	
	def __str__(self):
		return "SVM Model for Tag Cybersecurity\nTest Recall: " + str(self.fit_svm()[0])+ "%\nTest Accuracy: "+str(self.fit_svm()[1])+"%\nValidation Recall: "+ str(self.valid_svm()[0])+ "%\nValidation Accuracy: "+ str(self.valid_svm()[1])+ "%\nConfusion Matrix\n"+ str(self.cfm()[0])





def main():
	svm_model=SVM()
	print(svm_model)
	output_data=svm_model.output_data()
	print(output_data.head(n=3))
	output_data.to_csv("~/desktop/project_data/output_data.csv", sep=',', header=	True, encoding='utf-8')
	plot=svm_model.cfm()[1]
	plt.show(plot)
	
	

if __name__=="__main__":
	main()
