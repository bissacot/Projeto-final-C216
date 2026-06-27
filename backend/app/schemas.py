from pydantic import BaseModel


class CategoriaBase(BaseModel):
    nome: str


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(BaseModel):
    nome: str


class CategoriaResponse(CategoriaBase):
    id: int

    class Config:
        from_attributes = True


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


class ItemVendaCreate(BaseModel):
       produto_id: int
       quantidade: int


class ItemVendaResponse(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    preco_unitario: float

    class Config:
        from_attributes = True


class VendaCreate(BaseModel):
    itens: list[ItemVendaCreate]


class VendaResponse(BaseModel):
    id: int
    valor_total: float
    itens: list[ItemVendaResponse]

    class Config:
        from_attributes = True