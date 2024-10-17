#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Docstring:
Programa que calcula o consumo de combustível
de um veículo.
Python: 3.10.x ou superior
"""

VALOR_COMBUSTIVEL = 4.89  # Preço do combustível por litro

def receber_valor_float(x):
    """Recebe um valor float do usuário com tratamento de erros."""
    while True:
        try:
            valor_float = float(input(f'Informe o valor de {x}: '))
            return valor_float
        except ValueError:
            print('Erro ao informar o valor! Tente novamente.')

# Recebe os dados do usuário
consumo_veiculo = receber_valor_float('consumo do veículo (km/l)')
print(f'O consumo do veículo foi {consumo_veiculo} km/l')

tempo_viagem = receber_valor_float('tempo de viagem (min)')
print(f'O tempo de viagem foi {tempo_viagem} minutos')

velocidade_media = receber_valor_float('velocidade média (km/h)')
print(f'A velocidade média foi {velocidade_media} km/h')

# Calcula a distância percorrida
distancia = (tempo_viagem / 60) * velocidade_media  # converter minutos para horas
print(f'A distância percorrida é {distancia:.2f} km')

# Calcula o consumo de combustível
litros_consumidos = distancia / consumo_veiculo
custo_combustivel = litros_consumidos * VALOR_COMBUSTIVEL

print(f'Litros consumidos: {litros_consumidos:.2f} L')
print(f'Custo do combustível: R$ {custo_combustivel:.2f}')


