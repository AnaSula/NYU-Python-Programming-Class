import sys
from termcolor import colored

class EmptyString(Exception):
	pass

class Person:

	@staticmethod
	def empty_input(x,y,z):
		if x == "" or y=="" or z=="": 
			raise EmptyString


	def __init__(self):

		self.correct_values=['a','b','c','d','e','f','g']
	
		while True:
			self.fname=input("First name: ")
			self.lname=input("Last name: ")
			self.age=input("Age: ")
			try:
				self.__class__.empty_input(self.fname, self.lname, self.age)
				break
			except EmptyString:
				print(colored("As a reminder, you haven't provided your personal information.", 'blue'))
			return



	def __str__(self):
		return "Personality Test for "+ self.fname+" "+self.lname+", "+str(self.age)+" years old."


class Illegal(Exception):
	pass


class Questions(Person):


	@staticmethod
	def wrong_input(x,y):
		if x not in y:
			raise Illegal


	def __init__(self):
		super().__init__()	
		self.score=[]
		
		while True:
			self.q1=input("1. When do you feel your best?\n(a) in the morning\n(b) during the afternoon & early evening\n(c) late at night \n")
			self.q1=(self.q1.lower()).strip()
			try:
				self.__class__.wrong_input(self.q1, self.correct_values)
				break
			except Illegal:
				print(colored("Wrong value provided as an answer. Please, enter the letter corresponding to your answer.", 'red'))

		while True:
			self.q2=input("2. You usually walk \n(a) fairly fast, with long steps\n(b) fairly fast, with short, quick steps\n(c) less fast head up, looking the world in the face\n(d) less fast, head down\n(e) very slowly\n")
			self.q2=(self.q2.lower()).strip()
			try:
				self.__class__.wrong_input(self.q2, self.correct_values)
				break
			except Illegal:
				print(colored("Wrong value provided as an answer. Please, enter the letter corresponding to your answer.", 'red'))	

		while True:
			self.q3=input("3. When talking to people you\n(a) stand with your arms folded\n(b) have your hands clasped\n(c) have one or both your hands on your hips\n(d) touch or push the person to whom you are talking\n(e) play with your ear, touch your chin, or smooth your hair\n")
			self.q3=(self.q3.lower()).strip()
			try:
				self.__class__.wrong_input(self.q3, self.correct_values)
				break
			except Illegal:
				print(colored("Wrong value provided as an answer. Please, enter the letter corresponding to your answer.", 'red'))	
		
		while True:
			self.q4=input("4. When relaxing, you sit with\n(a) your knees bent with your legs neatly side by side\n(b) your legs crossed\n(c) your legs stretched out and straight\n(d) one leg curled under you\n")
			self.q4=(self.q4.lower()).strip()
			try:
				self.__class__.wrong_input(self.q4, self.correct_values)
				break
			except Illegal:
				print(colored("Wrong value provided as an answer. Please, enter the letter corresponding to your answer.", 'red'))
		
		while True:
			self.q5=input("5. When something really amuses you, you react with \n(a) a big, appreciative laugh\n(b) a laugh, but not a loud one\n(c) a quiet chuckle\n(d) a sheepish smile\n")
			self.q5=(self.q5.lower()).strip()
			try:
				self.__class__.wrong_input(self.q5, self.correct_values)
				break
			except Illegal:
				print(colored("Wrong value provided as an answer. Please, enter the letter corresponding to your answer.", 'red'))

		while True:
			self.q6=input("6. When you go to a party or social gathering you... \n(a) make a loud entrance so everyone notices you\n(b) make a quiet entrance so everyone notices you\n(c) make the quietest entrance, trying to stay unnoticed\n")
			self.q6=(self.q6.lower()).strip()
			try:
				self.__class__.wrong_input(self.q6, self.correct_values)
				break
			except Illegal:
				print(colored("Wrong value provided as an answer. Please, enter the letter corresponding to your answer.", 'red'))

		while True:
			self.q7=input("7. You're working very hard and you're interrupted. Do you...\n(a) welcome the break\n(b) feel extremely irritated\n(c) vary between these two extremes\n")
			self.q7=(self.q7.lower()).strip()
			try:
				self.__class__.wrong_input(self.q7, self.correct_values)
				break
			except Illegal:
				print(colored("Wrong value provided as an answer. Please, enter the letter corresponding to your answer.", 'red'))

		while True:
			self.q8=input("8. Which of the following colors do you like the most?\n(a) red or orange\n(b) black\n(c) yellow or light blue \n(d) green\n(e) dark blue or purple\n(f) white\n(g) brown or gray\n")
			self.q8=(self.q8.lower()).strip()
			try:
				self.__class__.wrong_input(self.q8, self.correct_values)
				break
			except Illegal:
				print(colored("Wrong value provided as an answer. Please, enter the letter corresponding to your answer.", 'red'))

		while True:
			self.q9=input("9. In those last few moments before going to sleep, lie..\n(a) stretched out on your back\n(b) stretched out face down on your stomach\n(c) on your side, slightly curled\n(d) with your head on one arm\n(e) with your head under the covers\n")
			self.q9=(self.q9.lower()).strip()
			try:
				self.__class__.wrong_input(self.q9, self.correct_values)
				break
			except Illegal:
				print(colored("Wrong value provided as an answer. Please, enter the letter corresponding to your answer.", 'red'))

		while True:
			self.q10=input("10. You often dream that you are...\n(a) falling\n(b) fighting or struggling\n(c) searching for something or somebody \nd) flying or floating \n(e) you usually have dreamless sleep\n(f) your dreams are always pleasant\n")
			self.q10=(self.q10.lower()).strip()
			try:
				self.__class__.wrong_input(self.q10, self.correct_values)
				break
			except Illegal:
				print(colored("Wrong value provided as an answer. Please, enter the letter corresponding to your answer.", 'red'))
		
		

	def qs(self):
		if self.q1=='a':
			self.score.append(2)
		elif self.q1=='b':
			self.score.append(4)
		else:
			self.score.append(6)

		if self.q2=='a':
			self.score.append(6)
		elif self.q2=='b':
			self.score.append(4)
		elif self.q2=='c':
			self.score.append(7)
		elif self.q2=='d':
			self.score.append(2)
		else:
			self.score.append(1)

		if self.q3=='a':
			self.score.append(4)
		elif self.q3=='b':
			self.score.append(2)
		elif self.q3=='c':
			self.score.append(5)
		elif self.q3=='d':
			self.score.append(7)
		else:
			self.score.append(6)
		
		if self.q4=='a':
			self.score.append(4)
		elif self.q4=='b':
			self.score.append(6)
		elif self.q4=='c':
			self.score.append(2)
		else:
			self.score.append(1)
		
		if self.q5=='a':
			self.score.append(6)
		elif self.q5=='b':
			self.score.append(4)
		elif self.q5=='c':
			self.score.append(3)
		elif self.q5=='d':
			self.score.append(5)
		else:
			self.score.append(2)
	
		if self.q6=='a':
			self.score.append(6)
		elif self.q6=='b':
			self.score.append(4)
		else:
			self.score.append(2)
	
		if self.q7=='a':
			self.score.append(6)
		elif self.q7=='b':
			self.score.append(2)
		else:
			self.score.append(4)
		
		if self.q8=='a':
			self.score.append(6)
		elif self.q8=='b':
			self.score.append(7)
		elif self.q8=='c':
			self.score.append(5)
		elif self.q8=='d':
			self.score.append(4)
		elif self.q8=='e':
			self.score.append(3)
		elif self.q8=='f':
			self.score.append(2)
		else:
			self.score.append(1)
		
		if self.q9=='a':
			self.score.append(7)
		elif self.q9=='b':
			self.score.append(6)
		elif self.q9=='c':
			self.score.append(4)
		elif self.q9=='d':
			self.score.append(2)
		else:
			self.score.append(1)
		
		if self.q10=='a':
			self.score.append(4)
		elif self.q10=='b':
			self.score.append(2)
		elif self.q10=='c':
			self.score.append(3)
		elif self.q10=='d':
			self.score.append(5)
		elif self.q10=='e':
			self.score.append(6)
		else:
			self.score.append(1)
		return self.score



