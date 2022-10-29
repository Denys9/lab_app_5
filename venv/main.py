def num(a):
    try:
        if a < 0:
            return False
        if a > 0:
            return True


    except Exception as ex:
        print(f'Eror information: {ex}')
res = num(5)
print(res)
