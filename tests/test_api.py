import requests

BASE_URL = "http://localhost:8000"


def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200


def test_criar_categoria():
    response = requests.post(
        f"{BASE_URL}/categorias/",
        json={"nome": "Cervejas"}
    )
    assert response.status_code in [200, 201]


def test_listar_categorias():
    response = requests.get(f"{BASE_URL}/categorias/")
    assert response.status_code == 200


def test_criar_produto():
    response = requests.post(
        f"{BASE_URL}/produtos/",
        json={
            "nome": "Heineken",
            "preco": 8.5,
            "estoque": 20,
            "categoria_id": 1
        }
    )
    assert response.status_code in [200, 201]


def test_listar_produtos():
    response = requests.get(f"{BASE_URL}/produtos/")
    assert response.status_code == 200


def test_criar_venda():
    response = requests.post(
        f"{BASE_URL}/vendas/",
        json={
            "itens": [
                {
                    "produto_id": 1,
                    "quantidade": 2
                }
            ]
        }
    )
    assert response.status_code in [200, 201]