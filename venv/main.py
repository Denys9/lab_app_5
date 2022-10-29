def print_rec(a, b):
    for i in range(0, a):
        for j in range(0, b):
            print('*', end="")
        print()
    print()


try:
    print_rec(3, 4)
except Exception as ex:
    print(f'Eror information: {ex}')

