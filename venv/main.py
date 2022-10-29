import math
def cube(b):
    return math.pow(b,3)
print(int(cube(5)))

try:
   cube(5)
except Exception as ex:
    print(f'Eror information: {ex}')


