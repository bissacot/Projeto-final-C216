from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.post("/", response_model=schemas.CategoriaResponse)
def criar_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.criar_categoria(db, categoria)


@router.get("/", response_model=list[schemas.CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.listar_categorias(db)


@router.get("/{categoria_id}", response_model=schemas.CategoriaResponse)
def buscar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.buscar_categoria(db, categoria_id)

    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    return categoria


@router.put("/{categoria_id}", response_model=schemas.CategoriaResponse)
def atualizar_categoria(
    categoria_id: int,
    dados: schemas.CategoriaUpdate,
    db: Session = Depends(get_db)
):
    categoria = crud.atualizar_categoria(db, categoria_id, dados)

    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    return categoria


@router.delete("/{categoria_id}")
def deletar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.deletar_categoria(db, categoria_id)

    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    return {"mensagem": "Categoria deletada com sucesso"}