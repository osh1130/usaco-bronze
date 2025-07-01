# fin = open('hoofball.in', 'r')
# fout = open('hoofball.out', 'w')
fin = open('Logical/hoofball_bronze_feb18/1.in','r')

N = int(fin.readline())
x = list(map(int, fin.readline().split()))

x.sort()

def target(i, x, N):
    if i == 0:
        return 1
    if i == N - 1:
        return N - 2
    if x[i] - x[i - 1] <= x[i + 1] - x[i]:
        return i - 1
    return i + 1

passto = [0] * N
to = [0] * N

for i in range(N):
    to[i] = target(i, x, N)
    passto[to[i]] += 1

print(passto)

answer = 0
for i in range(N):
    if passto[i] == 0:
        answer += 1
    j = to[i]
    if i < j and to[j] == i and passto[i] == 1 and passto[j] == 1:
        answer += 1

# fout.write(str(answer) + '\n')
# fin.close()
# fout.close()
