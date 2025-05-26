def rect_area(x1, y1, x2, y2):
    return max(0, x2 - x1) * max(0, y2 - y1)

fin = open("billboard.in","r")
fout = open("billboard.out","w")
lx1, ly1, lx2, ly2 = map(int, fin.readline().split())  # lawnmower
fx1, fy1, fx2, fy2 = map(int, fin.readline().split())  # cow feed

tarp_area = rect_area(lx1, ly1, lx2, ly2)

# case 1: cow feed completely covers vertical range
if fy1 <= ly1 and fy2 >= ly2:
    # check if it cuts left
    if fx1 <= lx1 < fx2 < lx2:
        tarp_area = rect_area(fx2, ly1, lx2, ly2)
    # or cuts right
    elif lx1 < fx1 < lx2 <= fx2:
        tarp_area = rect_area(lx1, ly1, fx1, ly2)
    elif fx1 <= lx1 and fx2 >= lx2:
        tarp_area = 0

# case 2: cow feed completely covers horizontal range
elif fx1 <= lx1 and fx2 >= lx2:
    # check if it cuts bottom
    if fy1 <= ly1 < fy2 < ly2:
        tarp_area = rect_area(lx1, fy2, lx2, ly2)
    # or cuts top
    elif ly1 < fy1 < ly2 <= fy2:
        tarp_area = rect_area(lx1, ly1, lx2, fy1)


fout.write(str(tarp_area) + "\n")
