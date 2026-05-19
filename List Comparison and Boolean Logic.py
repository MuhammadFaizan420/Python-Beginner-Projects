numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

minx = numbers_x[0]
maxx = numbers_x[-1]

miny = numbers_y[0]
maxy = numbers_y[-1]

if minx == maxx:
    print(f"{numbers_x} | result is True")
else:
     print(f"{numbers_x} |result is False")

if miny == maxy:
    print(f"{numbers_y} | result is True")
else:
     print(f"{numbers_y} | result is False")