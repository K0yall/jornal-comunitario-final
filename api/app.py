import os
import json
from flask import Flask, jsonify

app = Flask(__name__)

# Define o caminho para o arquivo JSON de dados simulados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'noticias.json')

def carregar_dados():
    """Função auxiliar para ler o arquivo JSON externo."""
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Arquivo de dados não encontrado em: {DATA_FILE}")
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# 1. Rota GET /status - Saúde da aplicação
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "nome": "API de Infraestrutura para Jornal Comunitário",
        "versao": "1.0.0",
        "status": "operacional"
    }), 200

# 2. Rota GET /noticias - Retorna todos os registros
@app.route('/noticias', methods=['GET'])
def get_noticias():
    try:
        dados = carregar_dados()
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"erro": "Erro interno ao carregar notícias", "detalhes": str(e)}), 500

# 3. Rota GET /noticias/{id} - Retorna um único registro por ID
@app.route('/noticias/<int:noticia_id>', methods=['GET'])
def get_noticia_por_id(noticia_id):
    try:
        dados = carregar_dados()
        # Busca a notícia correspondente ao ID informado
        noticia = next((item for item in dados if item["id"] == noticia_id), None)
        
        if noticia:
            return jsonify(noticia), 200
        
        # Retorno HTTP 404 semântico caso não encontre
        return jsonify({"erro": f"Notícia com ID {noticia_id} não encontrada"}), 404
    except Exception as e:
        return jsonify({"erro": "Erro interno no servidor", "detalhes": str(e)}), 500

if __name__ == '__main__':
    # Executa a aplicação localmente na porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)