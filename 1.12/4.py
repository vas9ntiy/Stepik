z=input('Figure\n')
if z=='треугольник':

    a=int(input('первая сторона'))
    b = int(input('вторая сторона'))
    c = int(input('третья сторона'))
    d = (a+b+c)/2
    e = (d * (d - a) * (d - b) * (d - c)) ** 0.5
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        print(e)
    else:
        print('Такого треугольника не существует')
elif z=='прямоугольник':
    a = int(input('первая сторона'))
    b = int(input('вторая сторона'))
    c=a*b
    if a>0 and b>0:
        print(c)
    else:
        print('Такого прямоугольника не существует')
elif z=='круг':
    a = int(input('Радиус'))
    if a>0:
        print(3.14*a**2)
    else:
        print('Такого круга не существует')
else:
    print('Не знаю такой фигуры')