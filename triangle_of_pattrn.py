n = int(input())
num = 1
space  = n - 1
for j in range(1, n+1):
    num = j
    for i in range(1, space + 1 ):
        print(" ", end='')
    space = space -1

    for i in range(1, j+1):
        print(num, end='')
        num = num +1
    num = num -2
    for i in range(1, j):
        print(num, end='')
        num = num - 1
    print()    