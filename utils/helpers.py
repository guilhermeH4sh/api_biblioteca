import json 

def ler_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError,
    json.JSONDecodeError):
        return []

def salvar_json(caminho_arquivo, dados):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        return True
    except Exception:
        return False