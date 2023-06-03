def isPalindrome(arr):
    if arr <= 0:
        return True
    if arr[0] != arr[len(arr)-1]:
        return False
    return isPalindrome(arr[1:-1])

arr= input()
if isPalindrome(arr):
    print("true")
else:
    print("false")