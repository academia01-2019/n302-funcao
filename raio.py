import math

def calcular_area(raio):
	area = math.pi * math.pow(raio, 2)
	return area

def calcular_comprimento(raio):
	comp = 2 * math.pi * raio
	return comp

r = float(input("Digite um raio: "))

area = calcular_area(r)
print(f'Uma circunferência de raio {r} tem uma área de {area}.')

comp = calcular_comprimento(r)
print(f'E comprimento {comp}.')
