import math

def jump_search(arr, key):
    n = len(arr)
    comparisons = 0

    step = int(math.sqrt(n))
    prev = 0

    # Jumping phase
    while prev < n and arr[min(step, n) - 1] < key:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return False, comparisons

    # Linear search phase
    while prev < min(step, n):
        comparisons += 1
        if arr[prev] == key:
            return True, comparisons
        prev += 1

    return False, comparisons


test_cases = int(input().strip())

while test_cases > 0:
    n = int(input().strip())
    arr = list(map(int, input().split()))
    key = int(input().strip())

    is_present, comparisons = jump_search(arr, key)

    if is_present:
        print("Present", comparisons)
    else:
        print("Not Present", comparisons)

    test_cases -= 1
