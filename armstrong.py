number=int(input('Enter your number : ')) #gets the number and converts it to int
num=number # temporary variable
sum=0 # sum of digits powered by 3
while num>0: #when num is 0 means no more digits have left to check
    sum += (num % 10 ) ** 3  # (num % 10)  ==> is the digit
    num //=10
if sum==number:
    print (number,'is armstrong number')
else:
    print (number,'is not armstrong number')



#################
# Function
#################
# def is_armstrong(number): #this fuction check either the argument is armstrong or not
#     num=number
#     sum=0
#     while num>0:
#         sum += (num % 10 ) ** 3
#         num //=10
#     return sum==number
#################



