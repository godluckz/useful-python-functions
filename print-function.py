print("============>Concatination<=======================")
age = 18
name = "Jimmy"

print("--1--")

print("My name is",name,"and i am",age,"years old")
print("-------------------")

#change separator, default above is \n
print("--2--")
print("My name is",name,"and i am",age,"years old", sep=" | ")
print("-------******---------")
print("-------******---------")


print("============>End of line change<=======================")
print("--3--")
print("Hello There")
print("Jimmy Jones")

#Change end of line so doesnt go to next line.
print("-------------------")
print("--4--")
print("Hello There", end=" - ")
print("Jimmy Jones")