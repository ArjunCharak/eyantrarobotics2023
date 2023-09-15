def main():
    T = int(input())

    for _ in range(T):
        N = int(input())
        max_score = -1  # Initialized to an impossible score to guarantee updates on the first student
        top_students = []

        for _ in range(N):
            student, score = input().split()
            score = float(score)
            top_students = [student] if score > max_score else top_students + [student] if score == max_score else top_students
            max_score = score if score > max_score else max_score

        for student in sorted(top_students):
            print(student)
main()