age=5
if(age != 5):
    print('This is wrong.')
elif(age >=10):
    print('This is corret')
else:
    print('This is right.')    
# This is right.

light=input('light :  ')
if(light=='red'):
    print('Stop')
elif(light=='yellow'):
    print('Look')
elif(light=='green'):
    print('go') 
else:
    print('Light is broken')   




A=int(input("A : "))
G=input("M/F : ")
if((A==1 or A==2) and G=='M'):
    print('fee is 100')
elif(A==3 or A==4 or G=='F'):
    print('fee is 200')    
elif(A==5 and G=='M'):
    print('fee is 300')
else:
    print('no fee')     
# print output for  A=5 & G=M
# A=2 & G=F


# ternary operator 
fruit=input('fruit: ')
water=input('water :')
eat='yes'if(fruit=='mango' and water=='7up') else 'no'
print(eat)

contite=int(input("contite: "))
price=float(input('price : '))
name=input('name : ')
sale='yes'if contite>1 and price>40.0 and name=='fish'else 'no'
print(sale) 

water=input('water :')
print('I drink this') if(water=='7up')else print('no, I do not drink it.')


# Clever condition
price=int(input("price :"))
buy=['No',"Yes"][price<30]
print(buy)

# discount 
buy=float(input('buy :'))
discount=buy*(1.0,0.5) [buy>5000]
print(discount)
