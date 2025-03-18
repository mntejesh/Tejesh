input = [10, 9, 8, 7, 6, 5, 1, 2, 3, 4]  # Elements are hard coded

def menu():
    print("\n1. Insertion Sort \n2. Merge Sort \n3. Quick Sort \n4. Selection Sort \n5. Shell Sort \n6. Heap Sort \n9. Exit")

def print_array():
    print("\nElements after sorting are ...")
    for i in input:
        print(i, end="\t")
    print()

# Insertion Sort Algorithm
def insertion_sort():
    for i in range(1, len(input)):
        element = input[i]
        j = i - 1
        while j >= 0 and input[j] > element:
            input[j + 1] = input[j]
            j -= 1
        input[j + 1] = element

def selection_sort():
    for i in range(len(input) - 1):
        minimum_value_index = i
        for j in range(i + 1, len(input)):
            if input[j] < input[minimum_value_index]:
                minimum_value_index = j
        # swap the minimum element with the first element
        input[i], input[minimum_value_index] = input[minimum_value_index], input[i]
        print_array()

def merging(low, mid, high):
    l1, l2, i = low, mid + 1, low
    b = [0] * len(input)
    while l1 <= mid and l2 <= high:
        if input[l1] <= input[l2]:
            b[i] = input[l1]
            l1 += 1
        else:
            b[i] = input[l2]
            l2 += 1
        i += 1
    while l1 <= mid:
        b[i] = input[l1]
        i += 1
        l1 += 1
    while l2 <= high:
        b[i] = input[l2]
        i += 1
        l2 += 1
    for i in range(low, high + 1):
        input[i] = b[i]

def merge_sort(low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid + 1, high)
        merging(low, mid, high)
        print_array()

def quick_sort(first, last):
    if first < last:
        pivot = first
        i, j = first, last
        while i < j:
            while input[i] <= input[pivot] and i < last:
                i += 1
            while input[j] > input[pivot]:
                j -= 1
            if i < j:
                input[i], input[j] = input[j], input[i]
        input[pivot], input[j] = input[j], input[pivot]
        quick_sort(first, j - 1)
        print_array()
        quick_sort(j + 1, last)

def shell_sort(n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = input[i]
            j = i
            while j >= interval and input[j - interval] > temp:
                input[j] = input[j - interval]
                j -= interval
            input[j] = temp
        interval //= 2
        print_array()

def heapify(n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and input[left] > input[largest]:
        largest = left
    if right < n and input[right] > input[largest]:
        largest = right
    if largest != i:
        input[i], input[largest] = input[largest], input[i]
        heapify(n, largest)

def heap_sort(n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        input[0], input[i] = input[i], input[0]
        heapify(i, 0)

def main():
    while True:
        menu()
        choice = int(input("\nSelect the sorting technique: "))
        if choice == 1:
            print("\n**Insertion Sort**")
            insertion_sort()
        elif choice == 2:
            print("\n**Merge Sort**")
            merge_sort(0, len(input) - 1)
        elif choice == 3:
            print("\n**Quick Sort**")
            quick_sort(0, len(input) - 1)
        elif choice == 4:
            print("\n**Selection Sort**")
            selection_sort()
        elif choice == 5:
            print("\n**Shell Sort**")
            shell_sort(len(input))
        elif choice == 6:
            print("\n**Heap Sort**")
            heap_sort(len(input))
        elif choice == 9:
            break
        else:
            print("Invalid choice")
        print_array()

if __name__ == "__main__":
    main()
