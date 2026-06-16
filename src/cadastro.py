# Thiago

import funcJson

def cadastrar_usuario():
    dados_brutos = funcJson.ler_json()
    lista_usuarios = dados_brutos if isinstance(dados_brutos, list) else []

    novo_aluno = {}

    while True:
        novo_aluno["Nome"] = input("\nNome: ").title()
        if novo_aluno["Nome"].replace(" ", "").isalpha():
            break

        else:
            print("Números ou símbolos não são aceitos.")
            continue

    while True:
        matricula_digitada = input("\nMatrícula: ")
        if not matricula_digitada.isdigit():
            print("Não aceitamos letras ou símbolos.")
            continue

        existe = False

        for usuario in lista_usuarios:
            if usuario["Matricula"] == matricula_digitada:
                existe = True
                break

        if existe:
            print(f"ERRO: A matrícula {matricula_digitada} já pertence a outro aluno.")
        else:
            novo_aluno["Matricula"] = matricula_digitada
            break

    print("\nSexo: 1-feminino / 2-masculino")
    while True:
        opcao_sexo = input("\nEscolha: ")
        if opcao_sexo == "1":
            novo_aluno["Sexo"] = "Feminino"
            break
        elif opcao_sexo == "2":
            novo_aluno["Sexo"] = "Masculino"
            break
        else:
            print("ERRO. Opção inválida.")

    while True:
       idade_digitada = input("\nIdade: ")

       if not idade_digitada.isdigit():
        print("Não aceitamos letras")
       else:
        if int(idade_digitada) < 100:
            novo_aluno["idade"] = idade_digitada
            break
        else:
            print("Idade inválida!")
            continue

    continuar = True
    novo_aluno["Cursos"] = []

    while True:
        # if coninuar:
            print("\nCursos: 1-PHP / 2-Java / 3-Delphi")
            opcao_curso = input("\nEscolha: ")

            if opcao_curso == "1":
                nome_curso = "PHP"
            elif opcao_curso == "2":
                nome_curso = "Java"
            elif opcao_curso == "3":
                nome_curso = "Delphi"
            else:
                print("ERRO. Opção inválida.")
                continue

            print("\nTurno: 1-Manhã / 2-Noite")
            opcao_turno = input("\nEscolha: ")

            if opcao_turno == "1":
                turno = "Manhã"

            elif opcao_turno == "2":
                turno = "Noite"
                
            else:
                print("ERRO. Opção inválida.")
                # print(novo_aluno["Cursos"]["Turno"])
            continuar = False
            for cada_aluno in novo_aluno["Cursos"]:
                if turno in cada_aluno["Turno"]:
                    print(f"Você já adicionou o turno da {turno}.")
                    print("Escolha outro turno.")
                    continuar = True

            if continuar:
                continue        
                
            novo_aluno["Cursos"].append({
                "Curso": nome_curso,
                "Turno": turno
            })
            
            mais_cursos = input("\nDeseja adicionar mais cursos? (S/N) ").upper().strip()[0]

            if mais_cursos not in ["S", "N"]:
                print("ERRO. Opção inválida.")
                continue
            elif mais_cursos == "S":
                continuar = True
                continue
            else:
                break

    lista_usuarios.append(novo_aluno)
    funcJson.salvar_json(lista_usuarios)
    print("\nUsuário cadastrado com sucesso!")

    continuar = input("\nDeseja cadastrar um novo usuário? (S/N): ").upper().strip()[0]
    if continuar == "S":
        cadastrar_usuario()

# João vitor

