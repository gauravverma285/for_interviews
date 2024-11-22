########################################################

Question:
Write a Python program to check if a given number is a Harshad number (Niven number) or not.

Definition:
A Harshad number is a number that is divisible by the sum of its digits.


For example:
    18 is a Harshad number because 1 + 8 = 9 and 18 / 9 = 2
    22 is not a Harshad number because 2 + 2 = 4 and 22 / 4 != integer

Expected Input/Output:
Input:
A single integer.

Output:
Print "<number> is a Harshad number" if it satisfies the condition.
Print "<number> is not a Harshad number" otherwise.



def is_harshad_number(number):
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in str(number))
    
    # Check if the number is divisible by the sum of its digits
    if number % digit_sum == 0:
        return True
    else:
        return False

# Input from the user
number = int(input("Enter a number: "))

# Check and display the result
if is_harshad_number(number):
    print(f"{number} is a Harshad number")
else:
    print(f"{number} is not a Harshad number")



# 1. how to create lamda function for get data from candra db & sve to astra db 

# how many roles in aws 

# howm nay eks system  in aws 

# create docker yaml File

# tell about monitering tool in aws  & gcp

# 1
# 121
# 1221
# 123321
# 12344321
