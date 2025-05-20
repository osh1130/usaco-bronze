# fin = open('Geometry/teleport_bronze_feb18/7.in','r')
fin = open('teleport.in','r')
fout = open('teleport.out','w')
a,b,x,y = map(int,fin.readline().split())
if a > b:
    a,b = b,a
dis = abs(b - a)
if x > y:
    dis = min(dis,abs(b-x)+abs(a-y))
else:
    dis = min(dis,abs(a-x)+abs(b-y))
# print(dis)
fout.write(str(dis))
