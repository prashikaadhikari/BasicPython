#question1
a=str(input("enter the first name:"))
b=str(input("enter the last name:"))
c=a+b
print(c)
print (c.upper())

#question 2
x="&"
print (ord("&"))

#question 3
print (chr(56))
print (chr(565))
print (chr(5656))

#question 4
a="python programming language is awesome"
b= (a[0:6])
print (b)
c=(a[19:27])
print (c)
d=b+c
print (d)

#question5
a="hello"
print (a. capitalize())
print(a.upper())
print (a.lower())

a="NEPAL"
p=a.endswith("o")
print(p)

a="Nepal"
p=a.startswith("N")
print(p)

name="prashika"
age="16"
x="My name is {} and age is {}".format (name,age)
print(x)




b=("syam".replace ("s","t"))
print (b)




b=("xyz".index("z"))
print (b)

a="hello"
print (a.isnumeric())
print (a.isalnum())


#question 6
name="prashika"
age=16
sentence=f'my name is {name} and age is {age}'
print (sentence)


x="My name is {0} and age is {1}".format ("harish",16)
print (x)
