arr =[4,5,6,2,3,1,2,3,2,6,7,8,9,10,12,13]

count = [0] * 10001

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

def quick_sort(arr, start, end):
    if (start > end):
        return
    
    left_idx = start + 1
    right_idx = end
    pivot = start

    while (left_idx <= right_idx):
        while left_idx <= end and arr[left_idx] <= arr[pivot]:
            left_idx += 1
        while right_idx > start and arr[right_idx] >= arr[pivot]:
            right_idx -= 1
        if right_idx < left_idx:
            arr[right_idx], arr[pivot] = arr[pivot], arr[right_idx]
        else:
            arr[right_idx], arr[left_idx] = arr[left_idx], arr[right_idx]
    
    quick_sort(arr, start, right_idx - 1)
    quick_sort(arr, right_idx + 1, end)

def count_sort(arr):
    global count
    for i in range(len(arr)):
        count[arr[i]] += 1

    for j in range(len(count)):
        if count[j]:
            for _ in range(count[j]):
                print(j)




