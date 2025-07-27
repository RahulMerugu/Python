from functools import reduce  #this is for the reduce function

name = 'Cat'
phrase = name + 'is my pet'  #concatenation
print (phrase)

age = 12
age2 = float(age)  #type conversion
print (type(name))  # type is used to check datatype of a variable
print (isinstance(age, int))   # isinstance is used to check if entered variable is of same datatype as datatype entered
print (isinstance(age2, float))

def Ternary():   #ternary operation
    return 'Adult' if age > 18 else 'Child'
print (Ternary())

print ("""Cat 
       
is   
       
chubby""")   #  """" is used for multiline string

print(name.upper()) #used to convert a string into uppercase

print ('at' in name)  #used to check if a substring is present in a string 

print ('It\'s a cat!')  # \ is used to allow single and double quotes inside of strings

name2 = 'Cat\nty'  # \n is used to go to next line, even in the middle of a string
print (name2)

print (name[1:3])  # this is called slicing, it only outputs the charcters at the positions present in this range in [] brackets


book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read])  #any gives true of any of the entities is true
print (read_any_book)

read_all_books = all([book_1_read, book_2_read])  #all only returns true of all entities have true values
print (read_all_books)


num1 = 2 + 3j  #j is used to denote imaginary part of a number
num2 = complex (2,3)  #complex function can also be used to denote imaginary numbers, the 1st number in () is real, and the 2nd is imaginary
print (num1)
print (num2)
print (num2.real, num2.imag)


from enum import Enum  # enum is used to create constants. The values assigned will never change
class State(Enum):
    inactive=0  
    active=1

print (State.active.value)
print (State.inactive.value)
print (len(State))  #gives the number of constants in the State enum
print (State['active'].value)  #another way of giving the same output as State.active.value
print (list(State))  # list will list all the values stored in the enum State


dogs = ['Roger' , 'Syd' , 1 , True]
print ("Roger" in dogs)  #searching for Roger in dogs, returns True
print (dogs[2])
dogs[2] = "Beau"
print (dogs)
dogs += ['Quincy' , 7]  #can add multiple new values of different data types to the list
print (dogs)
print (dogs.pop())  #removes last value stored in list
print (dogs)
dogs.insert(2 , 'best')
print (dogs)
dogs.remove(1)
print (dogs)
print (sorted(dogs , key = str.lower))  #sorts the entities by alphabetical, Upper case before lower case, but using key, we can make lowercase come before uppercase


cats = {"name" : "Floof" , "age" : 5}  #dictionary
print (cats['name'])
print (list(cats.items()))


set1 = {"Roger" , 'Syd'}  #sets
set2 = {'Roger'}
mod = set1 | set2   #union is denoted with |
print (mod)
mod = set1 > set2  #> is used to check set1 is bigger than set2
print (mod)


age3 = 8
print (age3.real)  #returns real part of the value
print (age3.imag)  #returns imaginary part of the value
print (age3.bit_length())  #returns the bit length of the value

items = [1 , 2]
items.append(3)
items.pop()
print (id(items))  #returns address of the value

items2 = [1 ,2 ,3 ,4]
for item in items2:
    print (item)

items3 = ['beau' , 'ram' , 'sam']
for index, item in enumerate(items3):
    print (index, item)


class Animal:  #creation of a class
    def walk(self):
        print("walking...")

class Dog(Animal):  #usage of inheritance
    def __init__(self, name4, age4):  #This is a Constructor
        self.name4 = name4
        self.age4 = age4
    def bark(self):
        print ('woof')

roger = Dog("Roger" , 8)
print (type(roger))
print (roger.name4)
print (roger.age4)
roger.bark()
roger.walk()


#lambda functions
lambda num : num * 2
multiply = lambda a,b : a * b #this is like a mini function where multiply acts as the name, and it perfroms the function of multiplying any 2 numbers

print (multiply(2,4))  # here,  2 and 4 are multiplied to give 8


# map(), filter(), reduce()

numbers = [1 , 2 , 3]
def double(a):
    return a * 2  #double = lambda a : a * 2  -> this is the use of lambda instead of double function

result = map (double , numbers)  #map() is used to run a function through a list. Here, every value in the list is doubled without needing a looping statement.

print (list(result))  #this gives an output of [2 , 4 , 6]


nos = [2 , 3 , 4]
res = map (lambda a : a * 2 , nos)  # combo of map and lambda 
print (list(res))  # ouptut is [4,6,8]

isEven = lambda a : a % 2 == 0
res2 = filter (isEven , nos)  # filter is used to filter out members of a list based on conditions. Here, values not divisible by 2 are filtered out.
print (list(res2))  # here, the output is [2,4]


expenses = [('dinner' , 80) , ('Car repair' , 120)]
sum = 0
#for expense in expenses:
    #sum+=expense[1]
#print (sum)

sum = reduce (lambda a , b : a[1] + b[1] , expenses)  #reduce() is used to combine muliple values in a tuple, list, dict, set, etc.
print (sum)

def fact(n):
    if n == 1:
        return 1
    return n * fact (n - 1)  #recursion, that is, calling a function within the same function. If there is no proper end to it, it will  1,000 times and then stop.
print (fact (3))


def logtime(func):
    def wrapper():
        print ('before')
        val = func()
        print ('after')
        return val
    return wrapper

@logtime   #decorators allow for the programmer to call the function whenever he wants 
def hello():
    print ('hello')

hello()


def increment(n):
    '''Increment a number'''  #docstring is used for documnetation. Can span multiple lines
    return n + 1

print (help(increment))  #when you use help keyword, in output we get the statement in the triple quotes  


def inc(n : int) -> int:  #this is annotations which allows for program to enforce tha the values in process is of a specific data type. In this case scenario, it is of the int type.
    return n + 1

count : int = 0  #for using annotations in regular statements


try:
    result1 = 2 / 0
    #some lines of code
except ZeroDivisionError:
    print ("Cannot divide by 0")
    # handler <Error1>
#else:
    #no exceptions were raised, code has run successfully
finally:
    #this part will run no matter what, doesn't matter if there is an exception or not
    result1 = 1

print (result1)

try:
    raise Exception("An error!")  # user defined error message
except Exception as error:
    print (error)

 
class DogNotFoundException (Exception):  #creation of own exception by using class
    print ("inside")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print ("Dog not found!")  #error message


numbs = [1 ,2, 3, 4, 5]
numbs_2 = [n ** 2 for n in numbs]  #this is called list compression where for loops sre compressed into a single line that is present in another list
print (numbs_2)   # Thus the output would come as [1, 4, 9, 16 ,25]


class Dog:
    def eat(self):
        print ('Eating dog food')

class Cat:
    def eat(self):
        print ("Eating catnip")

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()  #this is polymorphism, also called method overloading here.


class dog:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def __gt__(self , other):  #  __gt__ is used for comparing the values input into the class
        return True if self.age > other.age else False  
    
roger = dog ('Roger' , 8)
syd = dog ('Syd' , 7)  # this is operator overloading.

print (roger > syd)  #outputsa True as Roger is older than Syd



