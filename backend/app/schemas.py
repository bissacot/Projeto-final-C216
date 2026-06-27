class ProdutoBase(BaseModel):
    nome: str
    preco: float
    estoque: int
    categoria_id: int


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoUpdate(BaseModel):
    nome: str
    preco: float
    estoque: int
    categoria_id: int


class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        from_attributes = True