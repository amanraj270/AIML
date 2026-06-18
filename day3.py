# Conditonal Statements
# Simple if statement
# if condition:
#    # code to execute if condition is true 


# a=-10
# if a>0:
#     print("a is positive")

# if-else statement
# if condition:
#    # code to execute if condition is true


#else:
#   # code to execute if condition is false


#a=0
#if a>0:
#    print("a is positive")

#else:
#    print("a is not positive")

#match case statement
# match variable:
#     case value1:
#         # code to execute if variable matches value1
#     case value2:
#         # code to execute if variable matches value2
#     case value3:
#         # code to execute if variable matches value3
#    case _:
#         # code to execute if variable does not match any case

a=0
match a:
    case 0:
        print("a is zero")
    case 1:
        print("a is one")
    case 2:
        print("a is two")
    case _:
        print("a is not zero, one, or two")

        #multiple casess
