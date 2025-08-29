class Venda:
    def __init__(self, produto, quantidade, valor_total, cliente=None):
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = valor_total
        self.cliente = cliente