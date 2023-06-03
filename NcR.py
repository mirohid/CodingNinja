def ncr(n , r):
    n_fact  = fact(n)
    r_fact = fact(r)
    n_r_fact = fact(n-r)
    ans = n_fact//(r_fact*n_r_fact)
ncr(10,2)