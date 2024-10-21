#coding: utf-8
valores = list(range(1,11))
anos = list(range(2020,2060,10))
print(valores)
valores.extend(anos)
print(valores)
lista_concatenada = valores+anos
print(lista_concatenada)

mercado = [’ouro’, "bitcoin", ’titulos’ ]
mercado.sort()