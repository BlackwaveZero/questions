#two different ways
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
