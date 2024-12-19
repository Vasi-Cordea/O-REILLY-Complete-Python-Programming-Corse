#default arguments
def print_something(name = "Someone", age = "Uknknown"):
    print("My name is", name, "and my age is" , age)

print_something("Nick")

print_something(None, 27)

print_something(age=27)

print_something(age=27, name="Nick")