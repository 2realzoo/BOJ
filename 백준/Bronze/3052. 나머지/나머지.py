import sys
input = sys.stdin.readlines

nums = list(map(lambda x:int(x.rstrip('\n')), input()))
remainders = set()
for num in nums:
    remainders.add(num % 42)
print(len(remainders))