#1
'''my_var = int(input('Enter value here: '))
if my_var % 2 = 1:'''

#2 

#3
'''light_color = (input('Enter color here: '))
if light_color == 'green':
    print('go')
elif light_color == 'yellow':
    print('yeild')
elif light_color == 'red':
    print('stop')
else:
    print('invalid color')'''

#4
'''age = int(input('Enter your age: '))
athletics = input('Enter your athleticism goal: ')
if age >= 20 and age <= 39:
    if athletics == 'Above Average':
        print('47-72')
    elif athletics == 'Below Average':
        print('73-93')
elif age >= 40 and age <= 59:
    if athletics == 'Above Average':
        print('46-71')
    elif athletics == 'Below Average':
        print('72-94')
elif age >=60 and age <= 79:
    if athletics == 'Above Average':
        print('45-70')
    elif athletics == 'Below Average':
        print('71-97')
'''
#5
'''a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a <= b and a <= c:
    if b <= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b <= a and b <= c:
    if a <= c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a <= b:
        print(c, a, b)
    else:
        print(c, b, a)'''

#6
'''
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a >= b and a >= c:
    if b >= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b >= a and b >= c:
    if a >= c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a >= b:
        print(c, a, b)
    else:
        print(c, b, a)'''

#7
'''
knuts = int(input())
sickle_galleon = 17 
knuts_sickle = 29 
'''
#8
'''a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a >= b and a >= c:
    print(f'The largest number is {a}')
elif b >= a and b >= c:
    print(f'The largest number is {b}')
else:
    print(f'The largest number is {c}')'''

#9
'''a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a <= b and a <= c:
    print(f'The smallest number is {a}')
elif b <= a and b <= c:
    print(f'The smallest number is {b}')
else:
    print(f'The smallest number is {c}')'''

#10
'''race = input("Enter race: ")
class1 = input("Enter class: ")

health_points = -1 

if race == "Elf":
    if class1 == "Warrior":
        health_points = 150
    elif class1 == "Bard":
        health_points = 75
    elif class1 == "Wizard":
        health_points = 25
elif race == "Ogre":
    if class1 == "Warrior":
        health_points = 200
    elif class1 == "Bard":
        health_points = 100
    elif class1 == "Wizard":
        health_points = 50

print("Health points:", health_points)'''

#11
'''from random import randint
value = randint(0,1) #picks a random integer. Either 0 or 1.
coin = input('Heads or Tails:' )
if value == 0:
    print('Heads')
elif value == 1:
    print('Tails')'''


#12
'''num1 = int(input('Pick a number: '))
num2 = int(input('Pick another number: '))
num3 = int(input('Pick another number: '))

if num1 == num2 == num3:
        print('You entered the same number 3 times')
elif num1 == num2 or num2 == num3 or num1 == num3:
        print('You entered the same number 2 times')
else:
        print('Each number is unique')'''

#13
'''highway = int(input('Pick a highway number: '))
primary = highway % 100
if highway >= 1 and highway <= 999:
    if primary == 0:
        print('Invalid highway number')
    elif highway %2 == 0:
        print(f'Highway {highway} runs east/west')
    elif highway %2 == 1:
        print(f'Highway {highway} runs north/south')
else:
    print('Invalid highway number')'''

#14
'''letter = input('Enter a letter: ')
if letter == 'a':
    print('vowel')
elif letter == 'e':
    print('vowel')
elif letter == 'i':
    print('vowel')
elif letter == 'o':
    print('vowel')
elif letter == 'u':
    print('vowel')
else:
    print('consonant')'''

#15
'''grade = input('Enter your grade or k: ')
time = input('Enter Morning OR Afternoon: ')
if grade == 'k':
    if time == 'Morning':
        print(('The pool is open at 9 am.'))
    elif time == 'Afternoon':
        print(('The pool is open at 1 pm.'))
elif int(grade) >=1 and int(grade) <= 3:
    if time == 'Morning':
        print(('The pool is open at 9 am.'))
    elif time == 'Afternoon':
        print(('The pool is open at 1 pm.'))
elif int(grade) >=4 and int(grade) <= 8:
    if time == 'Morning':
        print(('The pool is open at 10 am.'))
    elif time == 'Afternoon':
        print(('The pool is open at 2 pm.'))
elif int(grade) >=9 and int(grade) <= 12:
    if time == 'Morning':
        print(('The pool is open at 11 am.'))
    elif time == 'Afternoon':
        print(('The pool is open at 3 pm.'))'''

#16
'''flavor = input('Pick a flavor: ')
if flavor == 'vanilla':
    print('Here is your vanilla ice cream!')
elif flavor == 'chocolate':
    print('Here is your chocolate ice cream!')
elif flavor == 'strawberry':
    print('Here is your strawberry ice cream!')
else:
    print(f'Sorry we do not have {flavor} ice cream.')'''

#17
'''player_1 = input('PLayer 1 choice: ')
player_2 = input('Player 2 choice: ')
if player_1 == 'Rock':
    if player_2 == 'Scissors':
        print('Player 1 wins!')
    elif player_2 == 'Paper':
        print('Player 2 wins!')
    elif player_2 == 'Rock':
        print('It is a tie')
if player_1 == 'Paper':
    if player_2 == 'Scissors':
        print('Player 2 wins!')
    elif player_2 == 'Paper':
        print('It is a tie!')
    elif player_2 == 'Rock':
        print('Player 1 wins!')
if player_1 == 'Scissors':
    if player_2 == 'Rock':
        print('Player 2 wins!')
    if player_2 == 'Paper':
        print('Player 1 wins!')
    if player_2 == 'Scissors':
        print('It is a tie!')'''

#18
'''side1 = int(input('Enter side length 1: '))
side2 = int(input('Enter side length 2: '))
side3 = int(input('Enter side length 3: '))

if side1 == side2 == side3:
        print('Equilateral')
elif side1 == side2 or side2 == side3 or side1 == side3:
        print('Isosoceles')
else:
        print('Scalene')'''
    
#19

'''person = input('Enter the person here: ')
if person == 'Darth Vader':
    print('Father')
elif person == 'Leia':
    print('Sister')
elif person == 'Han':
    print('Brother in law')
elif person == 'R2D2':
    print('Droid')
else:
    print('Unknown')'''


