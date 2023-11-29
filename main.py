# início do menu (estrutura de repetição com "while True")
while True:
    print("Bem-vindo ao menu da sua sonda!")
    print("1 - Login\n2 - Minha Sonda\n3 - Perfil do paciente\n4 - Encerrar Programa")

# criação da variável "menu", com um input que permite a escolha de um dos menus acima
    menu = input("Selecione uma das opções acima por favor: ")

# define a escolha do menu "Login"
    if menu == "1":
        print("\nPara realizar o login do paciente digite as seguintes informações:")
        NomeDoMedico = input("Digite o nome do medico: ")
        CPF = input("Digite seu cpf: ")
        Senha = input("Digite sua senha: ")

        print("\n- Nome do médico: \n" + NomeDoMedico + "\n- CPF do paciente: \n" + CPF + "\n- Senha: \n" + Senha)

# define a escolha do menu "Minha Sonda"
    elif menu == "2":
        print("1 - Dieta\n2 - Dados\n3 - Informações\n4 - Encerrar Programa")

        # criação da variável "minhasonda", com um input que permite a escolha das opções acima
        minhasonda = input("Digite a opção referente a o que você quer saber sobre sua sonda: ")

        # define a escolha da opção "Dieta"
        if minhasonda == "1":
            print("\nBase líquida:\n- Água: 1000 ml\n- Fórmula enteral: 1500 ml\nNutrientes:\n- Proteínas: 80 gramas\n- Carboidratos: 150 gramas\n- Gorduras: 50 gramas\nVitaminas:\n- Vitamina A\n- Vitamina B12\n- Vitamina E\n- Vitaminas do Complexo\nFibras:\n- Fibras solúveis (Aveia em pó)\n- Fibras insolúveis (Cenouras cozidas e trituradas)\n")

        # define a escolha da opção "Dados"
        elif minhasonda == "2":
            print("\nOs dados da sonda no momento são:\n- Temperatura: 28ºC\n- Nível: 600 ml\n- Consistência: Líquida")

        # define a escolha da opção "Informações"
        elif minhasonda == "3":
            print("As informações sobre a sonda são:\n- Tipo: Gastrostomia\n- Modelo: Botton Mic-Key\n- Fabricante: Avanos\n- Data de fabricação: 23/02/21\n- Status: Em funcionamento\n")

        # define a escolha de encerrar o programa
        elif minhasonda == "4":
            print("Programa finalizado!")
            exit()

        # caso o usuário digite qualquer coisa além das opções acima ele receberá a seguinte mensagem:
        else:
            print("Opção inválida")

# define a escolha do menu "Perfil do paciente"
    elif menu == "3":
        print("- Nome: Roberto Firmino\n- Sexo: Masculino\n- Telefone: 11 96320-2402\n- Data de nascimento: 02/10/1991\n- CPF: 027.716.284-63\n- Condição clínica: Recuperação Pós-AVC\n- Nome do médico responsável: Rodrigo Faro\n")

    # define a escolha de encerrar o programa
    elif menu == "4":
        print("Programa finalizado!")
        exit()

    # caso o usuário digite qualquer coisa além das opções de menu ele receberá a seguinte mensagem:
    else:
        print("Opção inválida")