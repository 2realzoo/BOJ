import sys
input = sys.stdin.readline

a = int(input().rstrip('\n'))
b = int(input().rstrip('\n'))
c = int(input().rstrip('\n'))

abc = str(a*b*c)
count_num = dict()
for i in range(len(abc)):
    if abc[i] in count_num:
        count_num[abc[i]] += 1
    elif abc[i] not in count_num:
        count_num[abc[i]] = 1

for j in range(10):
    if str(j) in count_num:
        print(count_num[str(j)])
    else:
        print('0')
