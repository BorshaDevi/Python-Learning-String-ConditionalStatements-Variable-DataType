# Conditional Statements:
"""If -elif-else(Syntax)

if(condition):
    Statement1
elif(condition):
    Statement2
Else:
    StatementN
"""
# Must add(:) after condition.
age=2
if(age >=3):
    print('Hello world')
    # Hello world 
elif(age==2):
    print('Hello world 2') 
    # Hello world 2
else:
    print('end')
# here are 4 spaces at the beginning of a line. This is called indentation.


# When need to check two condition then use and keyword
marks=int(input('marks: '))
if(marks>=90):
    print('A')
elif(marks>=80 and marks<90):
    print('B')
elif(marks>=70 and marks<80):
    print('C')
else:
    print('D')  
    
# When we need to check multiple conditions, we use or.
A=int(input("A : "))
G=input("M/F : ")
if(A==3 or A==4 or G=='F'):
    print('fee is 200')   
else:
    print('no fee') 


# Singal Line if/ Ternary Operator

"""<var>=<val1>if<condition>else<val2>"""
food=input('food: ')
# If food is 'cake', eat will be 'yes'; otherwise, it will be 'no
eat='yes'if food=='cake' else 'no'
print(eat)

"""<stt1>if <condition>else<stt2>"""
food=input('food :')
print('sweet') if food=='cake' or food =='jilapi'else print('not sweet')

# Clever 
""" <var> =(false_val , true_val)[condition]"""
age=int(input("age : "))
vote=('No','Yes')[age>=18]
print (vote)

# If your salary 0-50k than tax 10%(0.1) or 50K+ than tax 20%(0.2)
salary=float(input("salary : "))
tax=salary*(0.1 , 0.2) [salary>50000]
print (tax)