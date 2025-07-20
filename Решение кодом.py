
# ПУНКТ А
f=open("27_A.txt")

# создаем функцию, для нахождения расстояния
def dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def fl(claster, anomal):
    # обозначаем большую длину
    dl = 10**10
    for i in range(len(claster)):
        # длина между точкой и кластером
        d = dist(anomal[0][0],anomal[0][1], claster[i][0],claster[i][1])
        #  условие, для определения наименьшей длины между точкой кластера и аномалии
        if d<dl:
            # сохраняем координаты точки
            res = claster[i]
            # сохраняем расстояние между точкой и аномалией
            dl = d
    # выводим точку
    return res

# создаем масивы, где будут храниться точки кластеров и аномалии
anomal_1 = []
claster_1, claster_2 = [],[]

# перебираем все точки в файле и распределеям их по кластерам и аномалии
for s in f:
    x,y = map(float, s.replace(",",".").split())
    if x>4:
        claster_1.append([x,y])
    elif x<2:
        claster_2.append([x,y])
    else:
        anomal_1.append([x,y])

# точки, максимально близкие с аномалией
res1 = fl(claster_1,anomal_1)
res2 = fl(claster_2,anomal_1)

# Ответ пункта А:
print(int((res1[0]+res2[0])/2*10_000),int((res1[1]+res2[1])/2*10_000))

# ПУНКТ Б:
f=open("27_B.txt")
# создаем масивы, где будут храниться точки кластеров и аномалии.
# Важно, что аномалии должны находиться в разных массивах т.к для каждой анномали своя точка в кластере.
anomal_1, anomal_2 = [],[]
claster_1, claster_2, claster_3 = [],[],[]

# перебираем все точки в файле и распределеям их по кластерам и аномалии
for s in f:
    x,y = map(float, s.replace(",",".").split())
    if x>4:
        claster_1.append([x,y])
    elif x<0 and y>4.5:
        claster_2.append([x,y])
    elif x<0 and y<4.5:
        claster_3.append([x,y])
    elif 0<x<4 and y>4.5:
        anomal_1.append([x,y])
    elif 0<x<4 and y<4.5:
        anomal_2.append([x,y])

# точки, максимально близкие с аномалиями
res1 = fl(claster_1,anomal_1)
res2 = fl(claster_2,anomal_2)
res3 = fl(claster_3,anomal_1)
res4 = fl(claster_1,anomal_2)
res5 = fl(claster_2,anomal_1)
res6 = fl(claster_3,anomal_2)

# Ответ пункт Б:
print(int((res1[0]+res2[0]+res3[0]+res4[0]+res5[0]+res6[0])/6*10_000),int((res1[1]+res2[1]+res3[1]+res4[1]+res5[1]+res6[1])/6*10_000))