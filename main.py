from sistema import Sistema

def main():
    sistema = Sistema()
    
    while True:
        try:
            print("""
  __  __ ___ _  _ _   _   ___   _     _    ___     _  _   
 |  \/  | __| \| | | | | |   \ /_\   | |  / _ \ _ | |/_\  
 | |\/| | _|| .` | |_| | | |) / _ \  | |_| (_) | || / _ \ 
 |_|  |_|___|_|\_|\___/  |___/_/ \_\ |____\___/ \__/_/ \_\                                                       
""")
            print("---------------------------- CLIENTES")
            print("1. Cadastrar cliente")
            print("2. Clientes cadastrados")
            print("---------------------------- PRODUTOS")
            print("3. Cadastrar produto")
            print("4. Produtos em estoque")
            print("5. Pesquisar produto")
            print("---------------------------- VENDAS")
            print("6. Realizar venda")
            print("7. Vendas realizadas")
            print("---------------------------- DESFAZER")
            print("8. Desfazer ação")
            print("---------------------------- CAIXA")
            print("9. Valor total do estoque")
            print("10. Valor total de vendas")
            print("11. Gastos dos clientes")
            print("---------------------------- ARQUIVO")
            print("12. Salvar dados do estoque")
            print("13. Carregar dados do estoque")
            print("========================================")
            print("14. Sair")
            print("ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ")
            
            opcao = input("Opção: ").strip()
            
            if opcao == "1":
                nome_cliente = input("Nome do cliente: ")
                if nome_cliente:
                    sistema.cadastrar_cliente(nome_cliente)
                else:
                    print("Nome do cliente inválido. Tente novamente.")
            
            elif opcao == "2":
                sistema.listar_clientes()
            
            elif opcao == "3":
                nome_produto = input("Nome do produto: ")
                if nome_produto:
                    try:
                        quantidade_produto = int(input("Quantidade: "))
                        preco_produto = float(input("Preço: R$ "))
                        if quantidade_produto >= 0 and preco_produto >= 0:
                            sistema.cadastrar_produto(nome_produto, quantidade_produto, preco_produto)
                        else:
                            print("Valores devem ser positivos. Tente novamente.")
                    except:
                        print("Valores numéricos devem ser válidos. Tente novamente.")
                else:
                    print("Nome do produto inválido. Tente novamente.")
            
            elif opcao == "4":
                sistema.listar_produtos_estoque()
            
            elif opcao == "5":
                termo_pesquisa = input("Digite o nome ou ID do produto: ")
                if termo_pesquisa:
                    sistema.pesquisar_produto(termo_pesquisa)
                else:
                    print("Produto inválido. Tente novamente.")
            
            elif opcao == "6":
                try:
                    tem_cliente = input("A venda é para um cliente cadastrado? (s/n): ").lower()
                    id_cliente = None
                    if tem_cliente == 's':
                        id_cliente = int(input("ID do cliente: "))
                    
                    id_produto = int(input("ID do produto: "))
                    quantidade_venda = int(input("Quantidade: "))
                    
                    if quantidade_venda > 0:
                        sistema.realizar_venda(id_produto, quantidade_venda, id_cliente)
                    else:
                        print("Quantidade deve ser maior que zero.")
                except:
                    print("Valores numéricos devem ser válidos.")
            
            elif opcao == "7":
                sistema.ver_fila_vendas()
            
            elif opcao == "8":
                sistema.desfazer_ultima_operacao()
            
            elif opcao == "9":
                sistema.exibir_valor_total_estoque()
            
            elif opcao == "10":
                sistema.exibir_valor_total_vendas_realizadas()
            
            elif opcao == "11":
                sistema.exibir_clientes_valores_gastos()
            
            elif opcao == "12":
                nome_arquivo = input("Nome do arquivo (ou pressione ENTER nome padrão): ").strip()
                if not nome_arquivo:
                    sistema.salvar_dados_arquivo()
                else:
                    sistema.salvar_dados_arquivo(nome_arquivo)
            
            elif opcao == "13":
                nome_arquivo = input("Nome do arquivo (pressione ENTER para nome padrão): ").strip()
                if not nome_arquivo:
                    sistema.carregar_dados_arquivo()
                else:
                    sistema.carregar_dados_arquivo(nome_arquivo)
            
            elif opcao == "14":
                print("Saindo do sistema...")
                break
            
            else:
                print("Opção inválida. Por favor, escolha uma opção do menu.")
        
        except Exception as erro:
            print(f"Erro inesperado: {erro}")
            print("Continuando operação...")

if __name__ == "__main__":
    main()