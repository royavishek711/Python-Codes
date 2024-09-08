# def insertionSort(arr, n):
#         #code here
        
#         for i in range(n-1):
            
#             for j in range(i+1, 0, -1):
                
#                 if arr[j]<arr[j-1]:
#                     arr[j], arr[j-1]=arr[j-1], arr[j]
#                 else:
#                     break

        
#         return arr

# recursive
def insertionSort(arr, i, n):
        #code here
        
        if i==n:
            return
            
        for j in range(i, 0, -1):
            
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1]=arr[j-1], arr[j]
            else:
                break
        
        insertionSort(arr, i+1, n)
        return arr

arr=[4,6,2,5,5,2,4]

print(insertionSort(arr, 0, len(arr)))