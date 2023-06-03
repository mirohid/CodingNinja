def reverse(arr1):
    left = 0
    right = len(arr1)-1
    while (left<right):
        arr1[left], arr1[right] = arr1[right],arr1[left]
        left = left +1 
        right = right -1 

    return arr1
arr1 = [1,2,3,4,5,6]
print(reverse(arr1))
