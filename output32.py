def sum_multiply(a,b,*more):
    sum_value = a+b
    m_value = a*b
    for i in more:
        sum_value += i
        m_value*=i
    return sum_value,m_value
s_m = sum_multiply(2,3,4)
print(s_m)