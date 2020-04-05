text=input()
key=int(input())
tmp=''
for c in text:
    tmp+= chr( (ord(c) + key ) % 256 )
print (tmp)

#################
# Function
#################
# def convertChar(c,offset):
#     return chr( (ord(c) + offset ) % 256 )
# def Encrypt(text,key):
#     tmp=''
#     for c in text:
#         tmp+=convertChar(c,key)
#     return tmp
#################
# Note : why this type of encryptuin is not secure!?
#################

