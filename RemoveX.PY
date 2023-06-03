def removeX(s):
    chr = 'x'
    l = len(s)
    if len(s) == 0:
        return s
    smalleroutput = removeX(s[1:])
    if s[0] == chr :
        return ''+smalleroutput
    else:
        return s[0]+smalleroutput
    
string = input()
print(removeX(string))