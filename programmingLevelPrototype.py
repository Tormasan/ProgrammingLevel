import math
import glob, os


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
"""
countedLine = 0

for filename in glob.glob("*.py"):
    with open(filename) as readFile:
        lineCount=sum(1 for _ in readFile)
        countedLine += lineCount

print(countedLine)
"""
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



countedLine = 1

for filename in glob.glob("*.*"):
    os.listdir()
    print(filename)
    with open(filename) as readFile:
        lineCount=sum(1 for _ in readFile)
        countedLine += lineCount

print('\n')
print(str(countedLine) +' line of code ')

skillLevel=math.log(countedLine)
print('Programming Level :'+str(skillLevel))


flooredSkillLevel=math.floor(skillLevel)
print('Your Rank is : ')

if  flooredSkillLevel == 0:
    print('total noob')
elif flooredSkillLevel == 1:
    print('beginner')
elif flooredSkillLevel == 2:
    print('Tech Guru')
elif flooredSkillLevel == 3:
    print('Apprentice')
elif flooredSkillLevel == 4:
    print('Padawan')
elif flooredSkillLevel == 5:
    print('Code M0nkey')
elif flooredSkillLevel == 6:
    print('Salty Veteran')
elif flooredSkillLevel == 7:
    print('Master')
elif flooredSkillLevel == 8:
    print('Ace Engineer')
elif flooredSkillLevel == 9:
    print('Development Captain')
elif flooredSkillLevel == 10:
    print('Neo')
elif flooredSkillLevel == 11:
    print('PY GOD')
else:
    print('+=')


print("\n")



for all in os.listdir():
    print(all)
    if os.path.isdir(all) == True:
        print(all)


os.path.isfile("bob.txt")

"""
megnezzuk hogy konyvtarba vagyun e ha igen atalitjuk a cwd-t oda es vegignezzuk a file-okat glob.glob-al



"""