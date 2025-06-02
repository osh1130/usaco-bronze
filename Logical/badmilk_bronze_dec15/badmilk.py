from collections import defaultdict

fin = open('Logical/badmilk_bronze_dec15/1.in','r')
person = defaultdict(list)  # key: person, value: list of (milk, time)
milk_consumption = defaultdict(list)  # key: milk, value: list of (person, time)
sick = []

P, M, D, S = map(int, fin.readline().split())
for i in range(D):
    people, milk, time = map(int, fin.readline().split())
    milk_consumption[milk].append((people, time))
    person[people].append((milk, time))

for j in range(S):
    p, t = map(int, fin.readline().split())
    sick.append((p, t))

print(person)