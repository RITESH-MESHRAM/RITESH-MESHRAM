#!/usr/bin/env python
# coding: utf-8

# # Q.1 Write a program to print 'Hello Python' ten times.

# In[3]:


for i in range(10):     #for loop use
    print("Hello Python")


# In[18]:


i=1                  #while loop use
while i<=10:
    print("Hello Python")
    i+=1


# # Q.2 Write a program to print number from 1 to 10.

# In[4]:


for i in range(1,11):             #for loop use
    print(i)


# In[25]:


i=1                          #while loop use
while range(i<=10):
    print(i)
    i+=1


# # Q.3 Write a program to print sum of first ten number.

# In[5]:


sum = 0
for i in range(1, 11):
    sum += i
print("The sum of the first ten numbers is:", sum)


# # Q.4  Write a program to print n number entered by the user.

# In[7]:


n = int(input("Enter the number of integers you want to print: "))
for i in range(1, n+1):
    print(i, end=" ")


# # Q.5 Write a program to print sum of n numbers.

# In[4]:


sum = 0
print("Enter the Value of n: ")
n = int(input())
print("Enter " + str(n) + " Numbers: ")
for i in range(n):
    num = int(input())
    sum = sum+num
print("Sum of " + str(n) + " Numbers = " + str(sum))


# # Q.6 Write a program to print table of a number.

# In[9]:


n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=",n*i)


# # Q.7 Write a program to calculate the factorial of a numbers.

# In[12]:


n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print("The factorial of", n, "is", factorial)


# # Q.8 Write a program to print even number between 1 to 100.

# In[13]:


for i in range(2, 101, 2):
    print(i)


# # Q.9 Write a program to print odd number between 1 to 100.

# In[14]:


for i in range(1, 101, 2):
    print(i)


# # Q.10 Write a program to check whether a given number is palindrome or not.

# In[3]:


n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


# # Q.11 Write a program to find factors of a number.

# In[16]:


# Python Program to find the factors of a number

# This function computes the factor of the argument passed
def print_factors(x):
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num = 10

print_factors(num)


# # Q.12 Write a program to print the reverse of a number.

# In[2]:


# Function to reverse a number
def reverse_number(number):
    reverse = 0
    while number > 0:
        # Extract the last digit
        digit = number % 10
        # Add the digit to the reverse
        reverse = reverse * 10 + digit
        # Remove the last digit from the number
        number = number // 10
    return reverse

# Get input from the user
number = int(input("Enter a number: "))

# Call the function and print the reverse
reverse = reverse_number(number)
print("The reverse of", number, "is:", reverse)


# # Q.13 Write a program to print the sum of reverse of a number.

# In[3]:


# Function to reverse a number

def reverse_number(number):
    reverse = 0
    while number > 0:
        # Extract the last digit
        
        digit = number % 10
        # Add the digit to the reverse
        
        reverse = reverse * 10 + digit
        # Remove the last digit from the number
        
        number = number // 10
    return reverse

# Get input from the user

number = int(input("Enter a number: "))

# Call the function to reverse the number

reverse = reverse_number(number)

# Calculate the sum of the reversed number and print

sum_of_reverse = number + reverse
print("The sum of", number, "and its reverse", reverse, "is:", sum_of_reverse)


# # Q.14 Write a program to check whether a given number is prime or not 

# In[5]:


# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime

    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # If divisible, not a prime
    return True  # If not divisible, it's a prime

# Get input from the user
number = int(input("Enter a number: "))

# Call the function to check if the number is prime
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")


# # Q.15 Write a program to print prime number between 1 to 100.

# In[6]:


# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime

    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # If divisible, not a prime
    return True  # If not divisible, it's a prime

# Loop through numbers from 1 to 100 and print prime numbers
print("Prime numbers between 1 and 100:")
for number in range(1, 101):
    if is_prime(number):
        print(number)


# # Q.16 Write a program to print number is reverse order entered by the user.

# In[12]:


num = int(input("Enter by user"))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))


# # Q.17 Write a program to print the cube of all numbers from 1 to a given number.

# In[14]:


# Get input from the user
number = int(input("Enter a number: "))

# Print the cube of numbers from 1 to the given number
print("Cubes of numbers from 1 to", number, ":")
for i in range(1, number + 1):
    cube = i ** 3  # Calculate the cube of the current number
    print("Cube of", i, "is", cube)


# # 18 Write a program to count the total number of digits in a number.

# In[16]:


def count_digits(number):
    """
    Count the total number of digits in a given number.
    """
    # Convert the number to a string to easily access its digits
    number_str = str(number)
    # Use len() function to get the count of digits
    num_of_digits = len(number_str)
    return num_of_digits

# Get input from user
number = int(input("Enter a number: "))
# Call the count_digits() function and store the result
num_of_digits = count_digits(number)
# Print the result
print("Total number of digits in the number:", num_of_digits)


# # Q.19 write a program to print fibonacci series.

# In[19]:


def fibonacci_series(n):
    """
    Generate and print the Fibonacci series up to n terms.
    """
    # Initialize the first two terms of the series
    a, b = 0, 1
    # Print the first two terms
    print("Fibonacci series up to", n, "terms:")
    print(a, end=" ")
    print(b, end=" ")
    # Loop from 3rd to n-th term
    for i in range(3, n + 1):
        
        # Compute the next term by summing the previous two terms
        c = a + b
        # Print the next term
        print(c, end=" ")
        # Update a and b for the next iteration
        a, b = b, c
    print() 

n = int(input("Enter the number of terms for Fibonacci series: "))
fibonacci_series(n)


# # Q.20 Write a program to check whether a given number is amstrong number or not.

# In[23]:


def is_armstrong_number(number):
    num_str = str(number)

    num_of_digits = len(num_str)

    sum_of_powered_digits = 0
    
    for digit_char in num_str:
        
        digit = int(digit_char)
        
        sum_of_powered_digits += digit ** num_of_digits

    if sum_of_powered_digits == number:
        return True
    else:
        return False

number = int(input("Enter a number: "))

result = is_armstrong_number(number)
if result:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")


# # Q.21 Write a program to check whether a given number is strong number or not.

# In[33]:


sum1=0
num=int(input("Enter a number:"))
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum1=sum1+f
    num=num//10
if(sum1==temp):
    print("The number is a strong number")
else:
    
    print("The number is not a strong number")


# # Q.22 Write a program to check whether a given number is perfect number or not.

# In[36]:


n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")


# In[ ]:




