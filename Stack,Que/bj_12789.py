import sys

N = int(input())

line = list(map(int, sys.stdin.readline().split()))

start = 1

stack = []

for i in line:
    while stack and stack[-1] == start:
        stack.pop()
        start += 1

    if i == start:
        start += 1
    
    else:
        stack.append(i)

while stack and stack[-1] == start:
    stack.pop()
    start += 1

print("Nice" if start == N + 1 else "Sad")
