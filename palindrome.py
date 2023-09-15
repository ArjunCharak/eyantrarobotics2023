def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

T = int(input())
for _ in range(T):
    str_input = input().strip()
    if is_palindrome(str_input):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")