import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0
result = 666

while True:
    if '666' in str(result):
        cnt += 1
    if cnt == N:
        break

    result += 1

print(result)
#이걸 진짜 노가다를 해야 되네