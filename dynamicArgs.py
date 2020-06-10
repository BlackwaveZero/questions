def func(*args):
    arguments=list(args)
    arguments.sort()
    out=[]
    for arg in arguments:
        print(arg)
def getArgs():
    count=int(input())
    args=[]
    for i in range(count):
        args.append(input())
    func(*args)
getArgs()
