

### 1. Maximum and Minimum
numbers=[]
for i in range(5):
    num=int(input("Enter a number: "))
    numbers.append(num)
print("Maximum:",max(numbers))
print("Minimum:",min(numbers))


### 2. Palindrome

# python
def is_palindrome(word):
    return word==word[::-1]
word=input("Enter a word: ")
print(is_palindrome(word))

### 3. Count Words, Vowels, Consonants

# python
sentence=input("Enter a sentence: ")
words=len(sentence.split())
vowels=0
consonants=0/4

for ch in sentence.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels+=1
        else:
            consonants+=1
print("Total Words:",words)
print("Total Vowels:",vowels)
print("Total Consonants:",consonants)


### 4. Remove Duplicates

# python
numbers=[10,20,30,20,40,30,50]
unique=[]
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)

### 5. Factorial Using Recursion

# python
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
num=int(input("Enter a number: "))
print("Factorial:",factorial(num))


### 6. Squares Using List Comprehension

# python
numbers=[10,20,30,40,50]
square=[i*i for i in numbers]
print(square)

### 7. Sort Strings by Length

# python
words=["apple","cat","elephant","bat","dog"]
words.sort(key=len)
print(words)


### 8. Second Largest Number

# python
numbers=[12,45,23,78,56]
numbers.sort()
print("Second Largest:",numbers[-2])
### 9. Topper from Dictionary

# python
marks={"Aman":85,"Rahul":92,"Riya":88}
topper=max(marks,key=marks.get)
print("Topper:",topper)
print("Marks:",marks[topper])

### 10. Check Anagram
# python
str1=input("Enter first string: ")
str2=input("Enter second string: ")
if sorted(str1)==sorted(str2):
    print("Anagrams")
else:
    print("Not Anagrams")

### 11. Count Characters Using Dictionary
# python
text=input("Enter a string: ")
count={}
for ch in text:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
print(count)

### 12. Menu-Driven Calculator
# python
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter your choice: "))
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if choice==1:
    print("Result:",add(a,b))
elif choice==2:
    print("Result:",sub(a,b))
elif choice==3:
    print("Result:",mul(a,b))
elif choice==4:
    print("Result:",div(a,b))
else:
    print("Invalid Choice")
