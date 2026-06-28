import os
# pyrefly: ignore [missing-import]
from models.livro import Livro
# pyrefly: ignore [missing-import]
from utils.helpers import ler_json, salvar_json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_JSON = os.path.join(BASE_DIR, "data", "livros.json")

def cadastrar_livro(titulo, autor, ano):
    livros = ler_json(CAMINHO_JSON)
    if livros:
        novo_id = livros[-1]["id"] + 1 
    else:
        novo_id = 1

    novo_livro = Livro(id=novo_id, titulo=titulo, autor=autor, ano=ano)
    livro_dict = novo_livro.to_dict()
    livros.append(livro_dict)
    salvar_json(CAMINHO_JSON, livros)
    return livro_dict

def listar_livros():
    return ler_json(CAMINHO_JSON)

def buscar_livro_por_id(id_livro):
    livros = ler_json(CAMINHO_JSON)
    for livro in livros:
            if livro["id"] == id_livro:
                return livro
    return None

def remover_livro(id_livro):
    livros = ler_json(CAMINHO_JSON)
    tamanho_original = len(livros)
    livros_filtrados = [livro for livro in livros if livro["id"] != id_livro]

    if len(livros_filtrados) < tamanho_original:
        salvar_json(CAMINHO_JSON, livros_filtrados)
        return True
    return False

def atualizar_disponibilidade(id_livro, disponivel):
    livros = ler_json(CAMINHO_JSON)
    encontrado = False
    for livro in livros:
        if livro["id"] == id_livro:
            livro["disponivel"] = disponivel

        encontrado = True
        break

    if encontrado:
        salvar_json(CAMINHO_JSON, livros)
        return True
    return False