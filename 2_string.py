name = "Harry!!!"
print(len(name))
print(name.index("r"))
print(name[0:])
print(name[0:3])
print(name[-4:-1])
print("lets use a for loop:")
for character in name:
    print(character)

print(name.upper())
print(name.lower())
print(name.upper())
print(name.rstrip("!"))
print(name.replace("Harry","john"))
print(name.split())



blogheading = "introduction to js"
print(blogheading.capitalize())
print(blogheading.center(50))
print(len(blogheading))
print(len(blogheading.center(50)))

a = "harry" "!!!" "harry"
print(a.count("harry"))


s= "welcome to the console !!!"
print(s.endswith("!"))
print(s.find("to"))
print(s.isalnum())
print(s.isalpha())
print(s.islower())
print(s.isprintable())
print(s.swapcase())




s = "python" 
print(s.index("t"))
print(s[0])
print(s[3])
print(s[-1])
print(s[-3])
print(s[len(s)-1])
print(s[0:3])
print(s[2:5])
print(s[:4])
print(s[3:])
print(s[:-2])
print(s[::-1])
print(s[::2])
print(s[1::2])
print("hello"[-2])

# strings
name = "harry"
print(len(name))

# indexing / slicing 
print(name[0])
print(name[0:4])
print(name[0:-1])
print(name[0:-3])
print(name[-1:5])
print(name[-4:4])

# looping in strings 
for ch in name :
    print(ch)


# uppercase
print(name.upper())
# lowercase 
print(name.lower())

# rstrip
a = "!siddhi!!!!!!"

print(a.strip('!'))


multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)


first_name = "siddhi"
last_name = "patil"
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name)>len(last_name))
print(len(full_name))

# Escape Sequences in Strings

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote


# old formatting 
# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision

name = "siddhi"
age = 21
print("My name is %s and age is %d" %(name,age))

# str.formatting 
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# f-string 

a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

challenge = 'thirty days of python'
print(challenge.capitalize()) 
print(challenge.count('y'))
print(challenge.count('y',7,16))
print(challenge.endswith('on'))
# find tell about position of the letter 
print(challenge.find('y'))   
print(challenge.find('th'))
print(challenge.find('c')) 
# rfind returns last occurance of a substring 
print(challenge.rfind('y'))


sub_string = 'da'
print(challenge.index(sub_string))
# print(challenge.index(sub_string, 9)) give error 
print(challenge.rindex('on', 8))
# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) 

challenge = 'thirty days of python'
print(challenge.isalnum())

challenge = 'thirtydaysofpython2019'
print(challenge.isalnum()) 

challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge[::-1])
print(challenge.isalpha()) # True

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

num = "100"
print(num.isnumeric())

nums ="10.54"
print(nums.isnumeric())

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True


challenge = 'thirty days of python'
print(challenge.isdecimal())


challenge = '30 days of python'
print(challenge.isidentifier())
challenge = 'thirty days of python'
print(challenge.isidentifier())


skills = ['python','html','css','ml']
result = ' '.join(skills)
print(result)

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))


challenge = 'thirty days of python'
print(challenge.split()) 
challenge = 'thirty, days, of, python'
print(challenge.split(', '))


challenge = 'thirty days of python'
print(challenge.swapcase())   
challenge = 'Thirty Days Of Python'
print(challenge.swapcase()) 

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) 

challenge = '30 days of python'
print(challenge.startswith('thirty')) 



# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first = 'Thirty'
second = 'Days'
third = 'Of'
fourth = 'Python'
space = ' '
string = first + space + second + space +  third + space + fourth
print(string)

word = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(word))

print('Thirty', 'Days', 'Of', 'Python')




# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
print(company[0:7])

print(company.split()[0])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))
# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
text = "Python for Everyone"
print(text.replace("Everyone", "All"))
# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
words = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(words.split())
# What is the character at index 0 in the string Coding For All.
first_character = company[0]
print(first_character)
# What is the last index of the string Coding For All.
print(len(company)-1)
# What character is at index 10 in "Coding For All" string.
character = company[10]
print(character)
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
word = 'Python For Everyone'
text = word.split()


