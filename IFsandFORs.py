T = int(input())

for _ in range(T):
    n = int(input())
    result = [(i + 3) if i == 0 else (i * 2 if i % 2 == 0 else i ** 2) for i in range(n)]
    print(' '.join(map(str, result)))
