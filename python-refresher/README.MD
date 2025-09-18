##### Agenda
- Foundations of python
- Tool Installations
- Getting System Ready


###### Python
- support various libraries

###### Variables & Constant

- Constant refer to fixed value that remain same eg print("hello") where hello is value or constant

- Varaible are where we assign a name to the values in the computer memory location 
eg x = 100

###### Rules of variable name
- variable name cannot be a keyword
- should start with letter or _
- it can be alphanumeric
- names are case sensitive

###### Data Types in Python

- numeric
- sequence
- boolean

numeric
- int --> whole number
- float --> decimal value
- complex

Sequence
- ordered collection of simiar or different data types
- list - orderded collection of different data types 
- tuple - ordered collection of different data types but immutable
- string

type casting as a way to convert 1 data type to another data type using pre defined functions

###### Operators in python

- Arithmetic operators    +, -, * , /, %, ** . //
- Logical Operators       and, not- to inevert value
-- Comparison operators   >, <, <=, !=, ==

###### Object Oriented Programming

- programming paradigm that uses objects and classes for organizing the code
- key principles : encapsulation, inhertance, polymorphism and abstraction
- benefits are
- modularity of code : oirganize to reuse
- encapsulation: hide the implementation details and expose only the necessary information
- abstraction: focus on what object does rather than how it does
- inheritance: create new classes based on existing one
- polymorphism: use objects of different types in an interchangeable manner

- class: a blueprint for creating object, inside calss we have attibutes or variables and methods.
- object: it is an instance of class

- Class syntax:

``` python 
class Student:
    def __init__(self, name, age): # this is method
        self.name = name # attribute
        self.age = age # attribute

    def info(self): # this is a method
      return "school student"
     
```

- Instatiate the class

``` python 

s1 = Student("sam", 35)

print(s1.name)
print(s1.age)
```

- 2 attributes: Class atrribute, instance attribute

``` python 
class Car:
    model = "honda" # class attribute
    
    def __init__(self, engine, turbo):
        self.engine = engine  # instance attribute
        self. turbo = turbo # instance attribute
     ```

- methods are functions within the class

