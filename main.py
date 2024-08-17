#!usr/bin/ambetec python
# -*- coding: utf-8 -*-

"""
Docstring:
Programa que calcula o consumo de combustivel
de um veículo.
Python: 3.10.x ou superior
"""
VALOR_COMBUSTIVEL = float(4.89)

def receberValorFloat(x):
    while(True):
        try:
            receber_float = float(input(f'Informe o valor de {x}: '))#%f.2
            return receber_float
            break
        except:
            print('Erro ao informar o valor!')
            continue

consumo_veiculo = receberValorFloat('consumo do veículo')
print(f'O consumo do veiculo foi {consumo_veiculo}')

tempo_viagem = receberValorFloat('tempo de viagem')
print(f'O tempo de viagem foi {tempo_viagem}')

velocidade_media = receberValorFloat('velocidade média')
print(f'A velocidade média foi {velocidade_media}')

DISTANCIA = (tempo_viagem / 60 ) * velocidade_media #dividir por 60 , tempo em min

print(f'A distância percorrida é {DISTANCIA}')

