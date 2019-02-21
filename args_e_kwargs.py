# -*- coding: utf-8 -*-
#
# def retornar_itens_estoque(setor, *args):
#       print(f'Lista salva no estoque do setor: {setor}:')
#       for item in args:
#          print(item)
#
# retornar_itens_estoque('Administrativo', 'Documentos de A a Z', 'Livros de caíxa', 'Computadores')
#

def lista_de_compras(pessoa, **kwargs):
    fruta = kwargs.get('fruta')
    if fruta is not None:
        print(f'Na lista de compras do {pessoa} há uma fruta: {fruta}')

lista_de_compras('Jureg', fruta='Abacate', massas='Macarrão', verdura='Couve')

lista_de_compras('Irmão do Jorel', fruta='atemoia', bebida='Catuaba', sorvete='Limão')
