from collections import defaultdict

#fin = open('Logical/badmilk_bronze_dec15/10.in','r')
fin = open('badmilk.in','r')
fout = open('badmilk.out','w')
N,M,D,S = map(int,fin.readline().split())
history = [list(map(int,fin.readline().split())) for _ in range(D)]
sicklog = [tuple(map(int,fin.readline().split())) for _ in range(S)]

drinks_by_person_time = defaultdict(lambda: defaultdict(list))  # 人 -> 时间 -> 牛奶列表
drinks_by_milk = defaultdict(set)                               # 牛奶 -> (人, 时间)
sick_time = dict()  

# 构建饮用记录数据结构
for p, m, t in history:
    drinks_by_person_time[p][t].append(m)  # 人p在时间t喝了牛奶m
    drinks_by_milk[m].add((p, t))          # 牛奶m在时间t被人p喝了

# 构建生病记录
# 写入/赋值：安全，自动创建。读取不存在的 key：会抛出 KeyError
for p, t in sicklog:
    sick_time[p] = t

# print(drinks_by_person_time)
# {1: defaultdict(<class 'list'>, {1: [1, 4], 4: [3], 2: [2]}), 3: defaultdict(<class 'list'>, {3: [1]}), 2: defaultdict(<class 'list'>, {5: [1], 7: [2]})}
# print(drinks_by_milk)
# {1: {(2, 5), (1, 1), (3, 3)}, 4: {(1, 1)}, 3: {(1, 4)}, 2: {(1, 2), (2, 7)}})
# print(sick_time)
# {1: 3, 2: 8}

possible = []

# 遍历每种牛奶
for milk in range(1, M + 1):  # 牛奶编号是 1 到 M
    is_possible = True

    # 对每一个生病者
    for person, sick_t in sick_time.items():
        drank = False

        # 查这个人生病前有没有喝过 milk
        if person in drinks_by_person_time:
            for time in drinks_by_person_time[person]:
                if time < sick_t and milk in drinks_by_person_time[person][time]:
                    drank = True
                    break

        if not drank:
            is_possible = False
            break  # 只要一个人生病前没喝过，就排除该牛奶

    if is_possible:
        possible.append(milk)

max_sick = 0
for milk in possible:
    infected = set()
    for p, t in drinks_by_milk[milk]:
        if p not in sick_time or t < sick_time[p]:
            infected.add(p)
    max_sick = max(max_sick, len(infected))
#print(max_sick)
fout.write(str(max_sick))
