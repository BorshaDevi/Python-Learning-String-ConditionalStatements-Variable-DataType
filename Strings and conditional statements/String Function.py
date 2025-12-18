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


