#write a program that gets dimensions of a cuboid in first three lines and in the fourth line it gets the name of the shape which are circle cube cuboid
#and in the next lines it gets dimensions of those and calculates how many number of the second shape can fit in the first one
#EXAMPLE:
#input :  10
#         10
#         10
#         circle
#         5
#output : 8

#input :  10
#         10
#         10
#         cubiod
#         1
#         2
#         3
#output : 150
a1=int(input())
a2=int(input())
a3=int(input())
type=input()
if type=='circle' or type=='cube':
    radius=int(input())
    count=(a1//radius)*(a2//radius)*(a3//radius)
    print (count)
elif type=='cuboid':
    b1=int(input())
    b2=int(input())
    b3=int(input())
    count=(a1//b1)*(a2//b2)*(a3//b3)
    print (count)
else:
    print ('unkown shape')
