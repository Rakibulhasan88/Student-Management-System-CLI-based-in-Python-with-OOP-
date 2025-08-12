 
#user_input = input("What is your name?")
#a="Good Morning, {}. How are you?".format(user_input)
#print(user_input)
#print(a)

#name="Rakibul Hasan"
#age=21 
#=input("Enter university name:")

#text="Good Morning.I am {name}. I am {age} yers old. I am Study at {Student}".format(name=name, age=age, Student=Student)
#text2=f"Good Morning.I am {name}. I am {age} yers old. I am Study at {Student}"

#print(Student)
#print(text2)
"""
a= input("Enter Number:" );
number=int(a);
if(number%2 == 0):
    print("Even Number");
else:
    print("Sob kichu vhul");
"""
"""
# Dictionary
a={'Rakib':12, 'Karim':13, 'Tamim':78, 1:[1,2,3,4], 2:{3,4,5}}

print(type(a))
for i in a:
    print(i)

print("....")
for i in a.values():
    print(i)

print(a.keys(), a.values())

print(".....")
for k,v in a.items():
    print(f"Key Name:{k}, valus {v}")

print(".....")

#making Zip
a=[1,2,3]
b=["Mango","Banana", "Apple"]

print(list(zip(a,b)))
print(dict(zip(a,b)))
"""
"""
#Dictionary Comprehension
nums=list(range(0,11))

result={i: "Even" if i%2 == 0 else "Odd" for i in nums}

print(result)

"""

#mx= max([1,2,3,4])
#print(f"max value:{mx} . {mx*3}")
"""
def First_function():
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    sum=int(a+b)
    print("Sum is:",sum)

First_function()
"""
#print("Hello"=="hello")

#numbers=range(2,20,2)
#print(*numbers)

# Mapping dictionary data type

"""
person={
    'name':'Rakib',
    'Age':20,
    'University':'Daffodil International University'
}
print(person['name'])
"""

# FrozenSet immutable

# def f():
#     return 1
#     return 2


# print(f())
#LAMBDA function
# lamda argument: expression
# lambda x: x*x
square=lambda x: x*x
print(square(5))
add=lambda x,y: x+y
print(add(5,10))
multiply=lambda x,y: x*y
print(multiply(5,10))
# filter function

students=[('Rakib', 21), ('Karim', 22), ('Tamim', 20), ('Rifat', 23)]
sorted_students=sorted(students, key=lambda x: x[1])
print(sorted_students)

#map function
#filter function
#reduce function

nums=[1,2,3,4,5,6,7,8,9,10]
sq_nums=list(map(lambda x: x*x, nums))
print(sq_nums)