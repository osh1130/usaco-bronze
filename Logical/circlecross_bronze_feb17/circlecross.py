fin = open('circlecross.in', 'r')
fout = open('circlecross.out', 'w')

s = fin.readline().strip()

# 记录每个字母的位置
pos = {}
for i in range(len(s)):
    if s[i] not in pos:
        pos[s[i]] = [i]
    else:
        pos[s[i]].append(i)

count = 0

#枚举所有不同字母对
for a in range(26):
    for b in range(a + 1, 26):
        A = chr(ord('A') + a)
        B = chr(ord('A') + b)
        a1, a2 = pos[A]
        b1, b2 = pos[B]

        # 统计 B 在 A 区间中出现了几次
        b_inside = 0
        for b_pos in [b1, b2]:
            if a1 < b_pos < a2:
                b_inside += 1

        if b_inside == 1:
            count += 1

# 325=25*25



fout.write(str(count) + '\n')
fin.close()
fout.close()
