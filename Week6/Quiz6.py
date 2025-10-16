# #1
# def skip_letter(word):
#     result = []
#     for i in range(0, len(word),2):
#         result += word[i]
#     return result

# print(skip_letter('banana sunday'))


# #2
# def skip_letter(word):
#     result = []
#     for i in range(1, len(word),2):
#         result += word[i]
#     return result

# print(skip_letter('banana sunday'))

#3
# def output_even(small_num, large_num):
#     for i in range(small_num, large_num+1):
#         if i % 2 == 0:
#             print(i)
            
#     return 

# output_even(37,1050)

#4
# def output_odd(small_num, large_num):
#     for i in range(small_num, large_num):
#         if i % 2 != 0:
#             print(i)
            
#     return 

# output_odd(37,1050)

#5 
# def hailstone_seq(num):
#     saved_values = [num]
#     while num > 1:
#         if num % 2 == 0:
#             num = num // 2
#         else:
#             num = (num*3) + 1
#         saved_values.append(num)
#     return saved_values
        
# print(hailstone_seq(25))

#6
# def find_factors(num):
#     factors = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             factors.append(i)
#     return factors

# print(find_factors(12))

# #7
# def ascending_order(num1, num2, num3):
#     if num1 <= num2 and num1 <= num3:
#             if num2 <= num3:
#                 print(num1,num2,num3)
#             else:
#                 print(num1,num3,num2)
#     elif num2 <= num1 and num2 <= num3:
#         if num1 <= num3:
#             print(num2, num1, num3)
#         else:
#             print(num2, num3, num1)
#     else:
#         if num3 <= num1 and num3 <= num2:
#             if num1 <= num2:
#                 print(num3, num1, num2)
#             else:
#                 print(num3, num2, num1)
#     return

# ascending_order(2,4,45)
        
#8
# def descending_order(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#             if num2 >= num3:
#                 print(num1,num2,num3)
#             else:
#                 print(num1,num3,num2)
#     elif num2 >= num1 and num2 >= num3:
#         if num1 >= num3:
#             print(num2, num1, num3)
#         else:
#             print(num2, num3, num1)
#     else:
#         if num3 >= num1 and num3 >= num2:
#             if num1 >= num2:
#                 print(num3, num1, num2)
#             else:
#                 print(num3, num2, num1)
#     return

# descending_order(2,4,45)

# #9 
# def count(list_of_cards):
#     points = 0
#     for card in list_of_cards:
#         if str(card) in ['10', 'j', 'k', 'q']:
#             points -= 1
#         elif str(card) in ['2','3','4','5','6']:
#             points += 1
#         else:
#             points += 0
#     return points
#print(count([2,'k']))

# #10
# def war_of_numbers(num):
#     even_sum = 0
#     odd_sum = 0
#     for n in num:
#         if n % 2 == 0:
#             even_sum += n
#         else:
#             odd_sum += n
#     if even_sum > odd_sum:
#         print('Evens')
#     elif even_sum < odd_sum:
#         print('Odds')
#     else:
#         print('Same')
#     return 

# war_of_numbers([12,90,75,1,1])

# #12
# def largest_even(num):
#     largest = 0
#     for n in num:
#         if n % 2 == 0 and n > largest:
#             largest = n
#     if largest == 0: 
#         print(-1)
#     else:
#         print(largest)
#     return

# largest_even([3, 7, 2, 1, 7, 9, 10, 13])

# #13
# def largest_even(num):
#     largest = 0
#     for n in num:
#         if n % 2 == 1 and n > largest:
#             largest = n
#     if largest == 0: 
#         print(-1)
#     else:
#         print(largest)
#     return

# largest_even([2,4,6,8])

#14
# def progress_days(miles):
#     count = 0
#     for i in range(1, len(miles)):
#         if miles[i] > miles[i - 1]:
#             count += 1
#     return count

# print(progress_days([10,11,12,9,10]))

#15
# def progress_days(miles):
#     count = 0
#     for i in range(1, len(miles)):
#         if miles[i] < miles[i - 1]:
#             count += 1
#     return count

# print(progress_days([5,3,2,1]))

#16
# def like_or_dislike(events):
#     status = 'nothing'
#     for event in events:
#         if event == status:
#             status = 'nothing' 
#         else:
#             status = event
#     return status


# print(like_or_dislike(['dislike', 'dislike', 'dislike']))

#17
# def get_indices(lyst, target):
#     indicies =[]
#     for i in range (1,len(lyst)):
#         if lyst[i] == target:
#             indicies.append(i)
#     return indicies
    
# print(get_indices([1,5,5,2,7],5))

# #18
# def list_of_multiples(num,length):
#     multiples = []
#     for i in range(1, length + 1):
#         multiples.append(num*i)
#     return multiples

# print(list_of_multiples(7,5))


#19
def is_acronym(s,words):
    acronym = ''
    for word in words:
        'acronym.append(word[0])'
        acronym += word[0]
   
    if acronym == s:
        print('True')
    else:
        print('False')
    return

print(is_acronym("a", ("an", "apple")))

