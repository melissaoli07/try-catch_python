def dividir(x,y):
    try:
        print (f'{x} / {y} é {x/y}')
    except ZeroDivisionError as e:
        print(f'divisão por zero {e}')


def principal():
    dividir(10,2)
    dividir(10,5)
    dividir(10,0)
    dividir(6,3)
    dividir(10,0)

principal()