# # If-elif-else(syntax)

# # If(condition):
# #     print(something) [Here 4 spaces.Because in python proper spacing is very important . And this spacing called in python indention. ]
# # elif(codition):
# #     print(something)
# # else:
# #     print(something)


# # *we can write so many if.Like:
# #  If(condition):
# #     print(something)
# # If(condition):
# #     print(something)
# # [There is checking both]

# num=5
# if(num>2):
#     print('great')
# if(num >3):
#     print('also great')   
# # great
# # also great
# if(num>2):
#     print('great')
# elif(num >3):
#     print('also great')
# # great    
# # Here if condition is true that's why it print great and doesn't go next line.

# light='green'
# if(light=='red'):
#     print('stop')
# elif(light=='yellow'):
#     print('Look')
# elif(light=='green'):
#     print('Go')    
# else:
#     print("can't understand")        
# #  Go    

# Nesting condition
# It means if condition is written in the other if condition.

age=95
if(age>=18):
    if(age>=80):
        print('cannot drive')
    else:
        print('can drive')
else:
    print("can't drive")        