acronym = text[0][0] + text[1][0] + text[2][0]
print(acronym)
# Create an acronym or an abbreviation for the name 'Coding For All'.
text =  'Coding For All'
word = text.split()
acronym = word[0][0] +  word[1][0] +  word[2][0]
print(acronym)
# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
text = "Coding For All People"
print(text.rfind('l'))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sen ='You cannot end a sentence with because because because is a conjunction'
print(sen.index('because'))
print(sen.find('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sen.rfind('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start = sen.find('because')
end = sen.rfind('because')+ len('because')
print(sen[start:end])

print(' '.join(sen.split()[6:9]))
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sen.index('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))
# Does 'Coding For All' end with a substring coding?
print(company.endswith('Coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
text = '   Coding For All      '
print(text.strip())

text = "programming"
result = []
for ch in text :
    if ch.lower() in "aieou":
        result.append(ch)
print(result)


text = "PyTHon"
count = 0 
for ch in text :
    if ch.isupper():
        count +=1 
print(count)

upper_case = 0
lower_case = 0
for ch in text :
    if ch.isupper():
        upper_case += 1
    elif ch.islower():
        lower_case += 1 
print("upper:",upper_case)
print("lower:",lower_case)


text = "C0d!ng@123"
result = []
for ch in text :
    if ch.isalpha ():
        result.append(ch)
print(result)

text = "programming"
result = []
for ch in text :
    if ch.lower() not in "aeiou":
        result.append(ch)
print("".join(result))

freq = {} 
for ch in text :
    freq[ch] = freq.get(ch,0)+1
    # if freq[ch]>1:  for first repeating character 
    #     print(ch)
    #     break

# for second repeating character     
seen = set()
# count = 0        
# for ch in text :
#     if freq[ch] > 1 and ch not in seen:
#         count +=1 
#         seen.add(ch)

#         if count ==2 :
#             print(ch)
#             break
# for last repeating character 
last = None
for ch in text :
    if freq[ch]>1 and ch not in seen :
        last = ch
        seen.add(ch)
print(last)

# find non-repeating
result = []
for ch in text:
    if freq[ch] == 1:
        result.append(ch)
print(result)       

# find first non-repeating character  
for ch in text :
    if freq[ch] == 1 :
        print(ch)
        break      

# last non-repeating character 
last = None
for ch in text :
    if freq[ch] ==1:
        last = ch 
print(last)



# Find the FIRST non-repeating character 
# that is ALSO a vowel
text = "programming"
freq = {}
for ch in text :
    freq[ch] = freq.get(ch,0)+ 1 
for ch in text :
    if freq[ch]==1 and ch in "aeiou":
        print(ch)
        break

# LAST repeating consonant
last = None
for ch in text :
    if freq[ch]> 1 and ch not in "aeiou":
        last = ch 
print(last)

# 
# Find the FIRST non-repeating character 
# that is ALSO a vowel
text = "programming"
freq = {}
for ch in text :
    freq[ch] = freq.get(ch,0)+ 1 
for ch in text :
    if freq[ch]==1 and ch in "aeiou":
        print(ch)
        break

# LAST repeating consonant
last = None
for ch in text :
    if freq[ch]> 1 and ch not in "aeiou":
        last = ch 
print(last)

# "unique last repeating"
seen = set()
for ch in text :
    if freq[ch] >1 and ch not in seen:
        last = ch
        seen.add(ch)
print(last)

seen = set()
count = 0 
for ch in text :
    # if freq[ch] == 1 and ch not in seen:
    if freq[ch] == 1 and ch not in "aeiou" and ch not in seen:
        count +=1 
        seen.add(ch)

    if count == 2:
        print(ch)
        break

last = None
for ch in text :
    if freq[ch]==1 and ch in "aeiou":
        last = ch
        seen.add(ch)
print(last)

result = []
seen = set()
for ch in text :
    if freq[ch] > 1 and ch in "aeiou" and ch not in seen :
        result.append(ch)
        seen.add(ch)
print(result)



word = "communication"
freq = {}
for ch in word :
    freq[ch] = freq.get(ch , 0 )+ 1

result = []
seen = set()
for ch in word :
    if freq[ch]> 1 and ch in "aeiou" and ch not in seen:
        result.append(ch)
        seen.add(ch)
print(result)

for ch in word :
    if freq[ch]> 1 and ch in "aeiou":
        print(ch)
        break

count = 0
seen = set()
for ch in word:
    if freq[ch] > 1 and ch in "aeiou" and ch not in seen:
        count += 1
        seen.add(ch)

        if count == 2:
            print(ch)
            break


# without freq find first repeating character :
for ch in word :
    if ch in seen :
        print(ch)
        break
        seen.add(ch)



character = "dhananjay"
count = 0
for ch in character :
    if ch == "m":
        count += 1
print(count) 


freq = {}
for ch in character :
    ch = ch.lower()
    if ch in "aeiou":
        freq[ch] = freq.get(ch,0)+ 1
print(freq)


s = "python"
print(len(set(s)))
if len(s) == len(set(s)):
    print("Unique")
else:
    print("Not unique")


freq = {}
for ch in character :
    freq[ch]= freq.get(ch,0)+ 1

for ch in character :
    if freq[ch] == 1 and ch not in "aeiou":
        print(ch)
        break

count = 0
seen = set()
for ch in character :
    if freq[ch] > 1 and ch not in seen:
        count += 1 
        seen.add(ch)

        if count ==  2 :
            print(ch)
            found = True
            break

if not found:
    print("No second repeating character exist ")

result = []
for ch in character :
    if freq[ch]==1 and ch not in "aeiou" and ch not in seen :
        result.append(ch)
print(result)



freq = {} 
for ch in text :
    freq[ch] = freq.get(ch,0)+1

seen = set()
count = 0
for ch in text :
    if freq[ch] > 1 and ch not in seen :
        

