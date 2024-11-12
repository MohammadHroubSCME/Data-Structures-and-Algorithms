def example_1():
    my_list = [10, 20, 30, 40, 50]
    print("Example 1: Creating and displaying a list")
    print("List:", my_list)
    print("Items:")
    for item in my_list:
        print("Item:", item)

def example_2():
    my_list = [5, 15, 25]
    print("Example 2: Processing a list")
    print("Original list:", my_list)
    my_list.append(35)
    print("After appending:", my_list)
    print("List items:")
    for index, item in enumerate(my_list):
        print(f"Item {index + 1}: {item}")

def example_3():
    my_list = [1, 2, 3, 4, 5]
    print("Example 3: List with duplicate items")
    print("List:", my_list)
    unique_items = set(my_list)
    print("Unique items:", unique_items)

def example_4():
    my_list = [10, 20, 30, 40]
    print("Example 4: List with new items")
    for item in my_list:
        print("Item:", item)

def example_5():
    my_list = [1, 2, 3, 4, 5]
    print("Example 5: Displaying list items")
    for i in range(len(my_list)):
        print("Item at position", i, ":", my_list[i])

def example_6():
    my_list = [1, 2, 3, 4, 5]
    print("Example 6: List with special processing")
    if len(my_list) > 3:
        print("The list contains more than 3 items.")
    else:
        print("The list contains 3 items or fewer.")

def example_7():
    my_list = [1, 2, 3, 4, 5]
    print("Example 7: Displaying list items")
    print("List items:")
    for index in range(len(my_list)):
        print("Item", index + 1, ":", my_list[index])

def example_8():
    my_list = [1, 2, 3, 4, 5]
    print("Example 8: Displaying list with special processing")
    if len(my_list) < 5:
        print("The list contains fewer than 5 items.")
    else:
        print("The list contains 5 items or more.")

# Calling the functions
example_1()
example_2()
example_3()
example_4()
example_5()
example_6()
example_7()
example_8()