def selectionSort(arr,n):
    #code here
    
    for i in range(n):
        
        minn=i
        
        for j in range(i+1, n):
            if arr[j]<arr[minn]:
                minn=j
            
        arr[i], arr[minn]=arr[minn], arr[i]
        
    return arr

arr=[1,4,7,2,4,5,9]
print(selectionSort(arr, len(arr)))
