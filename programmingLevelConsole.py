import math
import glob, os

print('this program provide you information about how big is your breeeeee')
print('Put this .py file in your directory where all your code is (trust me kevin)')
print('now run it BIATCH!!!')
print('\n')

print('tell me what kind of extension you want maybe *.py *.c ')
extension=str(input(":"))
print("\n")

print('the program find the following items: ')

countedLine = 1

for filename in glob.glob(extension, recursive=False):
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

