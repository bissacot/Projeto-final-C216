def criar_produto(db: Session, produto: schemas.ProdutoCreate):
    novo_produto = models.Produto(
        nome=produto.nome,
        preco=produto.preco,
        estoque=produto.estoque,
        categoria_id=produto.categoria_id
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto


def listar_produtos(db: Session):
    return db.query(models.Produto).all()


def buscar_produto(db: Session, produto_id: int):
    return db.query(models.Produto).filter(models.Produto.id == produto_id).first()


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