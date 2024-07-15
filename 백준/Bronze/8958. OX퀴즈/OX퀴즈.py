import sys
input = sys.stdin.readline

t = int(input().rstrip('\n'))

for _ in range(t):
    answers = input().rstrip('\n')
    current_score = 0
    last_score = 0

    for i in answers:
        if i == 'O' :
            current_score += 1
        elif i == 'X' :
            current_score = 0
        last_score += current_score
    print(last_score)