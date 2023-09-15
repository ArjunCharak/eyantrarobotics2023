def generate_pattern(n):
    for i in range(n, 0, -1):
        pattern = ["*"] * i 
        for j in range(4, i, 5):
            pattern[j] = "#"
        print(''.join(pattern))

T = int(input())
for _ in range(T):
    N = int(input())
    generate_pattern(N)