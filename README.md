# Microserviço de Relatórios - Espaços Publicitários

Este microserviço fornece relatórios analíticos dos espaços publicitários cadastrados, organizados por status, loja e marca. Ele é executado de forma **independente** em um container Docker isolado, com seu próprio banco de dados.

## ✅ Funcionalidades

- Relatório de status dos espaços (`ocupado` / `disponível`)
- Quantidade de espaços por loja
- Quantidade de espaços por marca
- Retorno agrupado com todos os relatórios
- Documentação interativa com Swagger UI

## 🔧 Tecnologias Utilizadas

- Python 3.10
- Flask
- SQLAlchemy
- SQLite
- Swagger UI

## 🚀 Como Executar

### 1. Baixe os arquivos do projeto

Baixe todos os arquivos do microserviço e salve-os em um diretório local chamado `espacos-publicitarios-relatorios`.

### 2. Acesse o diretório no terminal

```bash
cd espacos-publicitarios-relatorios
```

### 3. Build da imagem Docker

```bash
docker build -t relatorios .
```

### 4. Execute o container na porta 5000

```bash
docker run -p 5000:5000 relatorios
```

A aplicação estará disponível em:

- [http://localhost:5000/relatorios/status](http://localhost:5000/relatorios/status)
- [http://localhost:5000/relatorios/lojas](http://localhost:5000/relatorios/lojas)
- [http://localhost:5000/relatorios/marcas](http://localhost:5000/relatorios/marcas)
- [http://localhost:5000/relatorios/geral](http://localhost:5000/relatorios/geral)
- [http://localhost:5000/swagger](http://localhost:5000/swagger) – documentação interativa

## 🗂️ Estrutura de Diretórios

```
espacos-publicitarios-relatorios/
├── app.py                # Arquivo principal com as rotas da API
├── models.py             # Modelo de dados e função de popular o banco
├── requirements.txt      # Lista de dependências
├── Dockerfile            # Instruções de build da imagem Docker
└── static/
    └── swagger.json      # Arquivo Swagger para documentação da API
```

## ℹ️ Observações

- O banco `relatorios.db` é criado automaticamente na pasta `/app/instance` dentro do container.
- Este microserviço é executado separadamente da API principal e não compartilha o banco com ela.
- Ideal para análises e visualizações independentes ou integráveis com dashboards externos.

---

Desenvolvido para fins acadêmicos na disciplina **Arquitetura e Projeto de Software - Pós PUCRIO**.
