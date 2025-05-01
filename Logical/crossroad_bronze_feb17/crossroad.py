fin = open('crossroad.in', 'r')
fout = open('crossroad.out', 'w')

N = int(fin.readline())

# 记录每头牛的历史（用ID做key，记录出现的side序列）
history = {}

for _ in range(N):
    cow_id, side = map(int, fin.readline().split())
    if cow_id not in history:
        history[cow_id] = []
    history[cow_id].append(side)

# 统计过马路的次数
cross_count = 0

for cow_id in history:
    sides = history[cow_id]
    for i in range(1, len(sides)):
        if sides[i] != sides[i - 1]:
            cross_count += 1

fout.write(str(cross_count) + '\n')
fin.close()
fout.close()
