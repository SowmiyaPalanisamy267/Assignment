# 1.odd or even
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = []   #a new list that starts out empty.
odd_numbers = []    #a new list that starts out empty.

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)    #add the even numbers to even_numbers
    else:
        odd_numbers.append(num)     #add the odd numbers to odd_numbers

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# 2.finding prime numbers from list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
for num in numbers:
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

#3.find the count of happy number from the list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
count = 0
for n in numbers:
    num = n
    seen = []
    while num != 1 and num not in seen:
        seen.append(num)
        sum_of_squares = 0
        while num > 0:
            last_digit = num % 10
            sum_of_squares = sum_of_squares + (last_digit ** 2)
            num = num // 10
        num = sum_of_squares
    if num == 1:
        count = count + 1
print("Number of happy numbers in the list:", count)

#4. sum of first integer and last integer
n = int(input("Enter a number: "))
last_digit = n % 10
first_digit = n
while first_digit >= 10:
    first_digit //= 10
print("Sum =", first_digit + last_digit)

#5.logic to find all the ways to make rs10 using rs 1, rs 2, rs 5 and rs 10 coins
for one_rs_coin in range(11):        # Rs1 coins (0 to 10)
    for two_rs_coin in range(6):     # Rs2 coins (0 to 5)
        for five_rs_coin in range(3): # Rs5 coins (0 to 2)
            for ten_rs_coin in range(2): # Rs10 coin (0 or 1)
                if one_rs_coin + 2*two_rs_coin + 5*five_rs_coin + 10*ten_rs_coin == 10:    #1(1rs tot value)+2(2rs tot value)+5(5rs tot value)+10(10rs tot value)=10
                    print("Rs1:", one_rs_coin, "Rs2:", two_rs_coin, "Rs5:", five_rs_coin, "Rs10:", ten_rs_coin)
#6.Duplication in all three list
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]
combined = list1 + list2 + list3
duplicates = []
for item in combined:
       if list1.count(item) > 0 and list2.count(item) > 0 and list3.count(item) > 0:
        if item not in duplicates:
            duplicates.append(item)
print("Duplicates in all three lists:", duplicates)

#7.find the first non repeating number
numbers = [4, 1, 1, 2, 22, 4, 5, 2]
for num in numbers:         # Loop through each number
        if numbers.count(num) == 1:  # Check if it appears only once
         print("First non-repeating number is:", num)
         break      #breaking because don't want to repeat the loop for second repeating number
#8.Find the minimum element is a sorted list
numbers = [40,30,20,10]
print("The minimum number is", min(numbers))

#9.find adding 3 numbers from list gives target value
numbers = [10, 20, 30, 9]
target = 59
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:  # Check if the sum equals the target
                print("Triplet found:", numbers[i], numbers[j], numbers[k])
            break
#10.find the sum of numbers to find if there is a sub-list with sum equal to zero
nums = [4, 2, -3, 1, 6]
found = False
for i in range(len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total = total + nums[j]
        if total == 0:
            found = True
if found:
    print("Yes, a sub-list with sum 0 exists.")
else:
    print("No, sub-list with sum 0 does not exist.")

