# list

import copy


l1=['hi', 'hello', 'hey', 'Bye', 'hi', 'hello']
# print(l1[0])
# print(l1[1:5])
# print(l1[2:5])
# print(l1[:5])
# print(l1[:])
# print(l1[-1])
# print(l1[-2:])

# l1.append(10)
# l1 .insert(1, 20)
# l1.extend([30, 40, 50])
# l1.remove(20)
# element=l1.pop(2)
# print(element)
# l1.clear()
# print(l1)
# print(l1.index('Bye'))
# print(l1.count('hi'))

l2=[10, 20, 30, 40, 50]
l2.sort()
l2.sort(reverse=True)
l2.reverse()
print(l2)

# 13=12.copy()
# print(l2)

#WAP to check if two strings are anagrams or not

s1='listen'
s2='silent'

if sorted(s1)==sorted(s2):
    print('Anagrams')
else:
    print('Not Anagrams')

# take a list of strings and short them based on their length

l3=['hi', 'hello', 'hey', 'Bye']
l3.sort(key=len)
print(l3)






