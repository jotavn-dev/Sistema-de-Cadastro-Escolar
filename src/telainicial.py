def tela_inicial():
    while True:
        print("==================================")
        print("           TI CURSOS")
        print("==================================")
        print("1 - Cadastrar Aluno")
        print("2 - Editar Aluno")
        print("3 - Remover Aluno")
        print("4 - Listagem Geral")
        print("5 - Listagem por Curso")
        print("6 - Listagem por Sexo")
        print("0 - Sair")
        print("==================================")


        opcao = input("digite a opçâo desejada: ")
        if opcao == "1":
            print(" --> Cadastro de aluno ")
            from cadastro import cadastrar_usuario
            cadastrar_usuario()
        elif opcao == "2":
            print(" --> Editar aluno ")
            from cadastro import editar
            editar()
        elif opcao == "3":
            print(" --> Remover aluno ")
            from cadastro import remover
            remover()
        elif opcao == "4":
           print(" --> Listagem geral ")
           from listagem import Listagem_Geral
           Listagem_Geral()
        elif opcao == "5":
            print(" --> Listagem por curso ")
            from listagem import Listagem_Por_Curso
            Listagem_Por_Curso()
        elif opcao == "6":
            print(" --> Listagem por sexo ")
            from listagem import Listagem_Por_Sexo
            Listagem_Por_Sexo()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")
            continue