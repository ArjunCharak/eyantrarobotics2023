def main():
    T = int(input())

    for _ in range(T):
        n = int(input())
        L = list(map(int, input().split()))
        print(*L[::-1])
        print(*[x + 3 for i, x in enumerate(L[::3]) if i != 0])
        print(*[x - 7 for i, x in enumerate(L[::5]) if i != 0])
        print(sum(L[3:8]))
main()