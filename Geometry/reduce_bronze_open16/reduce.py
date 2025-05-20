fin = open('reduce.in', 'r')
fout = open('reduce.out', 'w')

N = int(fin.readline())
points = [tuple(map(int, fin.readline().split())) for _ in range(N)]

points_sorted_x = sorted(points, key=lambda p: p[0])
points_sorted_y = sorted(points, key=lambda p: p[1])

candidates = set()

for i in range(3):
    candidates.add(points_sorted_x[i])
    candidates.add(points_sorted_x[-1 - i])
    candidates.add(points_sorted_y[i])
    candidates.add(points_sorted_y[-1 - i])

min_area = float('inf')

for remove_point in candidates:
    # 剩余点中 x 的最小最大，y 的最小最大
    xs = [p[0] for p in points if p != remove_point]
    ys = [p[1] for p in points if p != remove_point]

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    area = (max_x - min_x) * (max_y - min_y)
    if area < min_area:
        min_area = area

fout.write(str(min_area) + '\n')
fout.close()
