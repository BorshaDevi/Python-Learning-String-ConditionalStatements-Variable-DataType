# Type of Operators:

"""

Arithmetic Operators = (+ ,- ,* ,/, // ,**)

Relational / Comparison Operators = (== , != , > , < ,>= , <=)

Assignment Operators = ( = , -= , *= , /= , %= , //= , **=)

Logical Operators =(not , and , or)

Membership Operators = (in , not in)

Identity Operators = (is , is not)

Bitwise Operators = ( & ,l , ^)


"""

# # Assignment Operators = ( = , -= , *= , /= , %= , //= , **=)

# num=10
# # num=num + 10 this and this num +=10 ar same

# num +=10
# print(num)
# """20"""
# num -=5
# print(num)
# """5"""
# num *=5
# print(num)

# num /=5
# print(num)

# num **=5
# print(num)

"""Logical Operators"""
# The logical operator not makes the opposite value. If the value is true, using not makes it false.

# Not operator
a=50
b=40
print(not (a>b)) 

a=True
b=True
print(not (a==b))

# And operator

# For the And operator, all values must be true for it to return true. If even one value is false, then it returns false.
val1=True 
val2=False

print ("and operator " , val1 and val2)
# and operator False

print ('and  operator.....', (a==b) and (a>b))
# and operator False.Because a==b this logic is false.That's why it return false
A=50
B=40

print('And operator',(A!=B)and(A>B))
# True  Because  A!=B is true. A!=B means, A is not equal B.

# Or operator
# For the or operator, here if one value true ,it returns true.
or1=65
or2=54
print('or operator', (or1>or2) or (or1==or2) )
# true .Here or1>or2 this argument is true. that's why it returns true.

