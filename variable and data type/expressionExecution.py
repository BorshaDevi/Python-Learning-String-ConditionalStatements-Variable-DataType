# Expression Execution


# 1. String & Numeric values can operate together with * [it's means repeat]
#  * this name is staris
A,B=2,3
txt='@'
print(2*txt*3) 
# //@@@@@@ //6

w=5
tx='a'
print((w*tx)*w)  
# //aaaaaaaaaaaaaaaaaaaaaaaaa //25


# Python-এ string এবং number এর মাঝে * ব্যবহার করলে, string টা number এর গুনফল অনুযায়ী বারবার repeat হয়।

# 2.String & String can operate with + [aytake concatenation o bole]
# it's means String and string atouch with +.
A,B='2',3
txt="@"
print ((A+txt)*B)
# 2@2@2@

# 3. Numeric values can operate with all arithmetic operators
A,B,C=2,3,4
print(A+B*C)
# 14

# 4.Arithmetic expression with integer and float will result in float

A=4
b=5.0
print(A+b)
# 9.0

# 5.Result of division operator with two integers will be float
a=10
b=2
print(a/b)
# 2.5

# 6.Integer division with float and int will give int but displayed as float.
A=4
b=3.0
c=A//b
print(c,A/b)
# A/b 1.3333333333333333
# c   1.0

# In Python Integer division gives int (it’s int value convert float)but it is displayed as a float. And it 
# Like  A//b ans is 1.3333 but  it gives small int .mean 1  , if answer 0.5 it gives 0 .and then it converts float value like 1.0 , 0.0 .

# 7 Remainder is negative when denominator is negative
# n/d  n=numerator , d=denominator 
# +/+ = + , -/- = + , +/- = - , -/+ = +
A,B=5,2 
print ('hello %',A%B) 
# ans: 1
# 2)5(2
  # 4
  # -
  # 1
A,B=-5,-2
print('hello2',A/B)
# ans: 2.5
a,b=5,-2
print('hello3',a%b)
# ans: -1

A,B=-5,2
print ('hello4',A%B)
# ans: 1