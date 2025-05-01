#fin = open('Traversal/angry_bronze_jan16/2.in','r')
fin = open('angry.in','r')
fout = open('angry.out','w')
N = int(fin.readline())
bales = []
for i in range(N):
    bale = int(fin.readline())
    bales.append(bale)
bales = sorted(bales)
# bales = [int(fin.readline()) for _ in range(N)]
# bales.sort()

res = 0
for i in range(N):
    dis = 1
    posleft = i
    while True:
        nextpos = i
        while nextpos-1>=0 and bales[posleft]-bales[nextpos-1] <= dis:
            nextpos -= 1
        if nextpos == posleft:
            break
        posleft = nextpos
        dis += 1
    dis = 1
    posright = i
    while True:
        nextpos = i
        while nextpos + 1 < N and bales[nextpos+1]-bales[posright]<= dis:
            nextpos += 1
        if nextpos == posright:
            break
        posright = nextpos
        dis += 1
    res = max(res,posright-posleft+1)

#print(res)
fout.write(str(res))

# 爆炸中心每轮要更新：每次爆炸后必须用新炸到的 hay bale 作为新的爆炸中心继续扩散。

# 每轮可能炸多个：一轮爆炸可能炸掉多个 hay bale，不能只看一个方向或一个目标。