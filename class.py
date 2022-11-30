# # define the Vehicle class
# class Vehicle:
#     name = ""
#     kind = "car"
#     color = ""
#     value = 100.00
#     def description(self):
#         desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
#         return desc_str

# # your code goes here
# car1 = Vehicle()
# car1.name = "Fer"
# car1.color = "red"
# car1.kind = "convertible"
# car1.value = 60000.00

# car2 = Vehicle()
# car2.name = "Jump"
# car2.color = "blue"
# car2.kind = "van"
# car2.value = 10000.00

# # test code
# print(car1.description())
# print(car2.description())



# __init__ function

# class Persone:
#     def __init__(self,age,name):
#         self.sarf_age = age
#         self.sarf_name=name
    
    
#     # # str function
#     # def __str__(self):
#     #     return f'{(self.sarf_age), self.sarf_name}'


#     # initialize  function in class as object
#     def myclassFunction(self):
#         print('My Name is ' + self.sarf_name , 'My Age is ' + str(self.sarf_age))

# p = Persone(24,'Sarfraz')

# print(p)
# p.myclassFunction()



class Employe:

    # bennifit of class variaable is that we can change it anytym and any place
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
        # print(self.name, self.lname)
        # return  '{} {}'.format(self.name, self.lname)
        return (self.name, self.lname,'i am returning value')

    def all_raised(self):
        # self.age = int(self.age + 2)
        self.salry = int(self.salry * self.increment)

    def __repr__(self):
        return "Employe('{}', '{}', '{}')".format(self.name, self.lname, self.email)

    def __str__(self):
        return '{} - {}'.format(self.classfunc(), self.email)
#     @classmethod
#     def all_increment_class_method(cls,amount):
#         cls.increment = amount

#     # Adding employe with class method
#     @classmethod
#     def add_emp_with_class_method(cls, emp_str):
#         name, lname,age,salry = emp_str.split('-')
#         return cls(name,lname,age,salry)

#     @staticmethod
#     def is_day_work(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return (":Its Holiday",False)

#         return (":Its workind daye",True)

# import datetime

# date_time = datetime.date(2022, 11, 27)

# print(Employe.is_day_work(date_time))






# Instance Variable
first_emplye = Employe('Sarfraz', 'Jahan', 24, 10000) 
seconed_emplye = Employe('Jahan', 'Sarfraz', 26, 25000) 
seconed_emplye = Employe('Sarfi', 'User', 28, 35000) 
new_str = "Yousaf-Anwar-25-3000"
usman_str = "Usman-Maqbool-27-5456345"

print(first_emplye)


# print(first_emplye.name, first_emplye.lname)
# print(first_emplye.email)
# print(seconed_emplye.email)
# first_emplye.classfunc()
# print(Employe.classfunc(first_emplye))
# print(Employe.classfunc(seconed_emplye))


# # # all_raised Exapmle
# print(first_emplye.age)
# # bennifit of class variable
# first_emplye.increment = 2

# # Usage of class variable
# first_emplye.all_raised()
# seconed_emplye.all_raised()
# print(seconed_emplye.salry)
# print(first_emplye.salry)


# classMethod
# Employe.all_increment_class_method(4)
# print(first_emplye.increment, "Its total value")
# first_emplye.all_raised()
# print(first_emplye.age)
# print(first_emplye.salry, 'Its salery after class method')
# print(Employe.num_emp, "total number of emplyes")


# Statically add Employe

# name, lname,age,salry = new_emp.split('-')
# new_emp = Employe(name,lname,age,salry)

# print(new_emp.email)
# print(new_emp.name)

# print(Employe.num_emp, "total number of emplyes")

# Adding Value with class method decorator
# new_emp = Employe.add_emp_with_class_method(new_str)
# usman_emp = Employe.add_emp_with_class_method(usman_str)

# print(usman_emp.name)
# print(usman_emp.email)

# print(Employe.num_emp)




