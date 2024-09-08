# data-quality-fw


### SETTINGS FOR HIGH QUALITY PROJECTS AND TDD

Summary
1. Git: start a git and github repo
2. Pyenv: define python version based on oldest version required by a library that will be needed e.g:
```pyenv local 3.11.9```
3. Poetry: to manage depedencies
```poetry init```
4. Mkdocs+Mermaid: Run the following command and fix the yaml file:
```
poetry add mkdocs
mkdocs new . 
poetry run mkdocs serve # start localhost server
poetry add 'mkdocs-mermaid2-plugin'
poetry add 'mkdocs-material'
poetry add mkdocstrings[crystal,python]

########### fixing yaml file ##########
theme:
  name: material

plugins:
  - search
  - mermaid2
  - mkdocstrings
```
5. Taskipy: sets alias to commands
```
poetry add taskipy

########## fixing pyproject.toml file ######### 
[tool.taskipy.tasks]
format = """
isort . 
black .
"""
kill = "kill -9 $(lsof -t -i :8000)"
test = "pytest -v"
run = """ python3 app/main.py """
doc = "mkdocs serve"
```
Install isort and black for formatting
```
poetry add isort
poetry add black
```

Example how to to run taskipy setup:
``` 
poetry run task format
poetry run task test
```
6. Install Pytest
7. CI/CD: Create github/worflows directory and place CI.yml in the workflows folder with the following content:
```
name: ci

on: push
jobs:
    build-and-test:
        runs-on: ubuntu-latest
        steps:
            - name: Baixar o repositório
              uses: actions/checkout@v4

            - name: Instalar o Python
              uses: actions/setup-python@v5
              with:
                python-version: 3.12.1

            - name: Instalar o Poetry via pip
              run: pip install poetry

            - name: Instalar dependências com o Poetry
              run: poetry install

            - name: Rodar minha rotina de testes com o Poetry
              run: poetry run pytest tests -v
```
Following, write a test like in `test_funcao_hello_world`. The test will fail because there is no such module yet.