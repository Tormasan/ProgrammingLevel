import math
import glob, os

print('this program provide u information about how big is your breee')

"""
countedLine=0

for filename in glob.glob("*.py"):

    readFile= open(filename,'r')
    readLi=readFile.readlines()
    lineCount= readLi.count("\n")
    countedLine+=lineCount

print(countedLine)
"""
"""
countedLine = 0

for filename in glob.glob("*.py"):
    readFile = open(filename)
    lineCount=sum(1 for _ in readFile)

    #readLi = readFile.readlines()
    #lineCount = readLi.count("\n")

    countedLine += lineCount

print(countedLine)

"""

countedLine = 0

for filename in glob.glob("*.py"):
    with open(filename) as readFile:
        lineCount=sum(1 for _ in readFile)
        countedLine += lineCount

print(countedLine)

"""
with open('asd.py') as f:
    print (sum(1 for _ in f))

"""

"""
readMe= open('MachineLearningTutorial.py','r')
readLi= readMe.readlines()
print(readLi)
rows= readLi.count('\n')

print(rows)
print('Programming Level :'+str(math.log(rows)))
"""


'''
osszeszamolja a sorokat amit eddig programoztam minden sor 1 xp
exponencialis fugveny szerint megy az xp
10. szint  22025 sor
'''