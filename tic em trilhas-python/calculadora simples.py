# Gabriela Poock :)

def calculadora():
    while True:
        print('CALCULADORA SIMPLES')
        print()
        print('1. Soma')
        print('2. Subtração')
        print('3. Multiplicação')
        print('4. Divisão')
        print('s. Sair')
        operação = input('Selecione uma opção ou "s" para sair: ')

        if operação == "s" or operação == "S":
            print('Obrigada por utilizar a Calculadora Simples!')
            break

        if operação not in ['1', '2', '3', '4']:
            print('Ops, opção inválida! :( Tente novamente.')
            continue

        numero_1 = float(input('Primeiro número: '))
        numero_2 = float(input('Segundo número: '))

        if operação == '1':
            resultado = numero_1 + numero_2
            print('O resultado da soma destes números é: ', resultado)
        elif operação == '2':
            resultado = numero_1 - numero_2
            print('O resultado da subtração destes números é: ', resultado)
        elif operação == '3':
            resultado = numero_1 * numero_2
            print('O resultado da multiplicação destes números é: ', resultado)
        else:
            if numero_2 == 0:
                print('Divisões por zero não são possíveis. Tente novamente :)')
                continue
            else:
                resultado = numero_1 / numero_2
                print('O resultado da divisão destes números é: ', resultado)

calculadora()
