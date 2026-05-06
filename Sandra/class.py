#items =  [ "Bro", "0.2", "45", "True" ]
 
#for item in items: 
#    print(item, sep="/n") 


#n = 4
#while n > 0:
#    print("meow")
""""
def greet():
    print('hello, how are you doing')

greet()

#def greet(name, age, place):
#    print('hello',name)
#    print("you are", age)
#    print("you are from", place)

#greet("Sandra", 21, "Agona")

def add(num):
    print(num)

add(1 + 2)    
"""
#def add(a,b):
#    return a+b
#results=add(3,5)
#print (results)

#def is_even(user_input):
    
#    if user_input % 2 ==0:
#        return True
#    else:
#        return False 
    
#user_input = int(input("Enter a number: "))

#print(is_even(user_input))
""""    
def find_max(user_input):
    if user_input >= 5:
        print(user_input)
    else:
        print(5)

user_input = int(input("Enter num: "))

find_max(user_input)



  


      


 
#def character_check(actions):
#    if actions=='good':
#        print('I am a good person')
#    else:
#        print("i am not a good person")
        
#character_check('good')
"""
#def find_max(a,b):
#    if a>b:
#        return a
#    else:
#        return b
#print(find_max(8,2))

#def count_letters(text):
 #   return len(text)
#print(count_letters('sandra'))

#def count_letters(text):
#    count = 0
#    for _ in text:
#        count += 1
#    return count

#print(count_letters("owusu"))


#def celsius_to_fahrenheit(user_input):
#    print((user_input * 9/5) + 32)
#user_input = int(input("Enter your temperature in (celsius): "))

#result=celsius_to_fahrenheit(user_input)
#print(result)

#def sum_list(a,b,c,d,e) :
#    return (a + b + c + d + e)

#print(sum_list(1,2,3,4,5))

#def count_vowels(name) :
#    count=0
#    for i in name:
#        if i in 'aeiou':
#            count +=1
#    return count
#print(count_vowels('owusu'))    

#def reverse_text(name) :
 #   return name[::-1]
#print(reverse_text('hello'))

#def reverse_text(text):
#    reversed_text=''
#    for i in text:
#        reversed_text=i+reversed_text
#    return reversed_text
#print(reverse_text('prospect'))

#def change(a):
#    change=''
#    for i in a:
#        change = change.replace('r', 'R')
#    return change
#print(change('racecar')) 

#count_down = 11
#for count_down in range(count_down, 1, -2):
#    print(count_down)

#def reverse(name):
#    reverse =""
#    for i in name:
#        reverse = i + reverse
#    return reverse

#print(reverse("Sandy"))

#def factorial(number):
#    results =1
#    for i in range(1,number+1):
#        results *=i
#    return results    

#print(factorial(8))

#def is_palinddrome(text):
#    neat=text.replace("","").lower()
#    return neat==neat[::-1]
#print(is_palinddrome("noon"))
                                            #DICTIONARY

#list = [{'Name' : 'Ick', 'Age' : 20},
#        {'Name': 'Alice', 'Age': 18},
#        {'Name' : 'Alex', 'Age' :19}]

#print(list)
#print(list[-1]['Name'])




                                        #COMPARING DICT

#dict1 = { 'abc': 456 }
#dict2 = { 'abc': 123, 98.6: 37 }
#print(dict==dict2)

#print(dict2[98.6])
#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#print (dict['Name'])
#print(dict['Age'])
#print(dict["Class"])

#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#dict['Age'] = 8
#dict['School'] = "DPS School"
#print(dict['School'])

#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#dict['Age'] = 8
#del dict[]
#print(dict['Age'])

#text = 'abc'
#new_text = text.replace('b', '1') 
#print(new_text)

#Indexing
#3a = "abc"
#print(a[0])
#print(a[1])
#print(a[2])

#slicing
#print(a[0:1])
#print(a[0:2])
#print(a[0:3])

