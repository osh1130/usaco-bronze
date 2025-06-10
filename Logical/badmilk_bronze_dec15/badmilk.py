from collections import defaultdict

fin = open('Logical/badmilk_bronze_dec15/1.in', 'r')
#fout = open('badmilk.out', 'w')

P, M, D, S = map(int, fin.readline().split())

person_drink_log = defaultdict(list)  # person -> list of (milk, time)
milk_drink_log = defaultdict(list)    # milk -> list of (person, time)
sick_list = []

# 读取饮用记录
for _ in range(D):
    person, milk, time = map(int, fin.readline().split())
    person_drink_log[person].append((milk, time))
    milk_drink_log[milk].append((person, time))

# 读取生病记录
sick_time = dict()
for _ in range(S):
    person, time = map(int, fin.readline().split())
    sick_list.append((person, time))
    sick_time[person] = time

max_victims = 0

for milk in range(1, M + 1):
    # 检查：所有生病的人是否在生病前喝过这瓶奶
    is_possible = True
    for sick_person, sick_t in sick_list:
        drank = False
        for m, t in person_drink_log[sick_person]:
            if m == milk and t < sick_t:
                drank = True
                break
        if not drank:
            is_possible = False
            break
    if not is_possible:
        continue

    # 统计喝过这瓶奶的健康人和病人（但在生病前）
    victims = set()
    for person, time in milk_drink_log[milk]:
        if person not in sick_time or time < sick_time[person]:
            victims.add(person)

    max_victims = max(max_victims, len(victims))

print(max_victims)
#fout.write(str(max_victims) + '\n')
#fout.close()
