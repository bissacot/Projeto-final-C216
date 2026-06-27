from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.post("/", response_model=schemas.ProdutoResponse)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    categoria = crud.buscar_categoria(db, produto.categoria_id)

    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    return crud.criar_produto(db, produto)


@router.get("/", response_model=list[schemas.ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return crud.listar_produtos(db)


@router.get("/{produto_id}", response_model=schemas.ProdutoResponse)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = crud.buscar_produto(db, produto_id)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto


@router.put("/{produto_id}", response_model=schemas.ProdutoResponse)
def atualizar_produto(
    produto_id: int,
    dados: schemas.ProdutoUpdate,
    db: Session = Depends(get_db)
):
    categoria = crud.buscar_categoria(db, dados.categoria_id)

    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    produto = crud.atualizar_produto(db, produto_id, dados)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto


@router.delete("/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = crud.deletar_produto(db, produto_id)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return {"mensagem": "Produto deletado com sucesso"}