#print()

#Make a list
#a = [2,7,11,13]


#a = [1,2,3,4,5]
#b = a
#b[3] = 20
#b = list(a)
#print(b)
#print(a)

#a = [1,2,[2,6],[5,6],5]
#print[a[3][0]]
#S='SLICECOFSPAM'
#print(S[len(S)-2])

#t=[1,2,3,5,6,7,8]
#for i in range(2,len(t)):
 #   print(t[i])

#s=('hellobro')
#print(s[5:2:-1])

#class Employee:
#    def __init__(self, first, last, pay):
#        self.first = first
#        self.last = last
#        self.pay = pay
#        self.email = first + '.' + last + '@company.com'


#    def fullname(self):
#        return '{} {} {}' .format(self.first, self.last, self.pay )
            



#worker_1 = Employee('Phili', 'Tebri', 50000)
#worker_2 = Employee('Andie', 'Owusu', 40000)

#print(worker_1)
#print(worker_2)

#print(worker_1.first)
#print(worker_2.last)




#worker_1.fullname() 
##print(Employee.fullname(worker_1))

#class solution:
#    def twosum(self,nums:list[int],target:int)->list[int]:
#        n = len(nums)
#        for i in range(n):
#            j = i + 1
#            while j<n:
#                if nums[i]+nums[j]==target:
#                    return [i,j]
#                j+=1
#nums=[1,2,3,4,5]
#target=9
#Solution=solution()
#print(Solution.twosum(nums,target))

                            #TWO SUMS

""" def twoSum(nums, target):
    seen = {}  # number -> index

    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in seen:
            return [seen[needed], i]

        seen[nums[i]] = i

nums = [2,4,5,6,7,8]
target = 11
print(twoSum(nums,target))
"""
                                #ADD TWO NUMBERS
""""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        total = v1 + v2 + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next


# 🔹 Helper function to print the linked list
def printLinkedList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

l1 = ListNode(2, ListNode(4, ListNode(3)))


l2 = ListNode(5, ListNode(6, ListNode(4)))

result = addTwoNumbers(l1, l2)

print("Output:")
printLinkedList(result)
"""
                        #string

"""def lengthOfLongestSubstring(s):

    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
print(lengthOfLongestSubstring("abcdabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))     # 1
print(lengthOfLongestSubstring("pwwkew"))    # 3
"""

            #MEDIAN
"""
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i

        maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
        minRight1 = float('inf') if i == m else nums1[i]

        maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
        minRight2 = float('inf') if j == n else nums2[j]

        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            right = i - 1
        else:
            left = i + 1
nums1 = [1, 3]
nums2 = [2]

print(findMedianSortedArrays(nums1, nums2))
"""
            #PALINDROME
"""
def longestPalindrome(s):
    if not s:
        return ""

    start = 0
    max_len = 1

    def expand(left, right):
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)       # odd length
        expand(i, i + 1)   # even length

    return s[start:start + max_len]
print(longestPalindrome("babad"))
"""
#def num(user_input):
    

#    if user_input == 5:
#        print("yes")

    
#user_input=int(input("Enter a number"))
#num(user_input)
#from datetime import datetime,timedelta
#def get_date_from_day(day_name):
#    day_name=day_name.strip().capitalize()
#    days={
#        "Monday":0,
#        "Tuesday":1,
#        "Wednesday":2,
#       "Thursday":3,
#       "Friday":4,
#        "Saturday":5,
#        "Sunday":6
#    }
#    if day_name not in days:
#        print('invalid day name')
#        return
#    today=datetime.today()
#    today_weekday=today.weekday()
#    target_weekday=days[day_name]
#    difference=target_weekday-today_weekday
#    target_date=today+timedelta(days=difference)
#    print(f"{day_name} is on {target_date.strftime('%d-%m-%y')}")
#user_day=input("Enter day of the week:")
#"get_date_from_day   (user_day)


    

