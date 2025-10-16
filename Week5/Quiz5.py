'''def pyramid_volume(base, height):
    return round((base**2*height)/3, 2)

print(pyramid_volume(1,2))
'''
#3 
'''def total_score(two_pointers, three_pointers):
    return((two_pointers*2)+ (three_pointers*3))

print(total_score(5,7))'''


'''def pool_time(grade,time):
    time_output =''
    if grade == 'k':
        grade = 0
    if grade >= 0 and grade <= 3:
        if time == 'Morning':
            time_output = '9am'
        else:
            time_output = '1pm'
    elif grade >= 4 and grade <= 8:
        if time == 'Morning':
            time_output = '10am'
        else:
            time_output = '2pm'
    elif grade >= 9 and grade <= 12:
        if time == 'Morning':
            time_output = '11am'
        else:
            time_output = '3pm'
    return time_output

print(pool_time(5,'Morning'))'''

'''def convert_knuts(knuts):
    output = ''
    galleon = knuts//493
    remaining_knuts = knuts -(galleon * 493)
    sickle = remaining_knuts//29
    remaining_sickles = remaining_knuts -(sickle *29)
    if galleon >= 0:
        output = output + f'Galleon: {galleon}'
    if sickle > 0:
        output = output + f' Sickle: {sickle}'
    if remaining_knuts > 0:
        output = output + f' Knuts: {remaining_knuts}'
    return output

print(convert_knuts(993))'''

# def convert_bronze(bronze):
#     silver = bronze // 20
#     bronze = bronze % 20
#     gold = silver // 15
#     silver = silver % 15
#     result = '' 
#     if gold > 0:
#         result += f'{gold} gold '
#     if silver > 0:
#         result += f'{silver} sliver '
#     if bronze > 0:
#         result += f'{bronze} bronze '
#     return result.strip()

# print(convert_bronze(555))

# from random import randint   

# def toss_coin(guess):
#     value = randint(0, 1)      
#     if guess == value:          
#         return "Correct!"      
#     else:
#         return "Incorrect!"     
# guess = input('Enter guess: ')
# print(toss_coin(guess))



# def fever(temperature):
#     temperature =  int(input([-1]))
#     if temperature[-1] == 'F':
#         if temperature[-1] >= 98.6:
#             return True
#         else:
#             return False
#     elif temperature[-1] == 'C':
#         if temperature[-1] >= 37:
#             return True
#         else:
#             return False 
        

#1
# def reverse_string(word):
#     return word[::-1]
# word = input('Enter a word: ')
# print(reverse_string(word))

#2
# def fever(temp):
#     value, unit = float(temp[:-1]), temp[-1]
#     if unit == 'F':
#         return value > 98.6
#         return True
#     elif unit == 'C':
#         return value > 37
#     return False

# print(fever('36C'))
# 
#3
def boil(temp):
    value, unit = float(temp[:-1]), temp[-1]
    if unit == 'F':
        return value >= 212
        return True
    elif unit == 'C':
        return value >= 100
    return False
#data = input('Enter temperature here: ')
print(boil('99F'))

# #4
def hamming_distance(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count


print(hamming_distance('yoda', 'hoda'))

# #5
# '''def is_isogram(word):
#     for i in range(len(word)):
#         for j in range(i +1, len(word)):
#             if word[i] == word[j]:
#                 return False
#     return True

# word = input('Enter a word: ')
# print(is_isogram(word))

# '''

