def example_1():
    my_list = [1, 2, 3, 4, 5]
    print("Example 1: Creating and accessing a list")
    print("List:", my_list)
    print("First element:", my_list[0])
    print("Last element:", my_list[-1])

def example_2():
    my_list = [1, 2, 3]
    print("Example 2: Modifying a list")
    print("Original list:", my_list)
    my_list.append(4)
    print("After appending 4:", my_list)
    my_list[0] = 0
    print("After changing the first element to 0:", my_list)

def example_3():
    my_list = [1, 2, 3, 4, 5]
    print("Example 3: List slicing")
    print("Original list:", my_list)
    sliced_list = my_list[1:4]
    print("Sliced list [1:4]:", sliced_list)

def example_4():
    my_list = [1, 2, 3, 4, 5]
    print("Example 4: Iterating over a list")
    print("List:", my_list)
    for item in my_list:
        print(item)

def example_5():
    my_list = [1, 2, 3, 4, 5]
    print("Example 5: List comprehension")
    print("List:", my_list)
    squared_list = [x**2 for x in my_list]
    print("Squared list:", squared_list)
    

def example_6():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print("Example 6: Combining lists")
    print("List 1:", list1)
    print("List 2:", list2)
    combined_list = list1 + list2
    print("Combined list:", combined_list)

def example_7():
    my_list = [1, 2, 3, 4, 5]
    print("Example 7: Removing elements from a list")
    print("Original list:", my_list)
    my_list.remove(3)
    print("After removing 3:", my_list)
    my_list.pop()
    print("After popping the last element:", my_list)

def example_8():
    my_list = [1, 2, 3, 4, 5]
    print("Example 8: Finding elements in a list")
    print("List:", my_list)
    if 3 in my_list:
        print("3 is in the list.")
    else:
        print("3 is not in the list.")
    count_of_2 = my_list.count(2)
    print("Count of 2 in the list:", count_of_2)

def example_9():
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Example 9: Sorting a list")
    print("Unsorted list:", my_list)
    my_list.sort()
    print("Sorted list:", my_list)

def example_10():
    my_list = [1, 2, 3, 4, 5]
    print("Example 10: Reversing a list")
    print("Original list:", my_list)
    my_list.reverse()
    print("Reversed list:", my_list)

print("Welcome to the List Examples Program!")
while True:
    try:
        user_choice = int(input("Enter a number between 1 and 10 to run an example (or any other number to exit): "))
        if 1 <= user_choice <= 10:
            if user_choice == 1:
                example_1()
            elif user_choice == 2:
                example_2()
            elif user_choice == 3:
                example_3()
            elif user_choice == 4:
                example_4()
            elif user_choice == 5:
                example_5()
            elif user_choice == 6:
                example_6()
            elif user_choice == 7:
                example_7()
            elif user_choice == 8:
                example_8()
            elif user_choice == 9:
                example_9()
            elif user_choice == 10:
                example_10()
        else:
            print("Exiting the program. Goodbye!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")


