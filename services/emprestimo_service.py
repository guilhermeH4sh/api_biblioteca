import os
import datetime
# pyrefly: ignore [missing-import]
from models.emprestimo import Emprestimo
# pyrefly: ignore [missing-import]
from utils.helpers import ler_json, salvar_json
# pyrefly: ignore [missing-import]
import services.usuario_service as usuario_service
# pyrefly: ignore [missing-import]
import services.livro_service as livro_service

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_JSON = os.path.join(BASE_DIR, "data", "emprestimos.json")

def realizar_emprestimo(id_usuario, id_livro):
    # -- Valida se o usuário existe
    usuario = usuario_service.buscar_usuario_por_id(id_usuario)
    if not usuario:
        raise ValueError("Usuário inválido ou não encontrado.")
    
    # -- Valida se o livro existe e está disponível
    livro = livro_service.buscar_livro_por_id(id_livro)
    if not livro:
        raise ValueError("Livro não encontrado.")
    if not livro.get("disponivel", True):
        raise ValueError("Livro indisponível para empréstimo.")
        
    # -- Caso passe nas validações, gera um novo ID sequencial de empréstimo.
    emprestimos = ler_json(CAMINHO_JSON)
    if emprestimos:
        novo_id = emprestimos[-1]["id"] + 1
    else:
        novo_id = 1
        
    # -- Salva a data atual em formato texto
    data_atual = datetime.date.today().strftime('%d/%m/%Y')
    
    # -- Atualiza a disponibilidade do livro para False
    livro_service.atualizar_disponibilidade(id_livro, False)
    
    # -- Salva o novo registro de empréstimo no JSON de empréstimos
    novo_emprestimo = Emprestimo(
        id=novo_id,
        id_usuario=id_usuario,
        id_livro=id_livro,
        data_emprestimo=data_atual,
        data_devolucao=None
    )
    emprestimo_dict = novo_emprestimo.to_dict()
    emprestimos.append(emprestimo_dict)
    salvar_json(CAMINHO_JSON, emprestimos)
    
    return emprestimo_dict

def devolver_livro(id_emprestimo):
    emprestimos = ler_json(CAMINHO_JSON)
    emprestimo_encontrado = None
    
    for emp in emprestimos:
        if emp["id"] == id_emprestimo and emp["data_devolucao"] is None:
            emprestimo_encontrado = emp
            break
            
    if not emprestimo_encontrado:
        raise ValueError("Empréstimo ativo não encontrado.")
        
    # -- Define a data de devolução atual
    data_atual = datetime.date.today().strftime('%d/%m/%Y')
    emprestimo_encontrado["data_devolucao"] = data_atual
    
    # -- Altera a disponibilidade do livro de volta para True
    livro_service.atualizar_disponibilidade(emprestimo_encontrado["id_livro"], True)
    
    # -- Salva as alterações
    salvar_json(CAMINHO_JSON, emprestimos)
    return True

def listar_emprestimos_ativos():
    emprestimos = ler_json(CAMINHO_JSON)
    return [emp for emp in emprestimos if emp["data_devolucao"] is None]
