# Remember a statement is an excecution of code or a calculation
# Statements can be one lined or compound
# Lastly each statement has a header and ----
# Below I will study the basic Data structures in python
# All work is done in the abstract, which I will soon put to pratical use

######Sequence Types #########

# There are three sequence types: Lists, Tuples, and Ranges

# Lists in python are the same as arrays in other languages
# List are one of the intial data structures of python

listVar = ['something1', 'something2', 'something3']
listVar.append('somethingElse')
listVar.pop()
print(listVar)
listVar.reverse()
print (listVar)
print(len(listVar))

# Dictionaries are the same as Hashes in ruby or a Key/Value pair
# Python 3 allows me to store integers as a Keys, python 2 does not

a_dict = { }
thesecond_dict = {
"abc": "a string",
"another": "another string",
"yet another": "yet another string"
}

print(thesecond_dict)

print(thesecond_dict["abc"])

thesecond_dict['abc'] = "Michael's new joy"

print(thesecond_dict['abc'])

print(list(thesecond_dict.keys()))

print("michael" in thesecond_dict)

print("abc" in thesecond_dict)

# Tuples are considered a mix between a dictionary and a list
# Tuples is a data structure that is really good for making choices
# Due to Tuples being immutable they use less memory than list
# Tuples are not used as much as list and dictionaries

tup = ()
tup = ('abc', 'abc')
print (tup)
tup = (
    ('another tup', 'another'),
    ('moreTups','evenMore'),
)
print(tup)

print(tup[0])

# Adds another tuple to an existing Tuple
tup += (('yetanother', 123))

# Adds another item to a tup, but not in its own tuple
tup += ('Another 2', 456)

###### Loops ######
# Below I will remember how to iterate through data in Python

# In order to use a for loop I have to use a list or a dictionary
schools = ['Duke', 'Harvard', 'Columbia']
print(len(schools))

# Below is the for loop
for x in schools:
    print(x)

for x in schools:
    if x == "Harvard":
        print('Veritas')
    else:
        print('Blue Devils or Big C')

# Below is the while loop
# The while loop is the more tradition counter style vs iteration
# Becareful with conditions that all ways have an ending point

i = 0
while i <= 10:
    print(i)
    i += 1

###### Conditionals ######
# Conditionals in python represent boolean values
# I must find a way to create boolean values from data

True
False

obj_a = True
obj_b = False

print(obj_a == True)
obj_b == False
obj_a != obj_b

# Create and inverse with not
print(not obj_a)
print(not obj_a == obj_b)
print (not obj_a is obj_b)

print(len("Michael") == 7)
print(len("Michael") >= 7)
print(len("Michael") != 7)
print(len("Michael") > 7)
print(len("Michael") < 7)

# Below I will run some conditionals into Loops

my_schools = ["Duke Law", "Duke MQM", "Duke MBA"]

for degree in my_schools:
    print (degree)

for degree in my_schools:
    if(degree == "Duke Law" or "Duke MQM"):
        print(str(int(4.0)) + "years")

############ Functions  ############
# Functions are the backbones to an application they help code execute actions
# Below of a review of Lists, Loops, Parsing to Functions

items = ["Mic", "Phone", 323.12, 777.77, "Michael", "Bag", "Lemonade", 575.57]

print (isinstance(123.3, float))
print(isinstance(123.3, int))

# Below I will use the sort function to sort items in a list

str_items = ["MAB", "TRD", "Duke", "Harvard"]

str_items.sort()

print(str_items)

new_school = sorted(str_items)

print (new_school)

new_school = sorted(str_items, key=str.lower, reverse=True)

print (new_school)

# Below is the a list of intergers demonstrating the sort Function

int_list = [123, 777, 575, 555, 888,]

print(int_list)

new_sort = sorted(int_list, reverse = True)

print(new_sort)

new_sort = sorted(int_list, reverse = False)

print(new_sort)

# Below is more methods for extracting and manipulating data from Lists
print(sum(new_sort))

print(len(new_sort))

total = sum(new_sort)

average = total / len(new_sort)

# Below I will utilize python functions in a tradition since by defining
# The code below will loop through the list and parse the data by type into new list

def parse_list(some_list):
    new_items = []
    new_items2 = []
    for i in some_list:
        if isinstance(i, float) or isinstance(i, int):
            new_items.append(i)
        elif isinstance(i, str):
            new_items2.append(i)
        else:
            pass
    return new_items, new_items2

print(parse_list(items))

# formatting strings with variables also known as string intepretation

text = " This is a {var} variable".format(var="new way to")

print (text)

the_name = "Michael"
his_name = "His names is {the_name}".format(the_name = the_name)
print(his_name)

inter = "This is a series of injections {} {}".format("firstone", "secondone")

print(inter)

percent_sub = "hi there %s! Thanks" %("Michael")

print (percent_sub)

# String interpolation with decimal spaces or special formatting
text = "2 decimal places %.2f " %(20)
print(text)

text = "10 decimal places %.10f " %(20)
print(text)

text = "2 decimal places: %.2f" %(200.479839468438)
print(text)

# Below uses the datetime library in order to interpolate with dates and time
import datetime

today = datetime.date.today()
print (today)
print(datetime.datetime.now())

# Using date and time to interpolate and format date output
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)

text = today.strftime('%-m/%-d/%y')
print(text)

#Formating time in UTC
now = datetime.datetime.utcnow()
text = now.strftime('%y-%m-%d %H:%M:%S.%f')[:-4]
print(text)

#Formating for local time
now = datetime.datetime.now()
date_text = now.strftime('%y/%m/%d %H:%M: ')
