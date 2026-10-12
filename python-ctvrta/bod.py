# kontrola bodu ve grafu

x1 = 4
y1 = 2
x2 = 9
y2 = 7

xb = int(input("Zadejte x bodu: "))
yb = int(input("Zadejte y bodu: "))

if xb > x1 and xb < x2 and yb > y1 and yb < y2:
    print("Uvnitř")
elif xb >= x1 and xb <= x2 and yb >= y1 and yb <= y2:
    print("Na hranici")
else:
    print("Mimo")
