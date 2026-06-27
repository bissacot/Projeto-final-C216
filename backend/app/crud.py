from sqlalchemy.orm import Session

from app import models, schemas


# ---------- CATEGORIAS ----------

def criar_categoria(db: Session, categoria: schemas.CategoriaCreate):
    nova_categoria = models.Categoria(nome=categoria.nome)

    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)

    return nova_categoria


def listar_categorias(db: Session):
    return db.query(models.Categoria).all()


def buscar_categoria(db: Session, categoria_id: int):
    return db.query(models.Categoria).filter(
        models.Categoria.id == categoria_id
    ).first()


def atualizar_categoria(db: Session, categoria_id: int, dados: schemas.CategoriaUpdate):
    categoria = buscar_categoria(db, categoria_id)

    if categoria:
        categoria.nome = dados.nome
        db.commit()
        db.refresh(categoria)

    return categoria


def deletar_categoria(db: Session, categoria_id: int):
    categoria = buscar_categoria(db, categoria_id)

    if categoria:
        db.delete(categoria)
        db.commit()

    return categoria


# ---------- PRODUTOS ----------

def criar_produto(db: Session, produto: schemas.ProdutoCreate):
    novo_produto = models.Produto(
        nome=produto.nome,
        preco=produto.preco,
        estoque=produto.estoque,
        categoria_id=produto.categoria_id,
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto


def listar_produtos(db: Session):
    return db.query(models.Produto).all()


def buscar_produto(db: Session, produto_id: int):
    return db.query(models.Produto).filter(
        models.Produto.id == produto_id
    ).first()


def atualizar_produto(db: Session, produto_id: int, dados: schemas.ProdutoUpdate):
    produto = buscar_produto(db, produto_id)

    if produto:
        produto.nome = dados.nome
        produto.preco = dados.preco
        produto.estoque = dados.estoque
        produto.categoria_id = dados.categoria_id

        db.commit()
        db.refresh(produto)

    return produto


def deletar_produto(db: Session, produto_id: int):
    produto = buscar_produto(db, produto_id)

    if produto:
        db.delete(produto)
        db.commit()

    return produto


# ---------- VENDAS ----------

def criar_venda(db: Session, venda: schemas.VendaCreate):
    nova_venda = models.Venda(valor_total=0)

    db.add(nova_venda)
    db.commit()
    db.refresh(nova_venda)

    valor_total = 0

    for item in venda.itens:
        produto = buscar_produto(db, item.produto_id)

        if not produto:
            raise ValueError(f"Produto {item.produto_id} não encontrado")

        if produto.estoque < item.quantidade:
            raise ValueError(f"Estoque insuficiente para {produto.nome}")

        produto.estoque -= item.quantidade

        item_venda = models.ItemVenda(
            venda_id=nova_venda.id,
            produto_id=produto.id,
            quantidade=item.quantidade,
            preco_unitario=produto.preco,
        )

        valor_total += produto.preco * item.quantidade

        db.add(item_venda)

    nova_venda.valor_total = valor_total

    db.commit()
    db.refresh(nova_venda)

    return nova_venda


def listar_vendas(db: Session):
    return db.query(models.Venda).all()


def buscar_venda(db: Session, venda_id: int):
    return db.query(models.Venda).filter(
        models.Venda.id == venda_id
    ).first()


def deletar_venda(db: Session, venda_id: int):
    venda = buscar_venda(db, venda_id)

    if venda:
        db.delete(venda)
        db.commit()

    return venda