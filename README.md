# SisOSMP 

Software de Gerenciamento de Ordens de Serviço criado para a oficina Mecânica Pasetto. Critério de avaliação para a disciplina de Projeto de Software do curso de Engenharia de Computação - UEPG

# Guia para instalação

## Dependências

* [MySQL versão 8.0.30](https://downloads.mysql.com/archives/installer/)
* [Python versão 3.11.1](https://www.python.org/downloads/)
* [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) (Opcional)

## Rodando o projeto

* Abra o **MySQL command line client**, faça login e digite os comandos abaixo:

```
    create database sisosmp;
    use sisosmp;
```

* Crie o arquivo **.env** na raíz do projeto, usando como base o arquivo **example.env**, utilizando suas credenciais

* Abra um terminal na pasta do projeto e copie os comandos abaixo:

Sem o poetry:
```
    python -m venv '.venv'
    .\.venv\Scripts\activate.bat
    pip install -r requirements.txt
    .\.venv\Scripts\Python.exe main.py
```

Com o poetry:
```
    poetry install
    poetry run python main.py
```
