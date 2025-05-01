fin = open('circlecross.in', 'r')
fout = open('circlecross.out', 'w')

s = fin.readline().strip()
first_pos = {}
count = 0

for i in range(len(s)):
    c = s[i]
    if c not in first_pos:
        first_pos[c] = i
    else:
        start = first_pos[c]
        end = i
        # 记录这个区间中，哪些字母只出现一次 → 交叉
        seen = set()
        for j in range(start + 1, end):
            if s[j] not in seen:
                seen.add(s[j])
            else:
                seen.remove(s[j])
        # set 中剩下的字母是只出现一次的，即和 c 构成交叉
        count += len(seen)

fout.write(str(count//2) + '\n')
fin.close()
fout.close()

#遍历 52 个字符 ,52*52
