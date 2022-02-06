# Contador de palavras

Essa aplicação foi feita com objetivo de receber uma string e calcular quantas palavras existem, desconsiderando espaços extras e caracteres especiais.

## Tecnologias e Pré-requisitos

As seguintes ferramentas foram usadas na construção do projeto:
- Python
- Django

### Dependencia

Deve existir o Python, na versão 3, instalado.
Instalar o modulo Django

```shell
pip install django
```

## Rodando a aplicação

1. Clone o repositório
2. Acesse a pasta do projeto
3. Dentro da pasta que possui o arquivo manage.py digite no terminal:

```shell
python3 manage.py runserver
```

4. Acesse https://http://localhost:8000/

## Exemplos de texto

Uma tonelada de bananas custa 1.516 reais. (7 palavras)
Fui ao mercado com 50 reais e comprei pouca coisa (10 palavras)
Lista de compras: Maçã, queijo e leite (7 palavras)

### Critérios de contagem de palavras

- Sequências de letras
- Sequência de números, podendo conter ponto e vírgula entre eles.
- Não foi tratado a limpeza do texto. Exemplo: ("Eu estava pensando ...")

### Autoria

Larissa Hey