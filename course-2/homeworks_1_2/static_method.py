class Shape:
	
	@staticmethod				#define a static method before initiating an instance
	def add_ally(x,y):
		x.append(y)
		return x

	
	def __init__(self, shape_type):
		self.shape_type=shape_type
		self.__allies=[]		#initiate a private empty list in an instance 

	@property
	def allies_public(self):	#make it accessible for the subclasses
		return self.__allies

	def __create_allies(self):	#create a private method that calls the static method defined above
		return self.add_ally(self.allies_public, self.object)

	@property					#make it accessible by the subclasses		
	def ally_list_p(self):
		return self.__create_allies()





class Circle(Shape):

	def __init__(self, shape_type):
		super().__init__(shape_type)
		self.object='square'	#define the second argument for the add_ally method
		self.ally_list_p		#call the add_ally method 
		self.object='other'		#repeat as many times as you want 
		self.ally_list_p
		
	
	def __str__(self):
		return "results: "+ str(self.allies_public)



def main():
	circle_test=Circle('circle')
	print(circle_test)

if __name__ == '__main__':
	main()