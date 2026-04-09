num = [1,2,3,4,5,6]
for n in num :
    print(n)
print(num)


print(num[0])
print(num[-1])
num[0] = 10
print(num)

new_num = [8,7]
for n in num :
    new_num.append(n)
print(new_num)

n = [1,2,3,4,5]
n.extend([6,7,8])
print(n)

n.append(9)
n.append(10)
print(n)


s = []
s.extend("xyz")
print(s)

odd = []
even = []
number = [1,2,4,5,6,7,8,9,0,10,11,2,4,21,43,33]
# for n in number:
#     if n % 2 == 0 :
#         even.append(n)
# print(even)

# for n in number :
#     if n % 2 !=0:
#         odd.append(n)
# print(odd)



for n in number :
    if n % 2 == 0 :
        even.append(n)
    
    else:
        odd.append(n)
print(even)
print(odd)


nums = [1,2,2,3,4,1,5]
result = list(set(nums))
print(result)

result = []
seen = set()
for n in nums :
    if n not in seen:
        result.append(n)
        seen.add(n)
print(result)

# | Method      | Pros    | Cons            |
# | ----------- | ------- | --------------- |
# | set()       | simple  | order lost      |
# | seen + loop | correct | slightly longer |


numbers = [3, 7, 2, 9, 5]

largest = numbers[0]
for n in numbers:
    if n > largest :
        largest = n
print(largest)

second = first = float('-inf')
for n in numbers :
    if n > first :
        second = first
        first = n 
    elif n > second and n != first:
        second = n 
print(second)

smallest = numbers[0]
for n in numbers :
    if n < smallest :
        smallest = n 
print(smallest)


second = first = float('inf')
for n in numbers :
    if n < first:
        second = first 
        first = n 
    elif n < second and n != first :
        second = n 
print(second)


nums = list(set(numbers))
nums.sort(reverse= True)

if len(nums)>=3:
    print(nums[2])
else:
    print("No third largest ")


third = second = first = float('-inf')
for n in numbers :
    if n > first :
        third = second
        second = first 
        first = n 
    elif n > second and  n != first :
        third = second
        second = n 
    elif n > third and n != second and n != first :
        third = n 

if third == float('-inf'):
    print("No third largest")
else:
    print(third)










































































