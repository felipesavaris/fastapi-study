# Setup do projeto e explicações

Nesta página monstraremos quais bibliotecas usadas e configurações efetuadas para dar clareza do que foi feito e por que.

## Instalações de dependências 

Este projeto usa o Poetry como gerenciador de dependências.

- fastapi[standard]
- ruff (linter e formatador de código)
- pytest (framework/lib para testes)
    - pesquisar (isort, blue, black, flake8)
- taskipy (semelhante ao Makefile - decidi usar o Makefile por enquanto)

## Possíveis perguntas

### Diferença entre instalar fastapi e fastapi[standard]

A diferença está nas dependências extras instaladas:

fastapi - Instala apenas o core do FastAPI. Você precisa instalar manualmente outras dependências como:

```
uvicorn (servidor ASGI)
pydantic-settings (para configurações)
python-multipart (para upload de arquivos)
```

E outras bibliotecas conforme necessário
fastapi[standard] - Instala o FastAPI + dependências recomendadas para uso padrão, incluindo:

```
uvicorn[standard] com extras (servidor ASGI otimizado)
pydantic-settings
pydantic-email-validator
python-multipart
jinja2 (para templates)
httpx (cliente HTTP)
Entre outras
```

Em resumo: fastapi[standard] é mais conveniente para começar, enquanto fastapi sozinho te dá mais controle sobre quais dependências instalar, deixando a aplicação mais leve se você não precisar de todas as funcionalidades.

### O que pode-se analisar com Ruff

![Códigos que o Ruff pode analisar](/images/ruff-codigos.png)