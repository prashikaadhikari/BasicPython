#question1
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={**dic1,**dic2,**dic3}
print (dic4)

#question2

my_dictionary = {

"a": 1,

"b": True,

"c": [1, 2, 3, 4],

"d": {"Hello": 5, "World": 5}

}
my_dictionary.update({"xyz":None})
print(my_dictionary)
if 'pqe' in my_dictionary:
    print ("yes")
else:
    print ("no")

print (my_dictionary.values())
del my_dictionary["xyz"]
print (my_dictionary)


#question 3
my_list = list(range(0, 10))
def function (my_list):
            return sum (my_list)
print (function(my_list))

#question 4
another_list = [4, 5, 9, 1, 0, 2, 3]
print (max(another_list))
print (min(another_list))

#question5
l=[1,1,2,3,4,5,6,6,7,8]
y=set(l)
print (y)




    
