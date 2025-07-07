fin = open('taming.in', 'r')
fout = open('taming.out', 'w')

#fin = open('Logical/taming_bronze_feb18/10.in','r')
N = int(fin.readline())
A = list(map(int, fin.readline().split()))
A[0] = 0

for i in range(N):
    if A[i] != -1:
        d = A[i]
        for j in range(i-d, i+1):
            if j < 0:
                fout.write(str(-1))
                fin.close()
                fout.close()
                exit()
            need = j - (i-d)
            if A[j] != -1 and A[j] != need:
                fout.write(str(-1))
                fin.close()
                fout.close()
                exit()
            A[j] = need

min_count = 0
max_count = 0
for v in A:
    if v == 0:
        min_count += 1
    if v == -1:
        max_count += 1
max_count += min_count

#print(min_count,max_count)
fout.write(str(min_count) + ' ' + str(max_count) + '\n')
fin.close()
fout.close()
