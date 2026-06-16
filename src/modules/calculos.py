from modules.funcJson import ler_json

def calcular_mensalidade(nome):
    alunos = ler_json()
    for aluno in alunos:
        if aluno["Nome"].upper() == nome.upper():
            total_sem_desconto = 0.0
            desconto = 0.0
            idade = int(aluno["idade"])
            cursos = aluno["Cursos"]

            for nomeCurso in cursos:
                nome_curso = nomeCurso["Curso"]
                turno = nomeCurso["Turno"]
                if nome_curso == "PHP":
                    if turno == "Manhã":
                        total_sem_desconto += 210
                    elif turno == "Noite":
                        total_sem_desconto += 260
                elif nome_curso == "Java":
                    if turno == "Manhã":
                        total_sem_desconto += 320
                    elif turno == "Noite":
                        total_sem_desconto += 390
                elif nome_curso == "Delphi":
                    if turno == "Manhã":
                        total_sem_desconto += 290
                    elif turno == "Noite":
                        total_sem_desconto += 310

            if len(cursos) > 1:
                desconto = 0.30
            elif idade > 45:
                desconto = 0.15

            valor_final = total_sem_desconto * (1 - desconto)
            return round(valor_final, 2)
    return None
