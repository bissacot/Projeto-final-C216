from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/vendas", tags=["Vendas"])


@router.post("/", response_model=schemas.VendaResponse)
def criar_venda(venda: schemas.VendaCreate, db: Session = Depends(get_db)):
    try:
        return crud.criar_venda(db, venda)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))


@router.get("/", response_model=list[schemas.VendaResponse])
def listar_vendas(db: Session = Depends(get_db)):
    return crud.listar_vendas(db)


@router.get("/{venda_id}", response_model=schemas.VendaResponse)
def buscar_venda(venda_id: int, db: Session = Depends(get_db)):
    venda = crud.buscar_venda(db, venda_id)

    if not venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada")

    return venda


@router.delete("/{venda_id}")
def deletar_venda(venda_id: int, db: Session = Depends(get_db)):
    venda = crud.deletar_venda(db, venda_id)

    if not venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada")

    return {"mensagem": "Venda deletada com sucesso"}