# 🏫 Processo de ETL com API de Universidades  

## Descrição

Pipeline ETL (Extract, Transform, Load) que extrai dados de universidades de diferentes países através da API [Universities Hipolabs](http://universities.hipolabs.com) e os armazena em um banco de dados SQLite.

## Estrutura do Projeto

```
├── main.py                    # Script principal
├── main-notebook.ipynb        # Notebook Jupyter com exploração e exemplos
├── requirements.txt           # Dependências do projeto
└── src/
    ├── extract.py            # Classe para extração de dados da API
    └── load.py               # Classe para carregamento em SQLite
```

## Como Excutar o Projeto

1. **Instalar dependências:**
   ```
   pip install -r requirements.txt
   ```

2. **Executar a pipeline:**
   ```
   python main.py
   ```

#

## Tecnologias Usadas

* **Linguagem**: Python 3.12
* **Bibliotecas**: Pandas, requests (Consumo de API)
* **Banco de Dados**: SQLite
* **Ambiente alternativo**: Jupyter Notebook 