# Dan Wu
# 11/12/2020
# Write a function that takes as a parameter a list and reverses the order of the elements in that list.

def reverse_list(list) :
    """takes a list as parameter and reverses the order of elements in the list """
    i = 0
    j = len ( list ) - 1
    while (i < j) :
        temporary = list[i]
        list[i] = list[j]
        list[j] = temporary
        i += 1
        j -= 1

   