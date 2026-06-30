import pytest
from app import app

@pytest.fixture
def client():
    """Configura o cliente de testes do Flask sem rodar o servidor real."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# TESTE 1 (Obrigatório): Retorno HTTP 200 para a rota GET /[recurso]
def test_get_noticias_status_200(client):
    response = client.get('/noticias')
    assert response.status_code == 200

# TESTE 2 (Obrigatório): Validação estrutural do JSON retornado (campos obrigatórios)
def test_valida_estrutura_json_noticias(client):
    response = client.get('/noticias')
    dados = response.get_json()
    
    assert isinstance(dados, list)
    if len(dados) > 0:
        primeiro_registro = dados[0]
        # Garante que os campos essenciais de uma notícia comunitária existem
        assert "id" in primeiro_registro
        assert "titulo" in primeiro_registro
        assert "bairro" in primeiro_registro
        assert "conteudo" in primeiro_registro

# TESTE 3 (Obrigatório): Retorno HTTP 404 para um identificador inexistente em GET /[recurso]/{id}
def test_get_noticia_id_inexistente_404(client):
    response = client.get('/noticias/99999')  # ID visivelmente inexistente
    assert response.status_code == 404
    dados = response.get_json()
    assert "erro" in dados

# TESTE 4 (Autoria Própria): Validação semântica de integridade na rota /status
def test_get_status_integrity_and_version(client):
    """
    Teste de autoria própria: Verifica se a rota de status além de responder 200,
    retorna os metadados corretos de versão e estado operacional da infraestrutura.
    """
    response = client.get('/status')
    assert response.status_code == 200
    dados = response.get_json()
    assert dados["status"] == "operacional"
    assert dados["versao"] == "1.0.0"