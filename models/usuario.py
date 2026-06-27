class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email
    
    def to_dict(self):
        return{
        "id": self.id,
        "nome": self.nome,
        "email": self.email
        }

    @classmethod
    def from_dict(cls, dados_dict):
        return cls(
            id=dados_dict["id"],
            nome=dados_dict["nome"],
            email=dados_dict["email"]
        )
        