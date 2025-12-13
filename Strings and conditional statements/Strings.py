# String is a data type that stores a sequence of characters.
name='Hello world',
name2="Hello world",
name3="""Hello world"""
# we can write 3types of quotesion formate string.
"say hello. I'm x"
# see here I write 2 quotesion and under single quotesion.

"""Hey, "How  are you?" I'm fine."""
# see here I write 3 quotesion and under single quotesion and double quotesion.
'every thing is ok. "for that  I am happy."'
# see here I write single quotesion and under 2 quotesion.





# Escaped sequence character: 

# \n=Generated newline
# \t=tab
# \r=it's removed from this before line.
text="We are happy.\nyou don't think about this."
print(text)
text1="Today is chocolate day.\tyou must give the chocolate everyone."
print(text1)
text2="Don't worry for me.\\I am ok."
print(text2)
text3="This is our Tini day.\rso,let's go for dinner."
print(text3)





# length:

# if we need to know any string length ,we can use the len function.
# Length  count , not only character but also " ",%,$ etc.
text4='Borsha'
text5='Devi'
final_str_len=text4+" "+text5
print(final_str_len,len(final_str_len))
# Borsha Devi,11
name='Borsha Devi'
print(len(name))
# ans:11
#  if we carefully see that there are 10 words.but print 11.why?Because when string length counts, there are count spaces also.


# Indexing:

# Indexing means,in string all characters have position number.
# Index numbers start with 0 number. If any space or any special character ,there is also an index number.
# Write this val[0,1 ….etc ] 
text='Thank'
print(text[4])
text2='Thank you'
print(text2[5])
# Note: we don’t change character help with index numbers. 
text1='value'
text1[4]='@'
print(text1)
# they give you this : 'str' object does not support item assignment.