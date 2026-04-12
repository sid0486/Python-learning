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


# list comprehension :

nums = [1,2,3,4,5]
result = []
for n in nums :
    result.append(n*n)
print(result)


result = [n*n for n in nums]
print(result)


even = [n for n in nums if n % 2 == 0 ]
print(even)

odd = [n for n in nums if n %2 != 0]
print(odd)

squares = [n*n for n in nums if n % 2 == 0]
print(squares)

square = [n*n for n in nums if n %2 != 0]
print(square)

name = "python"
chars = [ch for ch in name ]
print(chars)


number = [1,2,3,5,6,8,9,10,43]
sq = [n*n for n in number ]
print(sq)

num = [n for n in number if n > 5 ]
print(num)

word = "programming"
vowel = [ch for ch in word if ch in "aeiou" ]
print(vowel)

nums = [1,2,3,4]
check = ["even" if n % 2 ==0 else "odd" for n in nums]
print(check)

result = ["big" if n > 3 else "small" for n in nums]
print(result)

result = ["even-big" if n %2 == 0 and n >3 else "others" for n in number]
print(result)


nums = [1,2,3,4,5]
total = 0
result = []
for n in nums :
    total += n
    result.append(n)
print(total)
print(sum(nums))

print(nums[ : :-1])

result = []
for i in range(len(nums)-1,-1,-1):
    result.append(nums[i])
print(result)

result = []
for n in nums :
    result.insert(0,n)
print(result)


nums = [1,2,3,4,5]
left = 0
right = len(nums)-1 
while left < right :
    nums[left], nums[right] = nums[right], nums[left]
    left += 1 
    right -= 1

print(nums)



nums = [1,2,2,3,4,1,5]
result = list(set(nums))
print(result)

# 👉 Visited / Seen Pattern
seen = []
for n in nums :
    if n not in seen:
        seen.append(n)
print(seen)

# better version :
seen = set()
result = []
for n in nums:
    if n not in seen:
        seen.add(n)
        result.append(n)
print(result)

# Structure	Speed
# list (in)	slow
# set (in)	fast ⚡

# 🔥 Tracking Top 2 Elements Pattern
def second_largest(number):
    first = second = float('-inf')
    for n in number :
        if n > first :
            second = first
            first = n 
        elif n > second and n != first :
            second = n 
    return second
print(second_largest([1,2,3,5,6,8,9,10,43]))


def leaderboard(scores):
    first = second = third = float('-inf')

    for n in scores:
        if n > first:
            third = second
            second = first
            first = n

        elif n > second and n != first:
            third = second
            second = n

        elif n > third and n != second and n != first:
            third = n

    return {
        "gold": first,
        "silver": second,
        "bronze": third
    }


nums = [50, 80, 70, 90, 85]

result = leaderboard(nums)

print("🥇 Gold:", result["gold"])
print("🥈 Silver:", result["silver"])
print("🥉 Bronze:", result["bronze"])

print(f"🥇 GOLD {result['gold']} | 🥈 SILVER {result['silver']} | 🥉 BRONZE {result['bronze']}")



nums = [2,7,11,15]
target = 9

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
nums = [2,7,11,15]
target = 9

result = two_sum(nums, target)
print(result)


# What if no pair exists?
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

nums = [2,8,11,15]
target = 9
result = two_sum(nums, target)
print(result)   


def two_sums(nums,target):
    seen = {}

    for i , n in enumerate(nums):
        needed = target - n 

        if needed in seen :
            return [seen[needed],i]

        seen [n] = i
        
nums = [2,7,11,15]
target = 9
result = two_sums(nums, target)
print(result)   

















