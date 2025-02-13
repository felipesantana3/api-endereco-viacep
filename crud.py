import sqlite3
from database import conn, cursor
from models import Endereco

def salvar_endereco(endereco: Endereco):
    cursor.execute('''
        INSERT OR IGNORE INTO CEP (cep, logradouro, complemento, bairro, cidade, uf, estado, regiao, ibge, gia, ddd, siafi)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (endereco.cep, endereco.logradouro, endereco.complemento, endereco.bairro, endereco.cidade, 
          endereco.uf, endereco.estado, endereco.regiao, endereco.ibge, endereco.gia, endereco.ddd, endereco.siafi))
    
    conn.commit()
    return {"mensagem": "Endereço salvo com sucesso!"}




def buscar_endereco(order_by: str = "cidade"):
    query = f"SELECT * FROM CEP ORDER BY {order_by}"
    cursor.execute(query)
    endereco = cursor.fetchall()

    return endereco



def deletar_endereco(cep: str):
    cursor.execute("DELETE FROM CEP WHERE cep = ?", (cep,))
    conn.commit()
    return {"mensagem": "Endereço deletado com sucesso!"}
