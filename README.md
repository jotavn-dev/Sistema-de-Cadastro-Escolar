# 🎓 TI Cursos - Sistema de Cadastro Escolar

Este é um sistema de gerenciamento de alunos desenvolvido em *Python* como projeto acadêmico do 1º período de faculdade. O software funciona via linha de comando (CLI) e simula o controle de matrículas, cursos, turnos e mensalidades de uma instituição de ensino.

---

## 🚀 Funcionalidades

O sistema conta com um fluxo completo de gerenciamento de dados (CRUD) e geração de relatórios:

* *Cadastrar Aluno:* Registro de nome, matrícula (única), sexo, idade, múltiplos cursos (PHP, Java, Delphi) e turnos (Manhã/Noite) com validação de dados.
* *Editar Aluno:* Permite alterar de forma modular qualquer campo de um aluno já cadastrado.
* *Remover Aluno:* Exclusão de registros do sistema pelo nome.
* *Listagem Geral:* Exibe todos os alunos cadastrados em um formato de tabela limpo e organizado.
* *Listagem por Curso:* Filtra e exibe alunos matriculados em uma tecnologia específica.
* *Listagem por Sexo:* Filtra os registros com base no gênero informado.
* *Regras de Negócio (Mensalidades):* Cálculo automático do valor com base no curso e turno escolhidos, aplicando descontos cumulativos (30% para mais de um curso ou 15% para alunos acima de 45 anos).

---

## 📦 Estrutura do Projeto

O projeto foi modularizado para garantir uma melhor legibilidade e manutenção do código:

* main.py: O ponto de entrada do programa.
* telainicial.py: Renderiza o menu principal interativo na tela.
* cadastro.py: Contém a lógica das funções de inserção, edição e remoção de dados (cadastrar_usuario, editar, remover).
* calculos.py: Centraliza as regras de negócio de preços dos cursos, turnos e cálculo de descontos.
* listagem.py: Responsável por gerar as tabelas e filtros de visualização dos dados na tela.
* funcJson.py: Módulo utilitário encarregado da persistência de dados (leitura e escrita do arquivo alunos.json).

---

## 🛠️ Tecnologias Utilizadas

* *Linguagem:* Python 3.14
* *Persistência de Dados:* JSON (JavaScript Object Notation)
* *Biblioteca Nativa:* json

---

## 💻 Como Executar o Projeto

1. Certifique-se de ter o Python instalado na sua máquina.
2. Certifique-se de ter o arquivo alunos.json na mesma pasta (ou o sistema irá ler uma lista vazia caso o arquivo seja iniciado corretamente).
3. Abra o terminal na pasta do projeto e execute:

python main.py

## 👥 Equipe e Divisão de Tarefas

O projeto foi desenvolvido em colaboração, onde cada integrante ficou responsável por módulos específicos do sistema:

* **[Thiago Souza](https://github.com/THsouza07)** — Responsável pelo desenvolvimento do módulo de cadastro (cadastrar_usuario) e remoção de alunos (remover) no arquivo cadastro.py.
* **[João Vitor](https://github.com/jotavn-dev)** — Responsável por toda a lógica de edição modular de dados (editar) no arquivo cadastro.py e pela persistência de dados e manipulação do arquivo JSON (funcJson.py).
* **[Kauan Manoel](https://github.com/kauaManoel)** — Responsável pelo módulo de cálculos de mensalidades e regras de descontos (calculos.py).
* **[Igor Cruz](https://github.com/iguu0)** — Responsável pela criação das telas de listagem e filtros de dados (listagem.py).
* **[Guilherme Cézar](https://github.com/guilhermecesar07)** — Responsável pela interface do menu (telainicial.py) e integração do fluxo principal (main.py).
