def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]
    return a

print(bubble_sort([19,9,4,7,3]))