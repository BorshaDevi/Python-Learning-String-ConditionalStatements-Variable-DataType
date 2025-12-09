# Type Conversion means changing the data type of a value from one type to another.
# In implicit type conversion, Python automatically converts data types during operations. You do not need to specify the type; the Python interpreter handles it.
""" When try to operate 2 type of value"""

a=2.0
b=2
print(a+b)
# 4.0

# this is give error.Because in python str and int,float can not operate  (+,-) in Conversion.
a='2'
b=2
print(a-b)