# 1.Write a program to input 2 numbers & print their sum.
a=int(input('a :'))
b=int(input("b :"))
print(a+b)

# 2. Write a program to input side of a square and print its area.
area=float(input("area :"))
# square rule is side * side
ans=area*area
print(ans)

# 3. Write a program to input 2 floating point numbers and print their average.
p1=float(input("p1 :"))
p2=float(input('p2 :'))
average=(p1+p2)/2
print(average)

# 4.Write a program to input 2 int numbers , a and b. print True if a is greater than or equal to b. if not print False.
A=int(input('A :'))
B=int(input('B :'))
val=True if A>=B else False
print(val)


vari='Thank you for your answer'
slicing=vari[0:len(vari)]
print(slicing,len(vari))

vari1='Today is a special day for me'
print(vari1[0:5])

vari2='I am use to this type of problem'
print(len(vari2))
print(vari2[(32-7):32])

vari3='This is awesome day'
print(vari3[7:])
# awesome day
print(vari3[:7])
# This is

vari='Today is a amazing day.'
print(vari[0:5])

vari2="I am very happy to share that I am going to Aboard"
print(vari2[:len(vari2)])
print(vari2[0:])

vari3="You know,It's very occoart"
print(vari3[((len(vari3))-7):-1])
print(vari3[-7:-1])


