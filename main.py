import json
import numpy as np

file = open('bolos.json', 'r')
bolos = json.load(file)
file.close()
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

print("Bem vindo ao Bolo-Mania!\n")
print("Aqui você pode encontrar os bolos mais pedidos e os mais pedidos de cada ingrediente.\n")

print('Média: {}'.format(mean_ingredients_per_bolo))
print('Desvio padrão: {}'.format(std_ingredients_per_bolo))
for key, value in sorted_itens:
    print(key, value['amount'], value['unit'], 'Usado em ' + str(value['quantity_used']) + ' bolo(s)')
    print('------------')
