def dividir(numerador, denominador1, denominador2):
    resultado = 0
    try:
        resultado = numerador / denominador1
    except ZeroDivisionError as e:
        try:
            resultado = numerador / denominador2
        except ZeroDivisionError as e:
            print(f'erro: {e}')
        else:
            print('operação realizada com sucesso!')
    else:
        print('operação realizada com sucesso!')
    return resultado

#teste
print({dividir(5,0,0)})
print({dividir(5,0,1)})
print({dividir(5,1,0)})
