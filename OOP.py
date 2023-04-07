# def zero_check(any_function):
#     def inner_function(x,y):
#         if x==0 or y==0:
#             return"Sorry Zero is not allowed"
#         else:
#             return any_function(x,y)
#     return inner_function
# @zero_check
# def add(x,y):
#     return (x+y)
# print (add (10,0))



def zero_check(any_function):
    def inner_function(x,y):
        if x==0 or y==0:
            return "Sorry Zero is not allowed"
        elif x==100 or y==1000:
            return "Sorry hundred is not allowed"
        else:
            return any_function(x,y)
    return inner_function

@zero_check
def add(x,y):
    return (x+y)

print(add(10,7))
print(add(0,7))
print(add(100,5))