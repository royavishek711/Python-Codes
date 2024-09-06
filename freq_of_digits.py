
def freq(arr, n):
#     The dictionary hashh will have keys ranging from 1 to n, with each key's initial value set to 0.
# This dictionary will be used to keep track of the frequencies of numbers in the array arr[] that are within the range 1 to n.
    hashh={i:0 for i in range(1, n+1)}

#     Condition if a in hashh: It checks if the current element a is a key in the dictionary hashh. This ensures that only numbers between 1 and n are counted, and numbers outside this range are ignored.
# Action hashh[a] += 1: If a is a valid key, its count (or frequency) in the dictionary is incremented by 1.
    for x in arr:
        if x in hashh:
            hashh[x]+=1
    
#     b in range(n): It loops over the indices of the array from 0 to n-1.
# arr[b] = hashh[b + 1]: For each index b, it updates the value at arr[b] with the frequency of b + 1 (because we need to use 1-based indexing for the numbers).
    for y in range(n):
        arr[y]=hashh[y+1]

    return arr

arr=list(map(int, input("Enter the elements: ").split()))
size=len(arr)

print(freq(arr, size))