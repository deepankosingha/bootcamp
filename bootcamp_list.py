""" program to find even product and odd sum
    By: Deepanko Singha
    ID: 30479851
"""
n = int(input("enter no of items: "))
li = []
for i in range(n):
    user_item = int(input('enter integer: '))
    # adding the items to the list
    li.append(user_item)
even_odd_list = []
for i in range(n - 1, 0, -1):
    for j in range(i):
        # checking that the product is even and sum of elements is odd
        if ((li[i] * li[j]) % 2 == 0) and ((li[i] + li[j]) % 2 != 0):
            even_odd_list.append(li[i])
            even_odd_list.append(li[j])
print("the list with even product and odd sum: \n", even_odd_list)
