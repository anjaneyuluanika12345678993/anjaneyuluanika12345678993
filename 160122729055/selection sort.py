arr = [21,6,3,23]
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        if(arr[i]>arr[j]):
           c = arr[i]
           arr[i] = arr[j]
           arr[j] = c
print(arr)



