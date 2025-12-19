# 1.endswith()

# This checks the ending of the string.
# You give a value, then it starts checking from the ending of the string.If it is found, it prints True; otherwise, it prints False.
str_="I am study from Chattogram College."
print(str_.endswith('ram.'))
# Because the value you gave is in the middle of the sentence.
print(str_.endswith('College.'))
# it is True.Because the value you gave is at the end of the sentence.
str_1='I am ok'
print("speceil value",str_1.endswith('am',0,4)) 
# True  

# 2.capitalize()

# This funcation makes the first letter of a string capital.
str1="happy coding"
print(str1.capitalize())
# Happy coding

# 3.replace()

# This function replaces the old value to new value.
str2='I am happy now'
print(str2.replace('happy','sad'))
# I am sad now
print(str2.replace('n','h'))
# I am happy how

# find()

# This function find the position index number of a string with a given value.
# And this is only the given first value number,it means if you give a value 
# and this value is more in this variable ,but it gives you the first value position index number.
# The method should be used only if you need to know the position of value.
# And if the don’t find the value you gave, it’s return -1.

va="It was a nice job for me.This is for me"
print(va.find('a'))
# 4
print(va.find('for'))
# 18
# here 2 for words in the sentence , and it gives  first for word index number.
print (va.find('g'))
# -1
#  here are no g letter .that's why it's gives -1.


# count()

# This function count how many values are  in the string with a given value. We can give letter,word.
va1="This was a wonderful sentence in this paragraph."
print(va1.count('was'))
# 1
print(va1.count('a'))
# 5
print(va1.count("a",6,10))
# 2  . It means,this count of number start 6 and end 10, In this range how many the value was.
print(va1.count("e",15))
# 4.It means,this count of number start 15.
