x1 = 0
y1 = 0
x2 = 100
y2 = 0

dx = x2 - x1
dy = y2 - y1

steps = 0;



steps = max(abs(dx),abs(dy))

xincr = dx/steps
yincr = dy/steps

for i in range(1,steps+1):
    print(f"({x1},{y1}) , ")
    x1 = x1 + xincr
    y1 = y1 + yincr

