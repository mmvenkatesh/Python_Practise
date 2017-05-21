class Employee(object):
	raise_amount=1.04
	employee_count=0
	def __init__(self,first,last,sal):
		#print self
		self.first=first
		self.last=last
		self.sal=sal
		self.email=first+'.'+last+'@gmail.com'
		Employee.employee_count+=1
		
			 
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
	
	def raise_sal(self):
		self.sal=int(self.sal*self.raise_amount)
		print self.sal

	@classmethod
	def raise_hike(cls,number):
		print cls
		cls.raise_amount=number

	@classmethod
	def from_string(cls,string_name):
		print cls
		first,last,sal=string_name.split('-')
		cls(first,last,int(sal)) 

	@staticmethod
	def is_workday(day):
		print day
		if day.weekday()==5 or day.weekday()==6:
			return False
		else:
			return True         

class Developer(Employee):
	def __init__(self,first,last,sal,pgm_lang):
		super(Developer,self).__init__(first,last,sal)
		self.pgm_lang=pgm_lang

class Manager(Employee):
	def __init__(self,first,last,sal,employees=None):
		super(Manager,self).__init__(first,last,sal)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print emp.fullname()					
			




dev_1=Developer('Manikanta','venkatesh',30000,'python')
dev_2=Developer('test','user',20000,'java')
print dev_1

mgr_1=Manager('new','data',3000,None)
print mgr_1.employees

mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_1)

print mgr_1.print_emps()

#print dev_1.fullname()

#print dev_1.email
#print dev_2.email
#print dev_1.pgm_lang
#print dev_2.pgm_lang




#print help(Developer)
#print dev_1.__dict__
#print dev_1.email
#print dev_1.sal
#print dev_1.raise_sal()

#dev_1.raise_amount=11.23
#print dev_1.__dict__
#print dev_1.raise_sal()








		
		
