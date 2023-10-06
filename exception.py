try:
    #div = 10/0
    n1 = int(input('número 1: '))
    n2 = int(input('número 2: '))
    result = n1/n2
    print(f'resultado: {result}')
    numero = int(input('número: '))
    print(numero)
except ValueError as e:
    print(f' entrada inválida | {e}')
except ZeroDivisionError as e:
    print(f' divisão por zero | {e}')
finally:
    print('Tchau, obrigado! Até amanhã!')