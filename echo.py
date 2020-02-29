#there is a broken speaker which plays every word n times and in every turn it removes one of the letters and replaces it with the next letter
#water
#aater
#ttter
#eeeer
#rrrrr
#write a prgram that prints the words said by speaker
#first dont use string slicing
#after that write a program with string slicing

word=input()

print ('without slicing : ')
for i in range(len(word)):
    for j in range (i):
        print (word[i],end='')
    for j in range(i,len(word)):
        print (word[j],end='')
    print ()

print ('with slicing : ')
for i in range(len(word)):
    for j in range (i):
        print (word[i],end='')
    print (word[i:len(word)])
