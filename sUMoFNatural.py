def SumN(n):
    if n==0:
        return 0
    smallOuput = SumN(n-1)
    output = smallOuput+n
    return output
n = int(input())
print(SumN(n))