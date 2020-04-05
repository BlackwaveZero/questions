text=input()

offset=0
flag=True

for char in text:
    if char==')':
        offset-=1
    elif char=='(':
        offset+=1
    if offset<0:
        flag=False
if flag and offset==0:
    print ('ok!')
else:
    print ('error!')




#################
# Function
#################
# def checkParenthesis(text):
#     offset=0
#     for char in text:
#         if char==')':
#             offset-=1
#         elif char=='(':
#             offset+=1
#         if offset<0:
#             return False
#     if offset==0:
#         return True
#     return False
#################
