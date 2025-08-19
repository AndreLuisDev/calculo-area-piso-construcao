def realizar_orcamento():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    largura = float(input("Digite a largura: "))
    comprimento = float(input("Digite o comprimento: "))
    area = largura * comprimento

    if area > 500:
        desconto = area * 0.20
    elif area > 100:
        desconto = area * 0.10
    else:
        desconto = 0.0

    return {
        "Orçamento da Área para colocação do piso"
        "1 - Nome do Cliente: ": nome,
        "2 - CPF: ": cpf,
        "3 - Comprimento: ": comprimento,". Largura: ": largura,
        "4 - Área de Piso necessária: ": area,
        "5 - Desconto aplicado na compra:": desconto
}

orcamento = None

while True:
    print("\n1 - Realizar orçamento.")
    print("2 - Visualizar orçamento")
    print("3 - Realizar novo orçamento")
    print("4 - Encerrar programa")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        orcamento = realizar_orcamento()
        orcamento
        print("Orcamento realizado com sucesso!")
    elif opcao == "2":
        if orcamento:
            print("\n -- ORÇAMENTO")
            for chave, valor in orcamento.items():
                print(f"{chave.capitalize()}: {valor}")
        else:
                print("Nenhum orçamento realizado ainda. Faça uma cotação.")
    elif opcao == "3":
        orcamento = realizar_orcamento()
        print("Novo orçamento relizado com sucesso!")
    elif opcao == "4":
        print("Encerrando programa ...")
        break
    else:
        print("Opção Inválida.")