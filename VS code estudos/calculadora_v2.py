
saida = ''

# Funções básicas (adição, substração, etc)
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return 'Não foi possível realizar a divisão por 0'
    return x / y

# Calculadora
def calculadora(n1, n2, operacao):
    
    # pra funcionar minuscula
    operacao = operacao.lower()  

    if operacao in ['+', 'soma', 'adicao']:
        resultado = adicao(num1, num2)     # tentei fazer com N1, N2, mas tava dando erro aí botei Num1 e foi
    elif operacao in ['-', 'subtracao', 'subtração']:
        resultado = subtracao(num1, num2)
    elif operacao in ['*', 'x', 'multiplicacao', 'multiplicação']:
        resultado = multiplicacao(num1, num2)
    elif operacao in ['/', 'divisao', 'divisão']:
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida. Tente novamente.'

    return resultado

# Laço
while saida.lower() != 'n':
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        operacao = input('Digite a operação (+, -, *, / ou nome): ')
        
        resultado = calculadora(num1, num2, operacao)  # aqui eu tava precisando de "# type: ignore", mas tava incomodando ele avisando algo sobre numeros invalidos
        print('Resultado da operação:', resultado)

        saida = input('Deseja continuar? (S/N): ')
    except ValueError:  
        print('Entrada inválida. Por favor, digite apenas números válidos.')   # essa mensagem aqui hahahah
        continue