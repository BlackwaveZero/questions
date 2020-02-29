number=int(input('Enter your number : '))
Digits = 1
Power  = 1
while (number / Power) >=  10 :
    Digits += 1
    Power *= 10
num=number
reverse=0
for i in range(Digits):
    reverse += (num % 10 ) * (10 ** (Digits-i-1))
    num //=10

if reverse==number:
    print (number,'is DoSeJor')
else:
    print (number,'is not DoSeJor')




#################
# Function
#################
# def NumberOfDigits (Number):#this function returns length of the number
#     Digits = 1
#     Power  = 1
#     while (Number / Power) >=  10 :
#         Digits += 1
#         Power *= 10
#     return Digits
# def isDoSeJor(number):#this fuction check either the reverse of the number is equal to itself or not
#     num=number
#     sum=0
#     lenght=NumberOfDigits(number)
#     for i in range(lenght):
#         sum += (num % 10 ) * (10 ** (lenght-i-1))
#         num //=10
#     return sum==number
################
