
def fac(n):
    if n==0:
        return 1
    return fac(n-1)*n


try:
    print(fac(5))
except Exception as ex:
    print(f'Eror information: {ex}')