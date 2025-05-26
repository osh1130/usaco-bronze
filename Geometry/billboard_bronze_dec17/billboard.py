# overlap with truck
def overlap_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    ox1 = max(ax1, bx1)
    oy1 = max(ay1, by1)
    ox2 = min(ax2, bx2)
    oy2 = min(ay2, by2)
    if ox1 < ox2 and oy1 < oy2:
        return (ox2 - ox1) * (oy2 - oy1)
    return 0

#fin = open('Geometry/billboard_bronze_dec17/1.in','r')
fin = open("billboard.in","r")
fout = open("billboard.out","w")
x1,y1,x2,y2 = map(int,fin.readline().split())
x3,y3,x4,y4 = map(int,fin.readline().split())
x5,y5,x6,y6 = map(int,fin.readline().split())

area1 = (x2-x1)*(y2-y1)
area2 = (x4-x3)*(y4-y3)

overlap1 = overlap_area(x1, y1, x2, y2, x5, y5, x6, y6)
overlap2 = overlap_area(x3, y3, x4, y4, x5, y5, x6, y6)

# visible area
visible_area = (area1 - overlap1) + (area2 - overlap2)
#print(visible_area)
fout.write(str(visible_area))