def merge(a1,a2,a):
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(a2):
        if (a[i] < a[j]):
            a[k] = a[i]
            k = k+1
            i = i+1
        else:
            a[k] = a[j]
            k = k+1
            j = j+1
    while i < len(a1):
        a[k] = a[i]
        k = k+1
        i = i+1
    while i < len(a2):
        a[k] = a[j]
        k = k+1
        j = j+1
def mergeSort(a):
    if len(a) == 0 or len(a) == 1:
        return
    mid = len(a)//2
    a1= a[0:mid]
    a2= a[mid:]

    mergeSort(a1)
    mergeSort(a2)

    mergeSort(a1, a2, a)
n= int(input())
a=list(int(i) for i in input().strip().split(' '))
mergeSort(a)
print(*a)
