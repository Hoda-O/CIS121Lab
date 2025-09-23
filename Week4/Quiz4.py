#1
'''larger = int(input())
smaller = int(input())
count = 0
while larger/2 >= smaller:
    larger = larger/2
    count += 1
print(count)'''
        
#2
'''x = 'counterattack'
print(x[2:10])'''
'''word = input('Enter a word: ')
for i in range (1, len(word),2):
    print(word[i])'''

#3
'''for number in range (37,1051):
    if number %2 == 0:
        print(number)'''

#4
'''word = ''
user_letter = input('Enter a number or type done to end: ')
while user_letter != 'done':
    word += user_letter
    user_letter = input('Enter a number or type done to end: ')
print(word)'''

#5
'''total = 0
for number in range (50,517):
    if number %2 == 1:
        total += number
print(total)'''

#6
'''number = int(input('Enter an integer: '))
total = 0
while number > 0:
    total += number
    number = int(input('Enter an integer: '))
print(total)'''
 
 #7
'''number = int(input('Enter a number: '))
while number > 1:
    if number % 2 == 0:
        print(number/2)
        number = int(input('Enter a number: '))
    elif number % 2 == 1:
        print(number*3+1)
        number = int(input('Enter a number: '))'''
    
#8
'''num = int(input('Enter a number: '))
for i in range (1, num+1):
    if num % i == 0:
        print(i, end=' ')'''

#9
width = int(input('Enter a width: '))
length = int(input('Enter a length: '))
pattern = input('Enter a pattern: ')

for i in range (length):
    print(pattern*width)