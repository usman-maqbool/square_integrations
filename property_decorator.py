class Employee:
    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age

    @property
    def fullname(self):
        return "{} {}".format(self.name, self.lname)
    
    @fullname.setter
    def fullname(self,names):
        name, lname = names.split(' ')
        self.name = name
        self.lname = lname



    @fullname.deleter
    def fullname(self):
        print("Name Deleted Value")
        self.name = None
        self.lname = None

    
    @property    
    def email(self):
        return "{}.{}_{}test@.com".format(self.name,self.lname,self.age)



emp_1 = Employee("Sarfraz", "Yousaf", 24)


emp_1.name = "Jahan"

emp_1.fullname = "sarfi ali"

# print(emp_1.name)
# print(emp_1.fullname())
print(emp_1.email)

print(emp_1.fullname)


del emp_1.fullname
print(emp_1.email)

emp_1.fullname = "sarfi ali"
print(emp_1.email)