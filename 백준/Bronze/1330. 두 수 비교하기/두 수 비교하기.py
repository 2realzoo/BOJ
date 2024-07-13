ab = input()
[a, b]= ab.split(' ')

a = int(a)
b = int(b)

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')