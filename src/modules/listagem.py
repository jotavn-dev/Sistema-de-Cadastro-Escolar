from modules import funcJson
from modules import calculos

alunos = funcJson.ler_json()


def Listagem_Geral():

    print("\n\n")
    print("=" * 100)
    print("Matricula", " " * 5, "Nome", " " * 30,
          "Sexo", " " * 5, "Idade", " " * 5,
          "Curso", " " * 8, "Mensalidade")
    print("=" * 100, "\n")

    for aluno in alunos:

        if aluno.get("Mensalidade") is None:
            aluno["Mensalidade"] = calculos.calcular_mensalidade(aluno["Nome"])

        cursos = aluno["Cursos"]

        if len(cursos) > 1:
            cursos = f"{cursos[0]['Curso']} e {cursos[1]['Curso']}"
        else:
            cursos = cursos[0]["Curso"]

        print(
            f"{aluno['Matricula']:<16}"
            f"{aluno['Nome']:<35}"
            f"{aluno['Sexo']:<13}"
            f"{aluno['idade']:<12}"
            f"{cursos:<15}"
            f"R$ {aluno['Mensalidade']}"
        )

    print("\n\nTecle Enter para voltar ao Menu\n")

    while True:
        tecla = input()

        if tecla == "":
            return
        elif tecla != "":
            continue


def Listagem_Por_Curso():

    print("Qual curso deseja listar? (PHP/JAVA/DELPHI)\n")

    while True:
        curso = str(input()).upper()

        if curso != "PHP" and curso != "JAVA" and curso != "DELPHI":
            print("Inválido")
            continue
        else:
            break

    print("\n\n")
    print("=" * 100)
    print("Matricula", " " * 5, "Nome", " " * 30,
          "Sexo", " " * 5, "Idade", " " * 5,
          "Curso", " " * 8, "Mensalidade")
    print("=" * 100, "\n")

    for aluno in alunos:

        if aluno.get("Mensalidade") is None:
            aluno["Mensalidade"] = calculos.calcular_mensalidade(aluno["Nome"])

        cursos = aluno["Cursos"]
        nomes_cursos = [c["Curso"].upper() for c in cursos]

        if curso in nomes_cursos:

            if len(cursos) > 1:
                cursos = f"{cursos[0]['Curso']} e {cursos[1]['Curso']}"
            else:
                cursos = cursos[0]["Curso"]

            print(
                f"{aluno['Matricula']:<16}"
                f"{aluno['Nome']:<35}"
                f"{aluno['Sexo']:<13}"
                f"{aluno['idade']:<12}"
                f"{cursos:<15}"
                f"R$ {aluno['Mensalidade']}"
            )

    print("\n\nTecle Enter para voltar ao Menu\n")

    while True:
        tecla = input()

        if tecla == "":
            return
        elif tecla != "":
            continue


def Listagem_Por_Sexo():

    print("Qual sexo deseja listar? (Masculino/Feminino)\n")

    while True:
        sexo = str(input()).upper()

        if sexo != "MASCULINO" and sexo != "FEMININO":
            print("Inválido")
            continue
        else:
            break

    print("-" * 100)
    print("Tela de Listagem por sexo")
    print("-" * 100)

    print("\n\n")
    print("=" * 100)
    print("Matricula", " " * 5, "Nome", " " * 30,
          "Sexo", " " * 5, "Idade", " " * 5,
          "Curso", " " * 8, "Mensalidade")
    print("=" * 100, "\n")

    for aluno in alunos:

        if aluno.get("Mensalidade") is None:
            aluno["Mensalidade"] = calculos.calcular_mensalidade(aluno["Nome"])

        if aluno["Sexo"].upper() == sexo:

            cursos = aluno["Cursos"]

            if len(cursos) > 1:
                cursos = f"{cursos[0]['Curso']} e {cursos[1]['Curso']}"
            else:
                cursos = cursos[0]["Curso"]

            print(
                f"{aluno['Matricula']:<16}"
                f"{aluno['Nome']:<35}"
                f"{aluno['Sexo']:<13}"
                f"{aluno['idade']:<12}"
                f"{cursos:<15}"
                f"R$ {aluno['Mensalidade']}"
            )

    print("\n\nTecle Enter para voltar ao Menu\n")

    while True:
        tecla = input()

        if tecla == "":
            return
        elif tecla != "":
            continue
