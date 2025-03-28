# Gerenciador de Endereços com FastAPI e API VIACEP

Um projeto simples desenvolvido com FastAPI e SQLite que permite buscar endereços através da API VIACEP, salvar esses endereços em um banco de dados, listar os endereços salvos e excluí-los.

## 📌 Funcionalidades
- **Buscar endereços** através da API VIACEP.
- **Salvar endereços** encontrados no banco de dados.
- **Listar endereços salvos**.
- **Excluir endereços** cadastrados.

## 🚀 Tecnologias Utilizadas
- Python
- FastAPI
- SQLite
- Pydantic
- Requests (para consumir a API VIACEP)

## 📂 Estrutura do Projeto
```
📁 seu_projeto/
├── main.py         # Arquivo principal para inicializar a aplicação FastAPI
├── models.py       # Definições dos modelos Pydantic
├── crud.py         # Funções para interagir com o banco de dados
├── README.md       # Documentação do projeto
```

## ⚙️ Instalação
1. Crie um ambiente virtual e ative:
```
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

2. Instale as dependências:
```
pip install fastapi uvicorn pydantic requests
```

3. Rode a aplicação:
```
uvicorn main:app --reload
```

4. Acesse no navegador:
```
http://127.0.0.1:8000
```

## 📚 Uso
- Acesse a documentação interativa do FastAPI em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📌 Rotas disponíveis
- `POST /enderecos/` - Buscar e salvar um novo endereço através do CEP
- `GET /enderecos/` - Listar todos os endereços salvos
- `DELETE /enderecos/{endereco_id}` - Excluir um endereço cadastrado


