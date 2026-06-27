class Emprestimo:
    def __init__(self, id, id_usuario, id_livro, data_emprestimo, data_devolucao=None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_livro = id_livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def to_dict(self):
        return{
        "id": self.id,
        "id_usuario": self.id_usuario,
        "id_livro": self.id_livro,
        "data_emprestimo": self.data_emprestimo,
        "data_devolucao": self.data_devolucao
        }
    
    @classmethod
    def from_dict(cls, dados_dict):
        return cls(
            id=dados_dict["id"],
            id_usuario=dados_dict["id_usuario"],
            id_livro=dados_dict["id_livro"],
            data_emprestimo=dados_dict["data_emprestimo"],
            data_devolucao=dados_dict["data_devolucao"]
        )