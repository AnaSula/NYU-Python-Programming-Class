
class Shape:

"""Abstract Base Shape"""

	def __init__(self, shape_type):
		self.shape_type=shape_type
		self.allies=[]
		self.enemies=[]

	
	def add_ally(self, shape_object):
		self.allies.append(shape_object)
		return self.allies

		
	def add_enemy(self, shape_object):
		self.enemies.append(shape_object)
		return self.enemies

	def __str__(self):
		return "Shape: "+self.shape_type+"\n"


class Triangle(Shape):

"""Subclass Triangle"""

	@staticmethod
	def __area_private(a):
		return ((3**0.5) / 4)*a**2
	
	@staticmethod
	def __perim_private(a):
		return (a*3)/2

	def __init__(self, shape_type, name, edge_length):
		super().__init__(shape_type)
		self.name=name
		self.edge_length=edge_length
		self.__allies=self.add_ally('Circle')
		self.__enemies=self.add_enemy('Square')
		self.__role="aggressive and prone to violence"
		self.__area_value=self.__class__.__area_private(self.edge_length)
		self.__perim_value=self.__class__.__perim_private(self.edge_length)
		return

	@property
	def ally_public(self):
		return self.__allies

	@property
	def enemy_public(self):
		return self.__enemies

	@property
	def area_public(self):
		return self.__area_value 

	@property
	def perim_public(self):
		return self.__perim_value

	@property
	def role_public(self):
		return self.__role


	def __str__(self):
		return super().__str__()+"Shape Name: "+self.name+"\nRole: "+self.role_public+"\nAllies: "+str(self.ally_public[0])+"\nEnemies: "+str(self.enemy_public[0])+"\nArea: "+str(self.area_public)+"\nPerimeter: "+str(self.perim_public)





class Square(Shape):

"""Subclass Square"""

	@staticmethod
	def __area_private(a):
		return a**2
	
	@staticmethod
	def __perim_private(a):
		return 4*a

	def __init__(self, shape_type, name, edge_length):
		super().__init__(shape_type)
		self.name=name
		self.edge_length=edge_length
		self.__role="complacent and bureaucratic"
		self.__allies=self.add_ally('None')
		self.__enemies=self.add_enemy('Triangle, Circle')
		self.__area_value=self.__class__.__area_private(self.edge_length)
		self.__perim_value=self.__class__.__perim_private(self.edge_length)
		return

	@property
	def ally_public(self):
		return self.__allies

	@property
	def enemy_public(self):
		return self.__enemies


	@property
	def area_public(self):
		return self.__area_value 


	@property
	def perim_public(self):
		return self.__perim_value

	@property
	def role_public(self):
		return self.__role

	
	def __str__(self):
		return super().__str__()+"Shape Name: "+self.name+"\nRole: "+self.role_public+"\nAllies: "+str(self.ally_public[0])+"\nEnemies: "+str(self.enemy_public[0])+"\nArea: "+str(self.area_public)+"\nPerimeter: "+str(self.perim_public)




class Circle(Shape):

"""Subclass Circle"""

	@staticmethod
	def __area_private(r):
		return r**2*3.14
	
	@staticmethod
	def __perim_private(r):
		return 2*r*3.14


	def __init__(self, shape_type, name, radius):
		super().__init__(shape_type)
		self.name=name
		self.radius=radius
		self.__role="wise and noble"
		self.__allies=self.add_ally('Triangle')
		self.__enemies=self.add_enemy('Square')
		self.__area_value=self.__class__.__area_private(self.radius)
		self.__perim_value=self.__class__.__perim_private(self.radius)
		return

	@property
	def ally_public(self):
		return self.__allies

	@property
	def enemy_public(self):
		return self.__enemies

	@property
	def area_public(self):
		return self.__area_value 

	@property
	def perim_public(self):
		return self.__perim_value

	@property
	def role_public(self):
		return self.__role


	def __str__(self):
		return super().__str__()+"Shape Name: "+self.name+"\nRole: "+self.role_public+"\nAllies: "+str(self.ally_public[0])+"\nEnemies: "+str(self.enemy_public[0])+"\nArea: "+str(self.area_public)+"\nCircumference: "+str(self.perim_public)



def main():
	triangle_1=Triangle('Triangle', 'Equilateral Triangle', 2)
	print(triangle_1)
	square_1=Square('Square', 'Boring Sqaure', 3)
	print(square_1)
	circle_1=Circle('Circle', 'Wise Circle', 1 )
	print(circle_1)



if __name__ == '__main__':
	main()