def merge(arr, low , mid, high):
    temp=[]
    left=low
    right=mid+1

    while(left<=mid and right<=high):
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
        
    for i in range(low, high+1):
        arr[i]=temp[i-low]

    
            
def mergeSort(arr, low, high):
    if low>=high:
        return
    mid=(low+high)//2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    merge(arr, low, mid, high)
    return arr


arr=list(map(int, input().split()))
print(mergeSort(arr, 0, len(arr)-1))