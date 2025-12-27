arr =[4,5,6,2,3,1,2,3,2,6,7,8,9,10,12,13]

count = [0] * 10001

def count_sort(arr):
    global count
    for i in range(len(arr)):
        count[arr[i]] += 1

    for j in range(len(count)):
        if count[j]:
            for _ in range(count[j]):
                print(j)
