import json
from time import sleep
def linhas():
    print('-' * 50)
def menu():
    sleep(1)
    linhas()
    print('Teste Técnico: Estágio Target Sistemas')
    print('Menu:')
    print('Teste (1): Variável Soma')
    print('Teste (2): Sequência de Fibonacci')
    print('Teste (3): Faturamento Mensal')
    print('Teste (4): Representação percentual estado')
    print('Teste (5): Invertendo caracteres')
    print('Sair (6)')
    linhas()

def opcao1():
    print('Teste 1: Variável Soma')
    indice = 13
    soma = 0
    k = 0
    while k < indice:
        k = k + 1
        soma = soma + k
    print(f'O valor da variável "SOMA" é: {soma}.')


def opcao2():
    print('Teste 2: Sequência de Fibonacci')
    verfib = int(input('Qual número deseja verificar se faz parte da sequência de Fibonacci? '))
    num1 = 0
    num2 = 1
    numfib = num1 + num2
    fibseq = [num1, num2, numfib]
    
    while verfib > numfib:
        num1 = num2
        num2 = numfib
        numfib = num1 + num2
        fibseq.append(numfib)
    print(fibseq)
    if verfib in fibseq:
        print(f'O número {verfib} está na sequência de Fibonacci!')
    else:
        print(f'O número {verfib} não está na sequência de Fibonacci!')


def opcao3():
    print('Teste 3: Faturamento Mensal')
    with open('dados.json') as jsonf:
        dados = json.load(jsonf)
    valores = [i['valor'] for i in dados if  i['valor'] != 0]
    minfat = min(valores)
    maxfat = max(valores)
    mediafat = sum(valores) / len(valores)
    supmedia = 0
    for i in valores:
        if i > mediafat:
            supmedia += 1
    print(f'O menor valor de faturamento ocorrido em um dia do mês foi R$ {minfat}.')
    print(f'O maior valor de faturamento ocorrido em um dia do mês foi R$ {maxfat}.')
    print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {supmedia}')
    
    
def opcao4():
    print('Teste 4: Percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.')
    dic = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'OU': 19849.53}
    totfat = sum(dic.values())
    ptotfat = {estado: (valor / totfat) * 100 for estado, valor in dic.items()}
    for estado, porcentagem in ptotfat.items():
        print(f"{estado}: {porcentagem:.2f}%")


def opcao5():
    print('Teste 5: Invertendo caracteres')
    texto = str(input('Qual texto você gostaria de inverter? '))
    textoinvert = texto[::-1]
    print(f'O texto invertido é: {textoinvert}')

def sair():
    print('Saindo... Obrigado pela oportunidade!')

while True:
    menu()
    esc = input('Escolha um teste (1-6): ')

    if esc == '1':
        opcao1()
    elif esc == '2':
        opcao2()
    elif esc == '3':
        opcao3()
    elif esc == '4':
        opcao4()
    elif esc == '5':
        opcao5()
    elif esc == "6":
        sair()
        break
    else:
        print("Escolha inválida, tente novamente.")
    
