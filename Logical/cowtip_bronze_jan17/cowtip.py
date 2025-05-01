#fin = open('Logical/cowtip_bronze_jan17/7.in','r')
fin = open('cowtip.in','r')
fout = open('cowtip.out','w')
N = int(fin.readline())
tip = [list(map(int,list(fin.readline().strip())))for _ in range(N)]
#print(tip)
time = 0
for i in range(N-1,-1,-1):
    for j in range(N-1,-1,-1):
        if tip[i][j]!=0:
            time+=1
            for a in range(i+1):
                for b in range(j+1):
                    tip[a][b]=1-tip[a][b]

            #print(tip)

#print(time)
fout.write(str(time))