student = {
    "name": "Rahul",
    "age": 21,
    "course": "bca"
}
print(student)

student["college"] = "xyz"
print(student)
student["age"] = 24
print(student)

# empty dictionary :
d = {}
# using dict()
d = dict(name = "amit",age = 22)
print(d)

# accessing value :
print(student ["name"])
# print(student ["nname"]) it gives keyerror 
print(student.get("name"))
# print(student.get("nname")) when we use get it give none in output not error 

# Removing items :
print(student.pop("college"))

# looping through dict :
for key in student :
    print(key)

for value in student.values():
    print(value)

for k , v in student.items():
    print(k,v)

# dict methods :
# d.keys = for all keys 
# d.value = for all values 
# d.items = for k ,v 
# d.update 

# dict in different data types :
data = {
    "id": 110,
    "marks": [ 90,56,87],
    "details": {"city": "mumbai","pin":400001}
}
print(data)


students ={
    "s1" : {"name": "sid","age":22},
    "s2" : {"name":"dhan","age":26}
}
print(students)

if "s1" in students:
    print("yes")

for key in students:
    if "name" in students[key]:
        print("yes")


for value in students.values():
    if "sid" in students:
        print("yes")


for student in students.values():
    if student["name"].startswith("d"):
        print("found")


squares = {x :x*x for x in range (1,11)}
print(squares)

even = {x : x*x for x in range (1,11) if x % 2 ==0}
print(even)

text = "programming"
freq = {}
for ch in text :
    freq[ch] = freq.get(ch,0)+ 1
print(freq)

from collections import Counter
print(Counter(text))


nums = [1,2,3,4,5,6,7,8]
group = {}
for n in nums :
    key = "even" if n%2==0 else "odd"
    if key not in group:
        group[key] = []
    group[key].append(n)

print(group)


expenses = [
    ("food", 100),
    ("travel", 50),
    ("food", 30),
    ("shopping", 200)
]
total = {}
for cat , amt in expenses:
    total [cat] = total.get(cat,0) + amt
print(total)

words = ["apple","ant","ball","bat","cat"]
groups = {}
for w in words:
    key = w[0] 
    if key not in groups:
        groups[key] = {}
    for ch in w :
        groups[key][ch] = groups[key].get(ch,0) + 1
print(groups)



marks = [35, 42, 67, 80, 55]
groups = {}
for i in marks :
    if i < 40 :
        key = "fail" 
    elif i < 59 :
        key = "pass"
    else :
        key = "first class"
    if key not in groups :
        groups[key] = []
    groups[key].append(i)
print(groups)


marks = [
    ("ram", 80),
    ("sita", 70),
    ("ram", 60),
    ("sita", 90)
]
total = {}
for name,mark in marks:
    total[name] = total.get(name,0) + mark
print(total)


text = "mississippi"
freq = {}
for ch in text :
    freq[ch] = freq.get(ch,0) + 1

max_count = None
max_count = 0
for i in freq :
   if freq[i] > max_count:
    max_count = freq[i]
    max_char = i
print(max_char)