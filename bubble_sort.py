def bubbleSort(arr, n):
    # code here
    
    for i in range(n):
        swapped=False
        
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                swapped=True
        
        if not swapped:
            break
    return arr

arr=[2,4,6,1,2,7,8]

print(bubbleSort(arr, len(arr)))
