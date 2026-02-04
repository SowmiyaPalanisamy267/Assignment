#1.filter person details under 18 from dictionaries filtering using lambda and mapping remaining using list
persons_details = {"Amit":45,
             "Bob":18,
             "Cath":32,
             "Dan":14}
print("person's details",persons_details)
above_18 = dict(filter(lambda item: item[1] >= 18, persons_details.items()))
print("Details of above 18",above_18)
under_18 = list(map(lambda item: item[0], filter(lambda item: item[1] < 18, persons_details.items())))
print("Details of under 18",under_18)


#2. lambda function to calculate the product of all numbers in list
from functools import reduce
numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)


#3. lambda function to check the square of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
is_even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", is_even)

squares_of_evens = [x**2 for x in is_even]
print("Squares of even numbers:", squares_of_evens)


#4.lambda function to find given string is a number
is_number = lambda s: s.isdigit()
print(is_number("123"))   
print(is_number("12.3")) 
print(is_number("abc"))

#5. lambda function extract date time and year from the given datetime object
from datetime import datetime
dt = datetime(2026, 2, 4, 12, 30, 45) # Create a datetime object

extract_date = lambda d: d.date()   
extract_time = lambda d: d.time()   
extract_year = lambda d: d.year     

print("Date:", extract_date(dt))
print("Time:", extract_time(dt))
print("Year:", extract_year(dt))


#6.Fibonacci series
Fibonacci_series = lambda n: n if n <= 1 else Fibonacci_series(n-1) + Fibonacci_series(n-2)

print(Fibonacci_series(1))
print(Fibonacci_series(8))
