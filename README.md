# GET STACKED !!

## Implementing custom stack using classes in python (Reimplementing basic list data structure)
- But list exists.
- Who cares

## Some workings
1. By default DISPLAY_xx() will display none until it is updated with a valid value which is stored until new value replaces it, and will be available in memory until end of program
2. Last popped, added, etc value can be accesed via self.addition, self.last_pop, etc.


## Cool feature
- Has both loose and strict functions
Example : ADD method wont raise error if it doesnt find 2 elements to add, but SADD is much more strict and raise error at places where you would commonly see errors like adding a single element with nothing.

This gives user freedom to choose between a code where you wont be thrown errors at every other steps, and a code where error would be raised as usual.


## Features to be Added:
1. Seperate class for strict functions
2. More functions to play with numeric values
3. PEEK method
4. EXTEND method
5. Give a string, and it will break it into characters and push to stack
6. Much more


## Usage
```
# Creates empty stack in memory
var = Stack.create_stack()

# To push values in stack
var.PUSH(3)
var.PUSH(4)

# For loosely add
var.ADD()
var.DISPLAY_ADD()

# For strict addition
var.SADD()
var.DISPLAY_SADD()
```
