n = int(input())

i = 1
while i <= n:
    #SAPACES..............................
    s = 1
    while s <= n-i:
        print(' ',end='')
        s = s +1
    p = 1
    j = 1
     # INCREASNG SEQ..............
    while j <= i:
        print(p, end='')
        j = j+1
        p = p+1
    # DECREASING SEQ...............
    p = i-1
    while p >= 1:
        print(p, end='')
        p = p-1

    print()
    i = i+1 
    