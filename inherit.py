


class Employe:
    increment = 1.5
    num_emp = 0
    def __init__(self, name,lname, age , salry):
        self.name = name
        self.lname = lname
        self.age = age
        self.salry = salry
        self.email = name + '.' + str(age) +'_'+ lname + '@test.com'

        Employe.num_emp += 1
        # # print full nam or more than one variable with function
    
    def classfunc(self):
        print(self.name, self.lname)
        # return  '{} {}'.format(self.name, self.lname)
        return ('i am returning value')

    def all_raised(self):
        # self.age = int(self.age + 2)
        self.salry = int(self.salry * self.increment)


# if we chabge some changing on subclkasses it will not affect the parent class
class Develpor(Employe):
    increment = 2
    # also we can more type and category to Develpor class 
    def __init__(self, name, lname, age, salry, prog_lan):
        super().__init__(name, lname, age, salry)
        self.prog_leng = prog_lan

class Manager(Employe):
    increment = 1.1
    def __init__(self, name, lname, age, salry,employee = None):
        super().__init__(name, lname, age, salry)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee
    def add_employe(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)
    def remove_employe(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)
    def print_employe(self):
        for emp in self.employee:
            print("-->", emp.classfunc())
# Instance Variable
devEm = Develpor('Sarfraz', 'Jahan', 24, 10000, 'Python') 
# manger_emplye = Manager('Jahan', 'Sarfraz', 26, 25000, "Manager") 
third_emplye = Employe('Sarfi', 'User', 28, 35000) 
new_str = "Yousaf-Anwar-25-3000"
usman_str = "Usman-Maqbool-27-5456345"
mngr_1 = Manager('Jhon', 'Doe', 24, 10000, [devEm]) 
# print(mngr_1.email, 'i am printing email')
new_develpor = Develpor('New', 'Develpor', 24, 10000, 'html')
new_develpor1 = Develpor('New1', 'Develpor1', 26, 50000, 'React')

mngr_1.add_employe(new_develpor1)
print("I am just")
mngr_1.print_employe()

# print(new_develpor.email)
# print(devEm.email)
# subclass
# print(devEm.salry, "before Increment")
# devEm.all_raised()
# print(devEm.salry, "after increment")
# add another
# print(devEm.email)
# print(devEm.prog_leng)
# print(manger_emplye.salry,"before increment")
# manger_emplye.all_raised()
# print(manger_emplye.salry,"after increment")
# print(manger_emplye.email)
# print(manger_emplye.role)

print(Employe.num_emp)