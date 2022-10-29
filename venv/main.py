def cube(n):
    a = n*n*n
    return a


try:
    cube(5)
except Exception as ex:
    print(f'Eror information: {ex}')