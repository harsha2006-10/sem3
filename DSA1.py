def array(arr, value, index):
    arr.append(0)                
    for i in range(len(arr) -1, index, -1):
        arr[i] = arr[i - 1]      
    arr[index] = value         
arr = [1, 2, 3, 4]
array(arr, 10,4)
print(arr) 

