'''#selection sort
a = list(map(int, input("Enter numbers: ").split()))

n = len(a)

for i in range(n):
    min = i

    for j in range(i + 1, n):
        if a[j] < a[min]:
            min = j

    a[i], a[min] = a[min], a[i]

print("Sorted array:", a)'''



#binary search
a = list(map(int, input("Enter numbers: ").split()))
tar = int(input("Enter target number: "))

low = 0
high = len(a) - 1

while low <= high:
    mid = (low + high) // 2

    if a[mid] == tar:
        print("Found at index:", mid)
        break

    elif a[mid] < tar:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Target not found")