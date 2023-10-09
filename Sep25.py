
def f(m, n):
    '''the number of expression of m with some number less than n'''
    f_va = 0
    if n == 1:
        f_va = m
    elif m < n:
        f_va = f_free(m)
    else:
        f_va += f(m, n-1)
        k = 1
        while m - n*k > 0:
            f_va += f(m-n*k, n-1)
            k += 1
            
    return f_va

def f_free(m):
    '''the consisting number has no limitation'''
    f_va2 = 0
    if m == 1:
        f_va2 = 1
    for j in range(1, m):
        if j == 1:
            f_va2 += 1
        else:
            k = 1
            while m - j*k > 0:
                f_va2 += f_free(m - j*k)
                k+=1
    return f_va2
                    

print(f_free(4))