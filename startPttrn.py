n = int(input())

i = 1
while i <= n:
    #SAPACES..............................
    s = 1
    while s <= n-i:
        print(' ',end='')
        s = s +1
    j = 1
     # INCREASNG SEQ..............
    while j <= i:
        print("*", end='')
        j = j+1
    # DECREASING SEQ...............
    
    print()
    i = i+1