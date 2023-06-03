def b_search(a,x,si,ei):
    if si>ei:
        return -1
    mid = (si+ei)//2

    if a[mid]==x:
        return mid
    elif a[mid]>x:
        return b_search(a,x,si,mid-1)
    else:
        return b_search(a,x,mid+1,ei)
print(b_search([1,2,3,4,5,6,7,8,9],6,0,9))