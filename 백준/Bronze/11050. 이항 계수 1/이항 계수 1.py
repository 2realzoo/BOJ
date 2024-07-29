import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

def pac(num):
    n_pac = 1
    for i in range(num, 1, -1):
        n_pac *= i
    
    return n_pac

print(int(pac(N)/(pac(K) * pac(N-K))))
