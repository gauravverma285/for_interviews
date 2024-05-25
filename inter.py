# programe for prime or not

# n = int(input("Enter a number : ")) 
# flag = False
# if n==1:
#     print(n, "is not prime")
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             flag =True
#             break
#     if flag:
#         print(n, "number is not prime")
#     else:
#         print(n, "number is prime")
# else:
#     print("please enter the number that is greater from 1")



# programe for fobonacci serious

# n = int(input("enter a number"))

# n1 = 0
# n2 = 1
# cout = 0

# if n < 0:
#     print("please enter positive number")
# if n == 1:
#     print("f series is : ", n)
# else:
#     while cout < n:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         cout += 1


# programe for find factorial for given number

# n = int(input("Enter a number : "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
# print(fact)


# write the code for print the number of even number from 1 to 100 range also every printed number is addtion is 5

# for i in range(1, 101):
#     if i%2==0:
#         print(i+5)



# write the code for find the second largest number from array array is a user input



# remove the duplicate tems from array and list a = [2,3,6,22,3,2,6]

# a = [2,3,6,22,3,2,6,6,6,6,2]


# b = set(a)
# c = list(b)
# print(c)

# new_list = []

# for i in a:
#     if i in new_list:
#         continue
#     new_list.append(i)

# print(new_list)


# we have a array like a = [1,2,3,4,5,6,7,8,9] now break in three array and find largest number from every arry.

# a = [1,2,3,4,5,6,7,8,9]

# list1 = []
# list2 = []
# list3 = []
# list4 = []

# length = len(arr)
# for i in arr:
#     if i <= arr[2]:
#         list1.append(i)
#         list4.append(list1)
#     elif i > arr[2] and i >= arr[6]:
#         list2.append(i)
#         list4.append(list2)
#     else:
#         list3.append(i)
#         list4.append(list3)
# print(list1, list2, list3)


# n = int(input("Enter the number : ")) # 7

# n1 = 0 # 1 1 2 3 5
# n2 = 1 # 1 2 3 5 8
# count = 0 # 1 2 3

# if n < 0:
#     print("please enter the positive number.")
# if n == 1:
#     print("series is ", n)
# else:
#     while count < n: # 0<7 1<7 2<7 3<7 4<7 5<7
#         print(n1) # 0 1 1 2 3 5
#         nth = n1 + n2 # 1 2 3 5 8 13
#         n1 = n2 # 1 1 2 3 5 8
#         n2 = nth # 1 2 3 5 8 13
#         count += 1 #1 2 3 4 5 6


# -------------------- star pattern -----------------

# n = int(input("Enter the number : "))

# for row in range(1, n+1):
#     for col in range(1, row+1):
#         print("*", end="")
#     print("\n")


# n = int(input("Enter the number : "))

# for i in range(1, n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(1, 2*i):
#         print("*", end="")
#     print("\n")


# *****
# ****
# ***
# **
# *

# n = int(input('Enter the number : '))

# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print("\n")

# *****
# *****
# *****
# *****
# *****

# n = int(input("enter the number : "))

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print("*", end="")
#     print("\n")

# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# n = int(input("Enter the number : "))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print("\n")

#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * *

# n = int(input("Enter the number : "))

# for i in range(1, n+1):
#     for j in range(0, n-i):
#         print(" ", end="")
#     for k in range(1, i+1):
#         print("*", end=" ")
#     print('\n')


        #           *   
        #          *  *   
        #         *  *  *   
        #        *  *  *  *   
        #       *  *  *  *  *   
        #      *  *  *  *  *  *   
        #     *  *  *  *  *  *  *   
        #    *  *  *  *  *  *  *  *   
        #   *  *  *  *  *  *  *  *  *   
        #  *  *  *  *  *  *  *  *  *  *

# n = int(input("Enter the number : "))

# for i in range(1, n+1):
#     for j in range(0, n-i):
#         print(" ", end="")
#     for k in range(1, i+1):
#         print("* ", end=" ")
#     print("\n")


                #   * * * * * * * * * * * 
                #    * * * * * * * * * * 
                #     * * * * * * * * * 
                #      * * * * * * * * 
                #       * * * * * * * 
                #        * * * * * * 
                #         * * * * * 
                #          * * * * 
                #           * * * 
                #            * * 
                #             *

# n = int(input("Enter the number : "))

# for i in range(n, 0, -1):
#     for j in range(0, n-i):
#         print(" ", end="")
#     for k in range(0, i):
#         print("* ", end="")
    # print("\n")


    #           * 
    #          * * 
    #         * * * 
    #        * * * * 
    #       * * * * * 
    #      * * * * * * 
    #     * * * * * * * 
    #    * * * * * * * * 
    #   * * * * * * * * * 
    #    * * * * * * * * 
    #     * * * * * * * 
    #      * * * * * * 
    #       * * * * * 
    #        * * * * 
    #         * * * 
    #          * * 
    #           *

# n = int(input("enter the number : "))

