text=input()
output=''
count=0
last=0
for i in range(len(text)):
    if count>0:
        if text[i]=='=':
            count+=1
        else:
            output+=text[last:i-(count*2)]
            last=i
            count=0
    else:
        if text[i]=='=':
            count=1
output+=text[last:len(text)-(count*2)]
print (output)

##########################################
#code khanom postpardaz
##########################################
# bText=input()
# gText=""
# for i in bText:
#     if i=="=":
#         if gText=="":
#             continue
#         gText=gText[:-1]
#     else:
#         gText+=i
#     print ('#',gText,'\n')
# print(gText)
########################################
