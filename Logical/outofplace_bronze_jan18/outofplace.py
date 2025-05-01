fin = open('outofplace.in', 'r')
fout = open('outofplace.out', 'w')

N = int(fin.readline())
cows = [int(fin.readline()) for _ in range(N)]

sorted_cows = sorted(cows)

# 计算错位元素个数
swaps = -1
for a in range(N):
    if cows[a] != sorted_cows[a]:
        swaps += 1

# 结果至少是 0（全对的情况）
swaps = max(0, swaps)
fout.write(str(swaps) + '\n')
fout.close()
# 如果有 K 个牛站错了位置（和排好序的数组对比）

# 那么其实有 1 头是罪魁祸首，其他的错只是它被挤错位了

# 所以我们只要把这头牛一步步冒泡到位

# 它会交换过 K−1 个牛的位置