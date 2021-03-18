'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except 
for the last two names, which should be separated by an ampersand.
'''

def namelist(names):
    realList = []
    for item in names:
        realList.append(item['name'])


    if len(realList) == 1:
        return realList[0]
    firstPart = ', '.join(realList[:-1])
    lastPart = " & " + realList[-1]
    return firstPart + lastPart


print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))

print(namelist([{'name': 'Bart'}]))