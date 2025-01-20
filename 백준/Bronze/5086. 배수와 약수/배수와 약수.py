import sys
input = lambda: sys.stdin.readline().rstrip()


# case1. factor
def factor(a, b):
    if b % a == 0:
        return True
    return False

# case2. multiple
def multiple(a, b):
    if a % b == 0:
        return True
    return False

while True:
    x, y = map(int, input().split())

    if x == 0 and y == 0:
        break
    if factor(x, y):
        print('factor')
    elif multiple(x, y):
        print('multiple')
    else:
        print('neither')