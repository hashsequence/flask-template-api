# Python Notes

These notes should refresh you on the syntax and OOP for python 3.9

## Variables

to declare and instantiate a variable in python

```python
name = "Rolf"

print(name)
#Rolf
print(name*name)
# RolfRolf
print(name+name)
# RolfRolf
```

## string formatting

```python
name = "Bob"
greeting = f"Hello, {name}"
print(greeting)
# Hello, Bob
name = "Rolf"
print(greeting)
# notice that its not a reference so it keeps it as Bob
# Hello, Bob
```
formtat()

```python
name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_Rolf = greeting.format("Rolf")

print(with_name)
# Hellp, Bob
print(with_Rolf)
# Hello, Rolf

longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("Rolf","Monday")
print(formatted)
# Hello, Rolf. Today is Monday

```

## User Input

* get user input

```python
name = input("Enter Name")
# waits for user input then prints below
print(name)

num = input("enter number")
print(int(num)) # type cast to int

num = num / 3.4
print(f"num divided by 3.4: {num:.2f}) # formats the float

```

## list, tuples, and sets

```python
l = ["Rob", "Rolf", "Anne"] # is a list
t = ("Rob", "Rolf", "Anne") # tuple: use regular parens, cannot add or remove elements from a tuple
s = {"Rob", "Rolf", "Anne"} # order is not gauranteed 

print(l[0]) #prints first element of l
# cannot use subscript notation like s[0]
# t[0] = "smith" -> this will cause runtime error

l.append("thunder") # appends element to the list
# tuple has no append
l.remove("thunder") # removes element from list
s.add("smith") #order is not same still
s.add("smith") # set has no dupes


```

### Set Operations

```python
friends = {"Rob", "Rolf", "Anne"}
abroad = {"Bob", "Lisa"}

local_friends = friends.difference(abroad) #takes the difference between two sets

friends = friends.union(abroad) # union of two sets

friends = friends.intersection(abroad) #intersection of two sets


```