class Results(Questions):

	def __init__(self):
		super().__init__()
		self.total_score=sum(self.qs())


	def answer(self):
		self.result=''
		if self.total_score>60:
			self.result='Others see you as somebody they should "handle with care". You are seen as vain, self-centered, and who is extremely dominant. Others may admire you, wishing they could be more like you, but do not always trust you, hesitating to become too deeply involved with you.'
		elif 51<=self.total_score<=60:
			self.result='Others see you as an exciting, highly volatile, rather impulsive personality; a natural leader, who is quick to make decisions, though not always the right ones. They see you bold and adventuresome, someone who will try anything once; someone who takes chances and enjoys adventure. They enjoy being in your company because of the excitement you radiate.'
		elif 41<=self.total_score<=50:
			self.result='Others see you as fresh, lively, charming, amusing, and always interesting; someone who is constantly in the center of attention, but sufficiently well-balanced not to let it go to their head. They also see you as kind, considerate, and understanding; someone who will always cheer them up and help them out.'
		elif 31<=self.total_score<=40:
			self.result='Others see you as sensible, cautious, careful and practical. They see you as clever, gifted, or talented, but modest. Not a person who makes friends too quickly or easily, but someone who is extremely loyal to friends you do make and who expect the same loyalty in return. Those who really get to know you realize it takes a lot to shake your trust in your friends, but equally that it takes you a long time to get over it if that trust is ever broken'	
		elif 21<=self.total_score<=30:
			self.result="Your friends see you as painstaking and fussy. They see you as very cautious, extremely careful... A slow and steady plodder. It'd really surprise them if you ever did something impulsively or on the spur of the moment, expecting you to examine everything carefully from every angle and then, usually decide against it. They think this reaction is caused partly by your careful nature."
		else:
			self.result="People think you are shy, nervous, and indecisive someone who needs looking after, who always wants someone else to make the decisions and who doesn't want to get involved with anyone or anything. They see you as a worrier who always sees problems that don't exist. Some people think you're boring. Only those who know you well know that you aren't."
		return self.result


	def __str__(self):
		return super().__str__()+"\nYour scores for this test is "+str(self.total_score)+"."+"\nExplanation: \n"+str(self.answer())



def main():
	person_1=Results()
	print(person_1)
	


if __name__ == '__main__':
	main()