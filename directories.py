
def getIndex(directories,dir):
    indexes=dir.split('/')
    counter=0
    length=len(indexes)
    index=directories
    while True:
        if length==counter:
            return (True,index)
        if indexes[counter] not in index:
            return (indexes[counter:length],index)
        index=index[indexes[counter]]
        counter+=1
def getParentIndex(directories,dir):
    if dir=='':
        return True

    indexes=dir.split('/')
    length = len(indexes) - 1

    if length<0:
        return (dir,directories)

    counter=0
    index=directories

    while True:
        if length==counter:
            if indexes[counter] in index:
                return (indexes[counter],index)
            return False

        if indexes[counter] not in index:
            return False

        index=index[indexes[counter]]
        counter+=1
def canRename(directories,dir,newName):
    parent=getParentIndex(directories,dir)
    if parent==False:
        return -1#does not exists
    if newName in parent[1][parent[0]]:
        return -2#new dir exists
    return parent
def rename(directories,dir,newName):
    if dir=='':
        return -1
    index=canRename(directories,dir,newName)
    if(type(index)!=tuple):
        return index
    childs = index[1][index[0]].copy()
    del index[1][index[0]]
    index[1][newName] = childs
    return True
def createDir(directories,dir):
    index=getIndex(directories,dir)
    if index[0]==True:
        return False#exists
    else:
        tmp=index[1]
        for d in index[0]:
            tmp[d]={}
            tmp=tmp[d]
    return True
def removeDir(directories,dir):
    index=getParentIndex(directories,dir)
    if index==False:
        return False
    if index==True:
        directories.clear()
    else:
        del index[1][index[0]]
    return True
def userInput(command):
    global directories
    if command=='create':
        dir=input()
        if createDir(directories,dir):
            return (directories)
        else:
            return('Directory exists')
    elif command=='remove':
        dir=input()
        if removeDir(directories,dir):
            return(directories)
        else:
            return('Directory does not exist')
    else:#rename
        dir = input()
        newName=input()
        status=rename(directories,dir,newName)
        if status==-1:
            return('Directory does not exist')
        elif status==-2:
            return('New directory exists')
        else:
            return(directories)
def getNumberOfCommand():
    return int(input())

directories={}

def run():
    directories
    count=getNumberOfCommand()
    for i in range(count):
        userInput(input())
    return str(directories)
run()
print(directories)




