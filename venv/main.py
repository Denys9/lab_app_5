
def is_prime(n):
    counter=0
    for i in range(1, n+1):
        if n%i == 0:
            counter +=1
    if counter==2:
        print(f'{n} є простим числом')
    else:
        print(f'{n} не є простим числом')


try:
    is_prime(5)
except Exception as ex:
    print(f'Eror information: {ex}')