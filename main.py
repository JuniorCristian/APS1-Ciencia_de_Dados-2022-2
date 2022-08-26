# Alunos
# Cristian Robert Belão de Meira Junior
# Douglas Cristiano Morona
# Felipe Rodrigues da Silva
# Fernando Macedo Kramar
# Pedro Henrique Brunning de Oliveira Schier

import json
import numpy as np
import pandas as pd


def getBolos():
    file = open('bolos.json', 'r')
    bolos = json.load(file)
    file.close()
    return bolos


def teste():
    bolos = getBolos()
    qtds = dict()
    ingredients_per_bolo = np.zeros(len(bolos))
    i = 0
    for bolo in bolos:
        ingredients_per_bolo[i] = len(bolo['ingredients'])
        for ingredient in bolo['ingredients']:
            if not (ingredient['name'] in qtds):
                qtds[ingredient['name']] = {'amount': 0, 'unit': 0, 'quantity_used': 0}
            qtds[ingredient['name']]['amount'] = float(qtds[ingredient['name']]['amount']) + ingredient['amount']
            qtds[ingredient['name']]['unit'] = ingredient['unit']
            qtds[ingredient['name']]['quantity_used'] += 1
        i += 1

    mean_ingredients_per_bolo = np.mean(ingredients_per_bolo)
    std_ingredients_per_bolo = np.std(ingredients_per_bolo)
    sorted_itens = sorted(qtds.items(), key=lambda x: x[1]['amount'], reverse=True)

    print('Média: {}'.format(mean_ingredients_per_bolo))
    print('Desvio padrão: {}'.format(std_ingredients_per_bolo))
    for key, value in sorted_itens:
        print(key, value['amount'], value['unit'], 'Usado em ' + str(value['quantity_used']) + ' bolo(s)')
        print('------------')


opx_mais_pedidos = 1
opx_bolos_mais_pedidos = 2
opx_media_std_bolos = 2
opx_sair = 1

opx = 0
print("Bem vindo ao Bolo-Mania!\n")
print("Aqui você pode encontrar os bolos gostosos de todos os tempos.\n")
bolos = getBolos()
pedidos = pd.read_csv("pedidos.csv")
while opx != opx_sair:
    print("Para começar, escolha uma opção abaixo:\n")
    print(str(opx_mais_pedidos) + " - Ver número de bolos pedidos")
    print(str(opx_bolos_mais_pedidos) + " - Ver Bolos mais pedidos")
    print(str(opx_mais_pedidos) + " - Ver média e desvio padrão dos bolos")
    print(str(opx_sair) + " - Sair")
    opx = int(input())
    if opx == opx_mais_pedidos:
        print("\nQuantidade de Bolos pedidos:\n")
        total = 0
        for bolo in bolos:
            qtd = np.sum(pedidos.where(pedidos['bolo'] == bolo['name']).dropna()['quantidade'])
            total += int(qtd)
            print(bolo['name'] + ': ' + str(int(qtd)))
            print('------------')
        print('Total: ' + str(total))
    elif opx == opx_bolos_mais_pedidos:
        print("\nBolos mais pedidos:\n")

    elif opx == opx_mais_pedidos:
        print("\nMédia e desvio padrão dos bolos:\n")

    elif opx == opx_sair:
        print("\nSaindo...")
    else:
        print("\nOpção inválida, tente novamente.")
        opx = 0
        continue
    opx = int(input())
