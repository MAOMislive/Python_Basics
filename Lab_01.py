# -*- coding: utf-8 -*-
"""Lab_01.ipynb

# **Basics of Python**
"""

print('Hello World Hi')

print('DBMS Champion 101')

student_ID = 11212115
student_name = '''Nayem'''
student_cgpa = 3.5
is_eligible = True

print(student_ID)
print(student_name)
print(student_cgpa)
print(is_eligible)

print(type(student_ID))
print(type(student_name))

x = 3
y = 3.5
z = 3 + 2j 

print(type(z))
print(z)
print(type(z.real))
print(z.real)
print(type(z))
print(z.imag)

# Taking Input 
a = input('Enter a number: ')
print('You have entered: '+a)

a = int(input('Enter a number: '))
a=a+10
print(a)

message = "Python Programming"
print(len(message))
print(message[1])
print(message[-2]) 
print(message[0:3])
print(message[2:5])
print(message.lower())
print(message.upper())
print(message[:5])
print(message[5:])

print(message.find("pro"))
print(message.find("Pro"))
print(message.replace("P", "J"))

"""# **Operators**
* Arithmetic operator
* Logical
* Relational
* Shorthand
"""

# Arithmetric Operators

x = 11;
y = 5;

print(x+y)
print(x-y)
print(x*y)
print(x/y)

#Relational Operators ---  <, >, <=, >=, ==, !=

print(2 < 5)
print(2 == 5)

#Logical Operators

print(2 < 5 and 2 == 5)
print(2 < 5 and not 2 == 5)

#Shorthand Assignment Operator --- ++, -+, *+, ...

"""# **3 number reverse**"""

num = int(input("Enter the number:"))

a = int(num%10)
num = num/10

b = int(num%10)
num = num/10

c = int(num%10)

print(str(a) + str(b) + str(c))

"""# **Conditional Statement**"""

gender = 'm'
types = "male"

if gender == 'F' or gender == 'f':
  print("Welcome to our beauty parlor!")
elif gender == 'm' and types == 'male' :
  print("Okay")
else:
  print("Sorry!, you are not allowed!!!")

student = "Rahad Khan"
if 'A' in student:
  print("Found")
else:
  print("Not Found")

"""# **Loop - FOR**"""

for i in range(5) :  #range(start, end, stepover)
  print(f'i:{i}')

for i in range(2, 5) :  #range(start, end, stepover)
  print(f'j:{i}')

for i in range(0, 10, 2) :  #range(start, end, stepover)
  print(f'k:{i}')

"""# **Patten design with single loop**"""

print("*"*10)

for i in range(1, 6, 1) :  #range(start, end, stepover)
  print("* "*i)

for i in range(1, 6, 1) :  #range(start, end, stepover)
  print(" "*(6-i) + "* "*i)

