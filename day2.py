# operators 
# Arithmetic operators
a = 10
b = 3
print("Addition:", a + b)        # Addition
print("Subtraction:", a - b)     # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)        # Division
print("Floor Division:", a // b)  # Floor Division
print("Modulus:", a % b)         # Modulus

#Assignment operators
a=10
b=20
a+=20 # a = a + 5
print("a after a+=5:", a)  # a = a + 5

a=10
b=20
a+=20 # a = a + 20  
# a+=20 # a = a + 20
# a+=b
# print("a=",a)

# Logical operators
x = True
y = False
print("x and y:", x and y)  # Logical AND
print("x or y:", x or y)   # Logical OR
print("not x:", not x)     # Logical NOT

#Comparison operators
a = 10
b = 20
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a < b:", a < b)    # Less than
print("a > b:", a > b)    # Greater than
print("a <= b:", a <= b)  # Less than or equal to
print("a >= b:", a >= b)  # Greater than or equal topyton

# Membership operators
my_list = [1, 2, 3, 4, 5]
print("1 in my_list:", 1 in my_list)      # Check if 1 is in the list
print("6 not in my_list:", 6 not in my_list)  # Check if 6 is not in the list
print("Hello" in "Hello World")  # Check if "Hello" is in the string
print("world" not in "Hello World")  # Check if "world" is not in the string
print("python in 1st line of code:", "python" in "1st line of code")  # Check if "python" is in the string

# Identity operators
a=10
b=20
c=a
print(a is b)  # Check if a and b refer to the same object
print(a is c)  # Check if a and c refer to the same object
print(a is not b)  # Check if a and b do not refer to the same object
print(a is not c)  # Check if a and c do not refer to the same object
print("a is b:", a is b)  # Check if a and b refer to the same object
print("a is not b:", a is not b)  # Check if a and b do not refer to the same object
