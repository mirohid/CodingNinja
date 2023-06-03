N = int(input())
for i in range(0, N):
    for j in range(0, N - i):
        if(i % 2 == 0):
            print(1, end='')
        else:
            print(0, end='')
print()