def bubble_sort(arr):
    n = len(arr)  # bilang ng elements sa list

    i = 0
    while i < n:  
        # bawat "pass" ng loop ay naglalagay ng pinakamalaking number sa dulo
        j = 0
        while j < n - i - 1:  
            # ikumpara ang magkatabing elements
            if arr[j] > arr[j + 1]:
                # kung mali ang order, i-swap sila
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        # pagkatapos ng bawat outer loop, sigurado na yung pinakamalaking value ay nasa tamang pwesto
        i += 1

    return arr


# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted:", numbers)
print("Sorted:", bubble_sort(numbers))
