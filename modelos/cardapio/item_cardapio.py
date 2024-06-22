from abc import ABC, abstractmethod # importando para conseguir criar um método abstrato

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod # aplicando um método abstrato | Todos as classes precisam ter esse método, mas cada uma com sua definição
    def aplicar_desconto(self):
        pass