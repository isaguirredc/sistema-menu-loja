from cliente import Cliente
from produto import Produto
from venda import Venda

class Sistema:
    def __init__(self):
        self.produtos_estoque = []
        self.clientes_cadastrados = []
        self.fila_vendas = []
        self.pilha_operacoes = []
        self.proximo_id_produto = 1
        self.proximo_id_cliente = 1
        self.valor_total_vendas = 0.0
    
    def cadastrar_cliente(self, nome):
        cliente = Cliente(self.proximo_id_cliente, nome)
        self.clientes_cadastrados.append(cliente)
        self.pilha_operacoes.append(('cadastro_cliente', cliente))
        self.proximo_id_cliente += 1
        print(f"Cliente {cliente.id} cadastrado com sucesso!")
    
    def listar_clientes(self):
        if not self.clientes_cadastrados:
            print("Nenhum cliente cadastrado no sistema.")
            return
        for cliente in self.clientes_cadastrados:
            print(f"ID: {cliente.id} | Nome: {cliente.nome} | Gasto Total: R${cliente.gasto_total:.2f}")
    
    def encontrar_cliente_por_id(self, id):
        for cliente in self.clientes_cadastrados:
            if cliente.id == id:
                return cliente
        return None

    def cadastrar_produto(self, nome, quantidade, preco):
        produto = Produto(self.proximo_id_produto, nome, quantidade, preco)
        self.produtos_estoque.append(produto)
        self.pilha_operacoes.append(('cadastro_produto', produto))
        self.proximo_id_produto += 1
        print(f"Produto {produto.id} cadastrado com sucesso!")
    
    def listar_produtos_estoque(self):
        if not self.produtos_estoque:
            print("O estoque está vazio.")
            return
        for produto in self.produtos_estoque:
            print(f"ID: {produto.id} | Nome: {produto.nome} | Quantidade: {produto.quantidade} | Preço: R${produto.preco:.2f}")
    
    def encontrar_produto_por_id(self, id):
        for produto in self.produtos_estoque:
            if produto.id == id:
                return produto
        return None
    
    def pesquisar_produto(self, termo):
        resultados = []
        if termo.isdigit():
            id_busca = int(termo)
            for produto in self.produtos_estoque:
                if produto.id == id_busca:
                    resultados.append(produto)
        for produto in self.produtos_estoque:
            if termo.lower() in produto.nome.lower():
                if produto not in resultados:
                    resultados.append(produto)
        
        if not resultados:
            print("Nenhum produto foi encontrado.")
            return
        
        for produto in resultados:
            print(f"ID: {produto.id} | Nome: {produto.nome} | Quantidade: {produto.quantidade} | Preço: R${produto.preco:.2f}")
    
    def realizar_venda(self, id_produto, quantidade, id_cliente=None):
        produto = self.encontrar_produto_por_id(id_produto)
        if not produto:
            print("Nenhum produto foi encontrado.")
            return False
        
        if produto.quantidade < quantidade:
            print(f"Quantidade em estoque de {produto} insuficiente para essa venda.")
            print(f"{produto} em estoque: {produto.quantidade}")
            return False
        
        valor_total = produto.preco * quantidade
        produto.quantidade -= quantidade
        
        cliente = None
        if id_cliente:
            cliente = self.encontrar_cliente_por_id(id_cliente)
            if cliente:
                cliente.gasto_total += valor_total
        
        venda = Venda(produto, quantidade, valor_total, cliente)
        self.fila_vendas.append(venda)
        self.pilha_operacoes.append(('venda', venda))
        self.valor_total_vendas += valor_total
        
        if cliente:
            print(f"Venda realizada para o cliente {cliente.nome}: R${valor_total:.2f}")
        else:
            print(f"Venda realizada: R${valor_total:.2f}")
        
        return True
    
    def ver_fila_vendas(self):
        if not self.fila_vendas:
            print("Nenhuma venda realizada ainda.")
            return
        for venda in self.fila_vendas:
            if venda.cliente:
                print(f"Cliente: {venda.cliente.nome} | Produto: {venda.produto.nome} | Quantidade: {venda.quantidade} | Total: R${venda.valor_total:.2f}")
            else:
                print(f"Produto: {venda.produto.nome} | Quantidade: {venda.quantidade} | Total: R${venda.valor_total:.2f}")
    
    def desfazer_ultima_operacao(self):
        if not self.pilha_operacoes:
            print("Nenhuma operação para desfazer.")
            return
        
        ultima_operacao = self.pilha_operacoes.pop()
        tipo_operacao, dados_operacao = ultima_operacao
        
        if tipo_operacao == 'cadastro_produto':
            self.produtos_estoque.remove(dados_operacao)
            print(f"Cadastro do produto {dados_operacao.nome} desfeito com sucesso.")
        
        elif tipo_operacao == 'cadastro_cliente':
            self.clientes_cadastrados.remove(dados_operacao)
            print(f"Cadastro do cliente {dados_operacao.nome} desfeito com sucesso.")
        
        elif tipo_operacao == 'venda':
            dados_operacao.produto.quantidade += dados_operacao.quantidade
            if dados_operacao in self.fila_vendas:
                self.fila_vendas.remove(dados_operacao)
            self.valor_total_vendas -= dados_operacao.valor_total
            if dados_operacao.cliente:
                dados_operacao.cliente.gasto_total -= dados_operacao.valor_total
            print(f"Venda do produto {dados_operacao.produto.nome} desfeita com sucesso.")
    
    def exibir_valor_total_estoque(self):
        valor_total = 0
        for produto in self.produtos_estoque:
            valor_total += produto.quantidade * produto.preco
        print(f"Valor total do estoque: R${valor_total:.2f}")
    
    def exibir_valor_total_vendas_realizadas(self):
        print(f"Valor total de vendas realizadas: R${self.valor_total_vendas:.2f}")
    
    def exibir_clientes_valores_gastos(self):
        if not self.clientes_cadastrados:
            print("Nenhum cliente cadastrado no sistema.")
            return
        
        print("Gastos totais dos clientes:")
        for cliente in self.clientes_cadastrados:
            print(f"ID: {cliente.id} | Nome: {cliente.nome} | Gasto Total: R${cliente.gasto_total:.2f}")

# EXTRA TXT SAVE/LOAD:
    def salvar_dados_arquivo(self, nome_arquivo="dados_estoque.txt"):
        try:
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write("Produtos:\n")
                for produto in self.produtos_estoque:
                    arquivo.write(f"{produto.id},{produto.nome},{produto.quantidade},{produto.preco}\n")
            print(f"Dados salvos com sucesso em {nome_arquivo}.")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")
    
    def carregar_dados_arquivo(self, nome_arquivo="dados_estoque.txt"):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                secao = None
                for linha in linhas:
                    linha = linha.strip()
                    if linha == "Produtos:":
                        secao = "produtos"
                    elif secao == "produtos" and linha:
                        partes = linha.split(',')
                        if len(partes) == 4:  
                            id, nome, quantidade, preco = partes
                            produto = Produto(int(id), nome, int(quantidade), float(preco))
                            self.produtos_estoque.append(produto)
                            self.proximo_id_produto = max(self.proximo_id_produto, int(id) + 1)
                        else:
                            print(f"Linha ignorada (formato inválido): {linha}")
            print(f"Dados carregados com sucesso de {nome_arquivo}.")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
