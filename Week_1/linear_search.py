def linear_search(arr, key):
    comparisons = 0

    for value in arr:
        comparisons += 1
        if value == key:
            return True, comparisons

    return False, comparisons


test_cases = int(input().strip())

while test_cases > 0:
    n = int(input().strip())
    arr = list(map(int, input().split()))
    key = int(input().strip())

    is_present, comparisons = linear_search(arr, key)

    if is_present:
        print("Present", comparisons)
    else:
        print("Not Present", comparisons)

    test_cases -= 1
