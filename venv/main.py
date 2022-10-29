
def max_num(a,b):
    return max(a,b)
res = max_num(5,10)
print(res)


try:
    max(5,10)
except Exception as ex:
    print(f'Eror information: {ex}')
