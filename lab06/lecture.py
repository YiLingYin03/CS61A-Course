def double_and_print(x):
    print('***', x, '=>', 2*x, '***')
    return x*x

def iterator_ex():
    s = range(3, 7)
    doubled = map(double_and_print, s)
    yield doubled


def list_partion(n, m):
    if n > 0 or m > 0:
        if n == m:
            yield str(m)
        
        yield list_partion(n,m-1)
            