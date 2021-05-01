# Bubble Sort
# It is a comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped
# if they are not in order.
#
# Bubble Sort is one of the most straightforward sorting algorithms. Its name comes from the way the algorithm works:
# With every new pass, the largest element in the list “bubbles up” toward its correct position.
#
# Bubble sort consists of making multiple passes through a list, comparing elements one by one, and swapping adjacent
# items that are out of order.

def bubble_sort(list):
    # Swap the elements to arrange in order

    # Start looking at each item of the list one by one,
    # comparing it with its adjacent value. With each
    # iteration, the portion of the array that you look at
    # shrinks because the remaining items have already been
    # sorted.
    for iter_num in range(len(list) - 1, 0, -1):
        for idx in range(iter_num):
            if list[idx] > list[idx + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp


list = [19, 2, 31, 45, 6, 11, 121, 27]
print(f"Bubble sort: {list} -> ", end="")
bubble_sort(list)
print(f"{list}")
# When the above code is executed, it produces the following esult − [2, 6, 11, 19, 27, 31, 45, 121]


# Merge Sort Merge sort first divides the array into equal halves and then combines them in a sorted manner.
#
# Merge sort is a very efficient sorting algorithm. It’s based on the divide-and-conquer approach, a powerful algorithmic
# technique used to solve complex problems.
#
# To properly understand divide and conquer, you should first understand the concept of recursion. Recursion involves
# breaking a problem down into smaller subproblems until they’re small enough to manage. In programming, recursion is
# usually expressed by a function calling itself.
def merge_sort(unsorted_list):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(unsorted_list) <= 1:
        return unsorted_list
    # Find the middle point and devide it
    middle = len(unsorted_list) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return (merge(left_list, right_list))


# Merge the sorted halves
def merge(left_half, right_half):
    res = []

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(left_half) != 0 and len(right_half) != 0:
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])

    # If you reach the end of either array, then you can
    # add the remaining elements from the other array to
    # the result and break the loop
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Merge sort: {unsorted_list} -> {merge_sort(unsorted_list)}")
# When the above code is executed, it produces the following result − [11, 12, 22, 25, 34, 64, 90]


# Insertion Sort
# Insertion sort involves finding the right place for a given element in a sorted list. So in beginning we compare the
# first two elements and sort them by comparing them. Then we pick the third element and find its proper position among
# the previous two sorted elements. This way we gradually go on adding more elements to the already sorted list by putting
# them in their proper position.
#
# Like bubble sort, the insertion sort algorithm is straightforward to implement and understand. But unlike bubble sort,
# it builds the sorted list one element at a time by comparing each item with the rest of the list and inserting it into
# its correct position. This “insertion” procedure gives the algorithm its name.
def insertion_sort(input_list):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(input_list)):
        # Initialize the variable that will be used to
        # find the correct position of the element
        j = i - 1
        # This is the element we want to position in its
        # correct place
        nxt_element = input_list[i]
        # Compare the current element with next one

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while (input_list[j] > nxt_element) and (j >= 0):
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            input_list[j + 1] = input_list[j]
            j = j - 1

        # When you finish shifting the elements, you can position
        # `nxt_element` in its correct location
        input_list[j + 1] = nxt_element


list = [19, 2, 31, 45, 30, 11, 121, 27]
print(f"Insertion sort: {list} - > ", end="")
insertion_sort(list)
print(f"{list}")
# When the above code is executed, it produces the following result − [2, 11, 19, 27, 30, 31, 45, 121]


# Shell Sort
# Shell Sort involves sorting elements which are away from each other. We sort a large sublist of a given list and go on
# reducing the size of the list until all elements are sorted. The below program finds the gap by equating it to half
# of the length of the list size and then starts sorting all elements in it. Then we keep resetting the gap until the
# entire list is sorted.

def shell_sort(input_list):
    # Start with a big gap, then reduce the gap
    gap = len(input_list) // 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, len(input_list)):
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = input_list[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            # Sort the sub list for this gap

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j - gap

            # put temp (the original a[i]) in its correct location
            input_list[j] = temp

        # Reduce the gap for the next element
        gap = gap // 2


list = [19, 2, 31, 45, 30, 11, 121, 27]
print(f"Shell sort: {list} -> ", end="")
shell_sort(list)
print(f"{list}")
# When the above code is executed, it produces the following result − [2, 11, 19, 27, 30, 31, 45, 121]


# Selection Sort
# In selection sort we start by finding the minimum value in a given list and move it to a sorted list. Then we repeat
# the process for each of the remaining elements in the unsorted list. The next element entering the sorted list is
# compared with the existing elements and placed at its correct position. So at the end all the elements from the
# unsorted list are sorted.
def selection_sort(input_list):
    for idx in range(len(input_list)):

        min_idx = idx
        for j in range(idx + 1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        # Swap the minimum value with the compared value

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


l = [19, 2, 31, 45, 30, 11, 121, 27]
print(f"Selection sort: {l} -> ", end="")
selection_sort(l)
print(f"{l}")
# When the above code is executed, it produces the following result − [2, 11, 19, 27, 30, 31, 45, 121]