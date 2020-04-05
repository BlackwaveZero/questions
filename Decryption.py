text=input()
key=int(input())
tmp2=''
for char in text:
    tmp2+= chr(  ord(char)-(key%256) )
print (tmp2)
#################
# Function
#################
# def convertChar(c,offset):
#     return chr(  ord(c)-(offset%256) )
# def Decrypt(text,key):
#     tmp=''
#     for c in text:
#         tmp+=convertChar(c,key)
#     return tmp
# print (convert(tmp2,key))
#################
# Note : why this type of encryptuin is not secure!?
#################