def editar():
    alunos = funcJson.ler_json()
    while True:
        print()
        print("\n".join([f"Nome: {nome['Nome']}" for nome in alunos]))

        for usuario in alunos:
            nome_busca = input("\nDigite o nome do usuário que deseja editar: ")

            if usuario["Nome"].upper() == nome_busca.upper():
                print(f"\nEditando dados de: {usuario['Nome']}")
            else:
                print("Nome do aluno não existe.")
                continue

            while True:
                menu = ["Nome", "Matricula", "Sexo:", "Idade", "Curso", "Turno:"]
                print(f"\n{", ".join(menu[:3])}")
                print(f"{", ".join(menu[3:])}")

                selecionar_opcao = input("\nInforme o que você quer editar: ").upper().strip()
                if selecionar_opcao == "NOME":
                    print(f"{usuario["Nome"]}")
                    while True:
                        usuario["Nome"] = input("\nNovo Nome: ")
                        if usuario["Nome"].replace(" ", "").isalpha():
                            break
                        else:
                            print("Só funciona letras.")
                            continue

                elif selecionar_opcao in ["MATRICULA", "MATRÍCULA"]:
                    print(f"\n{usuario["Nome"]} - {usuario["Matricula"]}")
                    while True:
                        usuario["Matricula"] = input("\nNova Matrícula: ")
                        if usuario["Matricula"].isdigit():
                            break
                        else:
                            print("Só aceita números.")
                            continue

                elif selecionar_opcao == "SEXO":
                    print(f"\n{usuario["Nome"]} - {usuario["Sexo"]}")
                    while True:
                        print("\nNovo Sexo: 1-fem / 2-mas")
                        opcao_sexo = input("\nEscolha: ")

                        if opcao_sexo == "1":
                            usuario["Sexo"] = "Feminino"
                            break

                        elif opcao_sexo == "2":
                            usuario["Sexo"] = "Masculino"
                            break

                        else:
                            print("ERRO. Não existe essa opção.")
                            continue

                elif selecionar_opcao == "IDADE":
                    print(f"\n{usuario["Nome"]} - Idade: {usuario["idade"]}", end=" ")

                    while True:
                        usuario["Idade"] = input("\nNova idade: ")
                        if usuario["Idade"].isdigit():
                            if int(usuario["Idade"]) < 100:
                                break
                            else:
                                print("Erro. idade inexistente")
                                continue
                        else:
                            print("Só aceita letras.")
                            continue

                elif selecionar_opcao in ["CURSO", "CURSOS"]:
                    while True:
                        print(f"\nNome: {usuario["Nome"]} - Curso:", end=" ")

                        nomes_curso = [cada_curso["Curso"] for cada_curso in usuario["Cursos"]]
                        print(" e ".join(nomes_curso))
                        
                        if len(usuario["Cursos"]) > 1:
                            print(f"\nVocê quer alterar o curso {usuario["Cursos"][0]["Curso"]} ou {usuario["Cursos"][1]["Curso"]}?")
                            selecionar_curso = input(f"\nEscolha (1 - {usuario["Cursos"][0]["Curso"]} e 2 - {usuario["Cursos"][1]["Curso"]}): ")
                        
                        else:
                            print(f"\nVocê está fazendo apenas o curso de {usuario["Cursos"][0]["Curso"]}: ")
                            selecionar_curso = input(f"\nEscolha (1 - {usuario["Cursos"][0]["Curso"]}): ")

                        print("\nQual curso você quer escolher:")

                        if selecionar_curso == "1":
                            if "Java" in usuario["Cursos"][0]["Curso"]:
                                print("\n1 - PHP\n3 - Delphi")
                        
                            elif "PHP" in usuario["Cursos"][0]["Curso"]:
                                print("\n2 - Java\n3 - Delphi")
                            
                            else:
                                print("\n1 - PHP\n2 - Java")

                            opcao_curso = input("\nEscolha: ").upper().strip()

                            if opcao_curso == "1":
                                usuario["Cursos"][0]["Curso"] = "PHP"
                                break

                            elif opcao_curso == "2":
                                usuario["Cursos"][0]["Curso"] = "Java"
                                break

                            elif opcao_curso == "3":
                                usuario["Cursos"][0]["Curso"] = "Delphi"
                                break

                            else:
                                print("ERRO. Essa opção não existe.")
                                continue

                        elif selecionar_curso == "2":

                            if "Java" in usuario["Cursos"][1]["Curso"]:
                                print("\n1 - PHP\n3 - Delphi")
                        
                            elif "PHP" in usuario["Cursos"][1]["Curso"]:
                                print("\n2 - Java\n3 - Delphi")
                            
                            else:
                                print("\n1 - PHP\n2 - Java")

                            opcao_curso = input("\nEscolha: ")

                            if opcao_curso == "1":
                                usuario["Cursos"][1]["Curso"] = "PHP"
                                break

                            elif opcao_curso == "2":
                                usuario["Cursos"][1]["Curso"] = "Java"
                                break

                            elif opcao_curso == "3":
                                usuario["Cursos"][1]["Curso"] = "Delphi"
                                break

                            else:
                                print("ERRO. Essa opção não existe.")
                                continue

                        else:
                            print("Não existe esse curso dentro do seu usuario.")
                            continue

                elif selecionar_opcao == "TURNO":
                    while True:
                        print()
                        for cada_curso in usuario["Cursos"]:
                            print(f"{cada_curso["Curso"]} - {cada_curso["Turno"]}")

                        print(f"\nVocê quer alterar o turno da {usuario["Cursos"][0]["Turno"]} ou da {usuario["Cursos"][1]["Turno"]}?")
                        selecionar_turno = input(f"\nEscolha (1 - {usuario["Cursos"][0]["Turno"]} e 2 - {usuario["Cursos"][1]["Turno"]}): ")

                        if selecionar_turno == "1":
                            if "Noite" in usuario["Cursos"][0]["Turno"]:
                                print("\nSó temos disponível o turno da manhã:")
                                print("\nDigite 1 - Manhã")

                                opcao_turno = input("\nEscolha: ")

                                if opcao_turno == "1":
                                    usuario["Cursos"][0]["Turno"] = "Manhã"
                                    break

                                else:
                                    print("Não existe essa opção.")
                                    continue
                        
                            elif "Manhã" in usuario["Cursos"][0]["Turno"]:
                                print("\nSó temos disponível o turno da noite:")
                                print("\nDigite 1 - Noite")

                            opcao_turno = input("\nEscolha: ")

                            if opcao_turno == "1":
                                usuario["Cursos"][0]["Turno"] = "Noite"
                                break
                            
                            else:
                                print("Não existe essa opção.")
                                continue

                        elif selecionar_turno == "2":
                            if "Noite" in usuario["Cursos"][1]["Turno"]:
                                print("\nSó temos disponível o turno da manhã:")
                                print("\nDigite 1 - Manhã")

                                opcao_turno = input("\nEscolha: ")

                                if opcao_turno == "1":
                                    usuario["Cursos"][1]["Turno"] = "Manhã"
                                    break

                                else:
                                    print("Não existe essa opção.")
                                    continue
                        
                            elif "Manhã" in usuario["Cursos"][1]["Turno"]:
                                print("\nSó temos disponível o turno da noite:")
                                print("\nDigite 1 - Noite")

                            opcao_turno = input("\nEscolha: ")

                            if opcao_turno == "1":
                                usuario["Cursos"][1]["Turno"] = "Noite"
                                break
                            
                            else:
                                print("\nNão existe essa opção.")
                                print("\nMais uma vez")
                                continue
                        
                        else:
                            print("\nNão existe essa opção.")
                            print("\nMais uma vez")
                            continue

                elif selecionar_opcao.isdigit():
                    print("\nNão coloque símbolos ou números")
                    print("Informe apenas os nomes da opção.")
                    continue

                else:
                    print("ERRO. Não existe essa opção.")
                    continue

                print("\nAlterações realizadas com sucesso!")
                funcJson.salvar_json(alunos)
                while True:
                    resposta = input("Quer alterar mais alguma coisa: (sim/não): ").upper().strip()[0]
                    if resposta == "S":
                        break

                    elif resposta == "N":
                        return

                    else:
                        print("\nErro. opção errada.")
                        print("Apenas confirme com (sim/não)\n")
                        continue

# Thiago

def remover():
    alunos = funcJson.ler_json()
    remove_usuario = input("\nDigite o nome do usuário que será removido: ")
    for usuario in alunos:
        if usuario["Nome"] == remove_usuario:
            alunos.remove(usuario)
            funcJson.salvar_json(alunos)
