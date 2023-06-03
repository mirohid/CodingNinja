def SumOfArray(arr):
    l = len(arr)
    if l==0:
        return 0 
    smallerList = SumOfArray(arr[1:])
    sum = arr[0]+smallerList
    return sum
    pass
n = int(input())
print(SumOfArray(4))