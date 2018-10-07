class Employee:
    
    raise_amount = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    def email(self):
        return('{}.{}@email.com'.format(self.first,self.last))
    
    def fullname(self):
        return("{} {}".format(self.first,self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
        
class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print("--> ",emp.fullname())
    
dev_1 = Developer("Nicholas","Njihia",16600,"Python")
dev_2 = Developer("Miguna","Miguna",60000,"Politics")
mgr_1 = Manager("Sue","Wangechi",200000)
print(dev_1.__dict__)
print(dev_2.__dict__)
print(mgr_1.__dict__)

@classmethod
def set_raise_amt(cls,amount):
    cls.raise_amt = amount
Employee.set_raise_amt = 1.10



print(dev_1.email())
print(isinstance(mgr_1,Manager))
print(dev_2.fullname())
print(dev_2.email())