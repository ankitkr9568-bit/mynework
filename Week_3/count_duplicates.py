# Count number of duplicate elements in an array

n = int(input("Enter size of array: "))

arr = []
freq = {}

print("Enter elements:")
for _ in range(n):
    x = int(input())
    arr.append(x)
    freq[x] = freq.get(x, 0) + 1

duplicates = 0

for count in freq.values():
    if count > 1:
        duplicates += count - 1

print("Total number of duplicate elements:", duplicates)
