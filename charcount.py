T = int(input())
for _ in range(T):
    str_input = input()[1:]
    print(','.join(str(len(word)) for word in str_input.split()))