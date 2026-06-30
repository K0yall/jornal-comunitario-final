import os
import json
from flask import Flask, jsonify
from flask_cors import CORS  # <-- Adiciona esta linha

app = Flask(__name__)
CORS(app)  # <-- Adiciona esta linha para libertar o acesso ao Frontend

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'noticias.json')

def carregar_dados():
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Arquivo de dados não encontrado em: {DATA_FILE}")
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "nome": "API de Infraestrutura para Jornal Comunitário",
        "versao": "1.0.0",
        "status": "operacional"
    }), 200

@app.route('/noticias', methods=['GET'])
def get_noticias():
    try:
        dados = carregar_dados()
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"erro": "Erro interno ao carregar notícias", "detalhes": str(e)}), 500

@app.route('/noticias/<int:noticia_id>', methods=['GET'])
def get_noticia_por_id(noticia_id):
    try:
        dados = carregar_dados()
        noticia = next((item for item in dados if item["id"] == noticia_id), None)
        if noticia:
            return jsonify(noticia), 200
        return jsonify({"erro": f"Notícia com ID {noticia_id} não encontrada"}), 404
    except Exception as e:
        return jsonify({"erro": "Erro interno no servidor", "detalhes": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)