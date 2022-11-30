# def decotwtor(func1):
#     def dec1():
#         print ("I am just printing this")
#         func1()
#         print("Here Just Every thing is printing")
#     return dec1

# @decotwtor
# def another_dec():
#     print("My name is sarfraz")


# another_dec()



# def div(a, b):
#     print(a / b)

# def new_ddec(func):
#     def inner_dec(a, b):
#         if a < b:
#             a , b = b , a 
#         return func(a, b)
#     return inner_dec

# div1 = new_ddec(div)

# div1(2,4)



# def decor(text):
#     return text.upper()
# print(decor('hello'))

# yell = decor

# print(yell('world'))


# def greet(func):
#     greeting = func("In this example im just clearing the concept of decorator")
#     print(greeting)

# greet(decor)


# def upper(text):
#     return text.upper()
# def loewr(text):
#     return text.lower()

# def greet(func):
#     greeting = func("I am just taking the core idea of decorator")
#     print(greeting)

# greet(upper)
# greet(loewr)



# def addernmbr(x):
#     def adder(y):
#         return x+y
#     return adder

# add_nmbr = addernmbr(10)

# print(add_nmbr(25))


# def hello_decor(func):

#     def inner_decor():
#         print("I am before the printing")
#         func()
#         print("i Am printed")
#     return inner_decor


# def in_which():
#     print("i am that function that will be printed")


# in_which = hello_decor(in_which)

# in_which()



# import time , math


# def calculate_time(func):
#     def inner_cal(*args, **kwargs):
#         print('I am going to printing value')
#         begin = time.time()
#         print('Value is just begin', begin)
#         func(*args, **kwargs)
#         end = time.time()
#         print('value is just going to end', end)
#         print('total time in this',  end - begin)
#     return inner_cal


# @calculate_time
# def get_factorial(num):
#     time.sleep(5)
#     print(math.factorial(num))

# get_factorial(10)

# def get_sum_with_decor(func):
#     def inner_sum_decor(*args, **kwargs):
#         print("here sum function is going to print")
#         related_value = func( *args , **kwargs)

#         print('value after executuion')
#         return related_value

#     return inner_sum_decor

# @get_sum_with_decor
# def sum_of_nmbr(a, b):
#     print(':its insode a function')
#     return a + b

# a,b = 5,10

# print("calvulated values is", sum_of_nmbr(a,b))



def intro_decor(func):
    def inner():
        x = func()
        return x * x

    return inner

def sec_decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@intro_decor
@sec_decor
def mul_decors():
    return 10

print(mul_decors())



