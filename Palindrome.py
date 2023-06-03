def checkPalindrome(n):
    temp = n
    rev = 0
    while(n > 0):
        dig = n % 10
        rev = rev*10 + dig
        n = n//10
    if(temp == rev):
        return True
    else:
        return False


n = int(input())
isPalindrome = checkPalindrome(n)
if isPalindrome == True:
    print("true")
else:
    print("false")