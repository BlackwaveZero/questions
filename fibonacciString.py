#write a program that get a number (n) and prints a string like S1,S2,S3,S4,...,Sn
#and Si is either + or -
#Si is positive when i is a fibonacci number otherwise Si is negetive
#Example:
#input : 15
#outpur : +++-+--+----+--

#input : 4
#outpur : +++-


n=int(input())
output='+'
a=1
b=1
while True:
    if b+a>=n:
        output+='-'*(n-b)
        break
    #produce fibonacci
    tmp=b
    b+=a
    a=tmp
    ############
    output+='-'*(b-a-1)
    output+='+'
print (output)




