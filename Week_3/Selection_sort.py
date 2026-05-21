def selection_sort_count(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return comparisons, swaps


# Driver Code
T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    comparisons, swaps = selection_sort_count(arr)

    # Print sorted array
    print(*arr)
    print(comparisons)
    print(swaps)
