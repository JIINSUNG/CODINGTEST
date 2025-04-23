import sys
input = lambda: sys.stdin.readline().rstrip()


while True:
    word = input()
    if word == '0':
        break
    isPelin = True

    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            isPelin = False
            break
    print("yes" if isPelin else "no")
