def compute_distance(x1, y1, x2, y2):
    squared_distance = (x2 - x1)**2 + (y2 - y1)**2
    distance = squared_distance**0.5
    return round(distance, 2)

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    print(f"Distance: {compute_distance(x1, y1, x2, y2):.2f}")
