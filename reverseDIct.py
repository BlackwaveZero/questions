def reverseDict(dict):
    new={}
    for key, value in dict.items():
        new[value]=key
    return new
def sort(dict):
    keys=list(dict.keys())
    keys.sort()
    newDict={}
    for key in keys:
        newDict[key]=dict[key]
    return newDict
def getUserInput():
    inp=input()
    dict=eval(inp)
    dict=reverseDict(dict)
    dict=sort(dict)
    print(dict)
getUserInput()
