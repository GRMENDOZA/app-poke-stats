'''
fibo(n) -> nth fibonacci
n: posicion
0 1 1 2 3 5 8 13 21...

fibo(0)---> 0
fibo(1)----> 1
fibo(3)---->2

n>=0 constraints int

nth = (n-1) + (n-2)
'''

def fibo(n:int) -> int:
    if isinstance(n, int) and n >= 0:
        n1, n2 = 0, 1
        count = 0

        while count < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

        return n1
    else:
        return 'El valor debe ser numerico'
    
if __name__ == '__main__':
    assert fibo(3) == 2
    assert fibo(4) == 3
    assert fibo(10) == 55
    assert fibo(1) == 1
    assert fibo('2') == 1
