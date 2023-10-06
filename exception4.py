def fahrenheit_to_celsius(f):
    return (5/9) * ((f - 32))


#teste
while True:
    try: 
        fahrenheit_temp = float(input('temperatura (f): '))
        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
        print("A temperatura em Celsius é de {:.1f}ºC".format(celsius_temp))
        break
    except ValueError as e:
        print(f'entrada inválida! {e}')
        