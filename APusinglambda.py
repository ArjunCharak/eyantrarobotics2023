def main():
    T = int(input())

    for _ in range(T):
        a1, d, n = map(int, input().split())
        ap_series = [a1 + i*d for i in range(n)]
        squares = [x*x for x in ap_series]
        print(*ap_series)
        print(*squares)
        print(sum(squares))

main()