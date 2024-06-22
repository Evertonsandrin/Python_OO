from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):        
        self._nome = nome.title()  # o _ torna o atributo privado
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod  # essa anotação é uma boa prática para mostrar métodos que pertencem a uma classe
    def listar_restaurantes(cls):  # o (cls) é uma complementação da boa prática do @classmethod
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
    
    @property  # o @property pertence apenas ao 'def ativo'
    def ativo(self):
        return '✔️' if self._ativo else '❌'
    
    def alternar_estado(self):  # esse não é um @classmethod, é um método o objeto restaurante
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'N/A'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property # para informar que é apenas leitura
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1): # por padrão a lista começa em 0
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)