# for i in range(1, n+1):
#     for j in range(0, n-i):
#         print(" ", end="")
#     for k in range(0, i):
#         print("* ", end="")
#     print('')

# for i in range(n-1, 0, -1):
#     for j in range(0, n-i):
#         print(" ", end="")
#     for k in range(0, i):
#         print("* ", end="")
#     print('')



# Enter the number of rows: 7
# *  
# * *  
# * * *  
# * * * *  
# * * * * *  
# * * * * * *  
# * * * * * * *  
# * * * * * * *  
# * * * * * *  
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

# n = int(input("Enter the number : "))

# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print("")

# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print("")


# Enter the number of rows: 5

#    * * * * * * 
#     * * * * * 
#      * * * * 
#       * * * 
#        * * 
#         * 
#         * 
#        * * 
#       * * * 
#      * * * * 
#    * * * * * 
#   * * * * * *

# n = int(input("Enter the number : "))

# for i in range(n, 0, -1):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(i):
#         print("* ", end="")
#     print("")

# for i in range(1, n+1):
#     for j in range(0, n-i):
#         print(" ", end="")
#     for k in range(0, i):
#         print("* ", end="")
#     print("")


# Enter the number of rows: 5
# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5  

# n = int(input("Enter the number : "))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(i, end="")
#     print("")


# Enter the number of rows: 5
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# n = int(input("Enter the number : "))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print("")


# Enter the number of rows: 5
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

# n = int(input("Enter the number : "))

# for i in range(1, n+1):
#     for j in range(0, (n-i+1)):
#         print(i, end="")
#     print("")


# Enter the number of rows: 6
# 6 6 6 6 6 6 
# 6 6 6 6 6 
# 6 6 6 6 
# 6 6 6 
# 6 6 
# 6

# n = int(input("Enter the number : "))

# for i in range(1, n+1):
#     for j in range(0, (n-i+1)):
#         print(n, end="")
#     print("")


# Enter the number of rows: 6
# 6 6 6 6 6 6 
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1

# n = int(input("Enter the number : "))

# for i in range(n, 0, -1):
#     for j in range(0, (i)):
#         print(i, end="")
#     print('')


# 1 
# 2 3 4 
# 5 6 7 8 9
# num = 1
# for i in range(0, 3):
#     for j in range(0, (2*i+1)):
#         print(num, end='')
#         num = num +1
#     print("")



# **********
# *        *
# *        *
# *        *
# **********

# n = int(input("Enter the number : "))
# height = 5
# width = 10

# for i in range(0, height):
#     for j in range(0, width):
#         if i==0 or i == 5-1 or j == 0 or j == 10-1:
#             print("*", end="")
#         else:
#             print(" ", end="") 
#     print()


# ********************
# **                **
# * *              * *
# *  *            *  *
# *   *          *   *
# *    *        *    *
# *     *      *     *
# *      *    *      *
# *       *  *       *
# ********************

# height = 10
# width = 20

# for i in range(0, height):
#     for j in range(0, width):
#         if i==0 or i == height-1 or j == 0 or j == width-1 or i==j or j==width-i-1:
#             print("*", end="")
#         else:
#             print(" ", end="") 
#     print()


# write the code for find the second largest number from array array is a user input

# n = int(input("Enter the number of elements : "))

# my_array = []

# for i in range(n):
#     ele = input("enter element {} : ".format(i+1))
#     my_array.append(ele)
# print(my_array)

# sorted_array = sorted(my_array)
# print(sorted_array)

# largest_element = sorted_array[-2]

# print(largest_element)

# 2nd way -------------- 2nd way


# import random

# # List of names
# names = ["Aradhna", "Gaurav", "Bhawna", "Manjit"]

# # Randomly select a name and print it
# random_name = random.choice(names)
# print(random_name)





# --------------

# def find_second_largest(arr):
#     # Convert input string to list of integers
#     arr = list(map(int, arr.split()))

#     # Initialize variables to store the largest and second largest numbers
#     largest = float('-inf')
#     second_largest = float('-inf')

#     # Iterate through the array
#     for num in arr:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num != largest:
#             second_largest = num

#     return second_largest

# # Take user input for the array
# array_input = input("Enter the array elements separated by space: ")

# # Call the function to find the second largest number
# second_largest_number = find_second_largest(array_input)

# # Print the second largest number
# print("The second largest number in the array is:", second_largest_number)



# ------------------------------------------------
# find the largest emement from array and array is user input ((((((((((((((()))))))))))))))
# arr = input("Enter the array element seperated by space : ")

# # my_array = list(map(int, arr.split()))
# my_array = list(map(int, arr.split()))

# largest = my_array[0]

# for i in my_array:
#     if i > largest:
#         largest = i
# print(largest)


# find the second largest element from array and array is user input ((((((((((((()))))))))))))

# arr = input("enter the array element seperated by spaces : ")

# my_arry = list(map(int, arr.split()))

# largest = second_largest = float('-inf')

# for i in my_arry:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i != largest:
#         second_largest = i
# print("largest :: ", largest)
# print("second_largest :: ", second_largest)




        

