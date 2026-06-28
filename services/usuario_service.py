import os
import re
# pyrefly: ignore [missing-import]
from models.usuario import Usuario
# pyrefly: ignore [missing-import]
from utils.helpers import ler_json, salvar_json

CAMINHO_JSON = os.path.join("data", "usuarios.json")

def cadastrar_usuario(nome, email):
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(padrao_email, email):
        raise ValueError("E-mail com formato inválido. ")
    
    usuarios = ler_json(CAMINHO_JSON)
    if usuarios:
        novo_id = usuarios[-1]["id"] + 1
    else:
        novo_id = 1

    novo_usuario = Usuario(id=novo_id, nome=nome, email=email)
    usuario_dict = novo_usuario.to_dict()
    usuarios.append(usuario_dict)
    salvar_json(CAMINHO_JSON, usuarios)
    return usuario_dict

def listar_usuarios():
    return ler_json(CAMINHO_JSON)

def buscar_usuario_por_id(id_usuario):
    usuarios = ler_json(CAMINHO_JSON)
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            return usuario
    return None

def remover_usuario(id_usuario):
    usuarios = ler_json(CAMINHO_JSON)
    tamanho_original = len(usuarios)
    usuarios_filtrados = [u for u in usuarios if u["id"] != id_usuario]
    if len(usuarios_filtrados) < tamanho_original:
        salvar_json(CAMINHO_JSON, usuarios_filtrados)
        return True
    return False
