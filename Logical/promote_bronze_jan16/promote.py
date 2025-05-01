#fin = open('Logical/promote_bronze_jan16/4.in','r')
fin = open('promote.in','r')
fout = open('promote.out','w')
data = [list(map(int, fin.readline().split())) for _ in range(4)]
add=0
res=''
for i in range(3,0,-1):
    addFrom = data[i][1]-data[i][0]
    print(add+addFrom)
    res = str(add + addFrom) + '\n' + res
    add = add+addFrom

# res_list.reverse()  # 翻转列表
# res = '\n'.join(map(str, res_list)) + '\n'
fout.write(res)