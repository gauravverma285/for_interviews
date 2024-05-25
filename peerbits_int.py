# diffrence beetween contains and icontains (((((((((())))))))))

   "contains"
# The contains lookup is case-sensitive. This means that the query will only match entries where the 
# exact case of the substring matches the case in the database field.

# example:
# from myapp.models import MyModel

# # This will match entries where 'title' contains the exact substring 'Hello'
# results = MyModel.objects.filter(title__contains='Hello')

# If an entry has title as "hello world", it will not match because of the case difference.

 "icontains"

# The icontains lookup is case-insensitive. This means that the query will match entries regardless 
# of the case of the substring in both the query and the database field.

# example :
# from myapp.models import MyModel

# # This will match entries where 'title' contains the substring 'Hello', 'hello', 'HELLO', etc.
# results = MyModel.objects.filter(title__icontains='Hello')

# If an entry has title as "hello world", it will match because the case is ignored.


# -----------------------------------------------------------------------------------------------------------

### i have a students table in which i have 100 objects now i want to return only 8 
    #objects write the orm query in django and sql query also (((((((((((())))))))))))

# Django ORM Query
#     students = Student.objects.all()[:8]

# SQL Query
#     SELECT * FROM students LIMIT 8;


# ----------------------------------------------------------------------------------------

### how many types of join in sql ((((((((((((((()))))))))))))))

    # INNER JOIN: Returns only the rows that have matching values in both tables.
    # LEFT (OUTER) JOIN: Returns all rows from the left table and the matched rows from the right table. If no match is found, NULL values are returned for columns from the right table.
    # RIGHT (OUTER) JOIN: Returns all rows from the right table and the matched rows from the left table. If no match is found, NULL values are returned for columns from the left table.
    # FULL (OUTER) JOIN: Returns all rows when there is a match in either left or right table. Rows without a match in one of the tables will have NULL values for the columns of that table.
    # CROSS JOIN: Returns the Cartesian product of the two tables, meaning it returns all possible combinations of rows from both tables.
    # SELF JOIN: A self join is a regular join, but the table is joined with itself.


# ---------------------------------------------------------------------------------------

### li = [4,3,5,7,2,4,9] write the python code for set the decending order of list element

    # Method 1: Using sort() Method

    #     li = [4, 3, 5, 7, 2, 4, 9]
    #     li.sort(reverse=True)
    #     print(li)

    # Method 2: Using sorted() Function
    #     li = [4, 3, 5, 7, 2, 4, 9]
    #     sorted_li = sorted(li, reverse=True)
    #     print(sorted_li)


    # ------- logical code -----------

    # li = [4, 3, 5, 7, 2, 4, 9]

    # # Function to sort the list in descending order
    # def bubble_sort_descending(arr):
    #     n = len(arr)
    #     # Traverse through all list elements
    #     for i in range(n):
    #         # Last i elements are already in place
    #         for j in range(0, n-i-1):
    #             # Traverse the list from 0 to n-i-1
    #             # Swap if the element found is smaller than the next element
    #             if arr[j] < arr[j+1]:
    #                 arr[j], arr[j+1] = arr[j+1], arr[j]

    # # Call the function
    # bubble_sort_descending(li)
    # print("Sorted list in descending order:", li)
