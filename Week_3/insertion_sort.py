def insertion_sort_count(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift elements greater than key
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return comparisons, swaps


# Driver Code
T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    comparisons, swaps = insertion_sort_count(arr)

    # Print sorted array
    print(*arr)
    print(comparisons)
    print(swaps)
