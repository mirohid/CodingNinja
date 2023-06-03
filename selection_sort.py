def select_sort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i],a[min_index] = a[min_index],a[i]
    return a
print(select_sort([13,4,9,5,3]))
 