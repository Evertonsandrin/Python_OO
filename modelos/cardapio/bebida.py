from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida (ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco) # super é uma Herança, buscando atributos e métodos de outra classe
        self.tamanho = tamanho

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08) # utilize o pass para retirar o desconto