from itertools import permutations
#fin = open('Logical/hps_bronze_jan17/1.in','r')
fin = open('hps.in','r')
fout = open('hps.out','w')
N = int(fin.readline())
games = [tuple(map(int, fin.readline().split())) for _ in range(N)]

# permutations = [
#     (1, 2, 3),
#     (1, 3, 2),
#     (2, 1, 3),
#     (2, 3, 1),
#     (3, 1, 2),
#     (3, 2, 1)
# ]

permutation = list(permutations([1, 2,3]))

# def beats(x, y):
#     return (x == 1 and y == 3) or (x == 3 and y == 2) or (x == 2 and y == 1)

def beats(x, y):
    #是否相邻，并且是顺时针
    return (x-y+3)% 3 == 1

max_wins = 0

for perm in permutation:
    # 构造当前映射，例如 perm = (3, 1, 2)
    # 表示 1 → 3（Scissors）, 2 → 1（Hoof）, 3 → 2（Paper）
    mapping = {1: perm[0], 2: perm[1], 3: perm[2]}
    
    wins = 0
    for a, b in games:
        move1 = mapping[a]
        move2 = mapping[b]
        if beats(move1, move2):
            wins += 1

    max_wins = max(max_wins, wins)

#print(max_wins)
fout.write(str(max_wins))


# 有向图（Directed Graph），建立“谁打谁”的字典或邻接表（打败表）
# beats = {
#     1: [5],         # 1 打 5
#     2: [1],         # 2 打 1
#     3: [1],         # 3 打 1
#     4: [1],         # 4 打 1
#     5: [2, 3, 4]    # 5 打 2、3、4
# }
# def beats_fn(a, b):
#     return b in beats.get(a, [])
