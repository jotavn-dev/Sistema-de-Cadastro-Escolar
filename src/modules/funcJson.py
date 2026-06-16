import json

def ler_json():
    with open("src/database/alunos.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_json(lista_alunos):
    with open("src/database/alunos.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista_alunos, arquivo, indent=5, ensure_ascii=False)