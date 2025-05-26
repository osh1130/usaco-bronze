fin = open("balancing.in","r")
fout = open("balancing.out","w")
n, b = map(int, fin.readline().split())
cows = [tuple(map(int, fin.readline().split())) for _ in range(n)]

x_options = set()
y_options = set()

# Generate all possible fence positions (x + 1), since cows' x/y are odd, x + 1 is even
for x, y in cows:
    x_options.add(x + 1)
    y_options.add(y + 1)

min_max_region = n  # max possible is n

for a in x_options:
    for b in y_options:
        q1 = q2 = q3 = q4 = 0
        for x, y in cows:
            if x > a and y > b:
                q1 += 1
            elif x < a and y > b:
                q2 += 1
            elif x < a and y < b:
                q3 += 1
            elif x > a and y < b:
                q4 += 1
        max_region = max(q1, q2, q3, q4)
        min_max_region = min(min_max_region, max_region)

fout.write(str(min_max_region))
# print(min_max_region)
