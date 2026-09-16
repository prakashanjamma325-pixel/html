frozenset
========

python also has an immutable set called frozensset.
normal set:
A={1,2,3} A.add(4)  #

frozenset:
A=frozenset([1,2,3]) print(A)
you cannot modify it:
a.add(4)
this gives an error.
difference
set -> mutable
frozen ->immutable

python dictionary
================

a dictionary in python is a collection used to store data in 
key-value pairs
word ->meaning
"apple" ->"a frute"

in python:
stundent={
"name":"raju",
"age":20,
"course":"cse"}
here:
"name" ->key
"raju" ->value
"age" ->key
20 ->value

1. creating a dictionary
empity dictionart
d={}
or:
d=dict()



dictionary characteristics

a dictionary:
. stores  key-value pairs
. keys must be unique 
. values can be duplicated

. is mutable
. maintains insertion order in modern python 
.keys commonly string , number
. values can be almost any python object


accessing values
use the key :
stuent={
"name":"ravi",
"age":20
}
print(stundent["name])
print(student["age"])
out put:
ravi 20

important

you accesa dictionary using its key ,not its pos's.
student["name"]
unlike a list:
list[0]



aading a new element
simple




dictionary method

1.get : by using get we can axcess the value so we have pass ke as a paramete

accessing using get()
you can also use:
student.get("name")
example:
student={
"name":"ravi",
"age":20
}
print(student.get("name"))
output:
ravi



difference b/w [] and get()
student["city"]
if "city" doesn't exist->keyerror
but:
student.get("city")
returns:
none
you can provide a defalute value:
print(student . get ("city","not available"))
output:
not available

pop item

removes and return the last inserted  key -values pair .
student ={
"name"="ravi",
"age":20,
"city":"hyd"
}
student.clear()
print(student)
output:
{}
keys=it returns all keys
ex:student.keys

values=it returns all values
ex:student.keys

items=it returns all keysvalu pairs
ex:student.item()






























