class Student:
	def __init__(self, str, a, b, c):
		self.name = str
		self.m1 = a
		self.m2 = b
		self.m3 = c

	def __eq__(self,other):
		if self.m1==other.m1 and self.m2==other.m2	and self.m3==other.m3:
			return True
		else:
			return False

		#return ((self.m1==other.m1) and (self.m2==other.m2)	and (self.m3==other.m3))		
	def __gt__(self,other):
		return ((self.m1>other.m1) and (self.m2>other.m2)	and (self.m3>other.m3))		
def main():
	obj1 = Student("Piyush",70,91,80)
	obj2 = Student("Servesh",56,89,78)
	if obj1 == obj2 :
		print("Both the students are same")
	else:
		print("Both the students are different")

	if obj1 > obj2 :
		print("First object is greater")
	else:
		print("Second object is greater")
	
if __name__ == '__main__':
		main()	