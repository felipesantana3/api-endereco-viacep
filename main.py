
from fastapi import FastAPI, Query
import requests
from models import Endereco
from crud import salvar_endereco, buscar_endereco, deletar_endereco

app = FastAPI()


@app.post("/Adicionar/{cep}")
def consulta_cep(cep: str):
    cep = cep.replace("-", "")
    
    
    if len(cep) != 8 or not cep.isdigit():
        return {"erro": "CEP inválido"}


    endereco_salvo = buscar_endereco(cep)
    if endereco_salvo:
        return {"mensagem": "CEP encontrado no banco de dados", "dados": endereco_salvo}


    url = f"http://www.viacep.com.br/ws/{cep}/json"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            return {"erro": "CEP não encontrado"}

        endereco = Endereco(
            cep=cep,
            logradouro=dados.get("logradouro", ""),
            complemento=dados.get("complemento", ""),
            bairro=dados.get("bairro", ""),
            cidade=dados.get("localidade", ""),
            uf=dados.get("uf", ""),
            estado=dados.get("uf", ""),  
            regiao="",
            ibge=dados.get("ibge", ""),
            gia=dados.get("gia", ""),
            ddd=dados.get("ddd", ""),
            siafi=dados.get("siafi", "")
        )


        salvar_endereco(endereco)

        return {"mensagem": "Endereço salvo no banco de dados", "dados": endereco.dict()}

    return {"erro": "Erro ao acessar a API"}


@app.get("/buscar/")
def buscar_no_banco(order_by: str = Query("cidade", enum=["cidade", "bairro", "estado"])):
    endereco = buscar_endereco( order_by)
    if endereco:
        return {"mensagem": "Endereços encontrados!", "dados": endereco}
    return {"erro": "Endereço não encontrado no banco de dados"}


@app.delete("/deletar/{cep}")
def deletar_no_banco(cep: str):
    return deletar_endereco(cep)

    


