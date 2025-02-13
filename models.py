from pydantic import BaseModel

class Endereco(BaseModel):
    cep: str
    logradouro: str
    complemento: str
    bairro: str
    cidade: str
    uf: str
    estado: str
    regiao: str
    ibge: str
    gia: str
    ddd: str
    siafi: str
