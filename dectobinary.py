def dec_to_binary(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    return dec_to_binary(n // 2) + str(n % 2)

def main():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        print(dec_to_binary(n).zfill(8))

main()
