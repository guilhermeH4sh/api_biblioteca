class Livro:
    def __init__(self, id, titulo, autor, ano, disponivel=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "disponivel": self.disponivel
        }
    @classmethod
    def from_dict(cls, dados_dict):
        return cls(
            id=dados_dict["id"],
            titulo=dados_dict["titulo"],
            autor=dados_dict["autor"],
            ano=dados_dict["ano"],
            disponivel=dados_dict["disponivel"]
            )