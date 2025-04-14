from flask import Flask, jsonify
from models import db, Espaco
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relatorios.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Swagger UI config
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # Manteremos, mas certifique-se que o arquivo está sendo servido

swagger_ui = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Relatórios de Espaços"}
)

app.register_blueprint(swagger_ui, url_prefix=SWAGGER_URL)

# Rotas da API
@app.route("/relatorios/status")
def relatorio_status():
    total = Espaco.query.count()
    disponiveis = Espaco.query.filter_by(status="disponível").count()
    ocupados = total - disponiveis
    return jsonify({"total": total, "disponíveis": disponiveis, "ocupados": ocupados})

@app.route("/relatorios/lojas")
def relatorio_por_loja():
    resultados = db.session.query(Espaco.loja, db.func.count(Espaco.id)).group_by(Espaco.loja).all()
    return jsonify({loja: total for loja, total in resultados})

@app.route("/relatorios/marcas")
def relatorio_por_marca():
    resultados = db.session.query(Espaco.marca, db.func.count(Espaco.id)).group_by(Espaco.marca).all()
    return jsonify({marca: total for marca, total in resultados})

@app.route("/relatorios/geral")
def relatorio_geral():
    status = relatorio_status().get_json()
    por_loja = relatorio_por_loja().get_json()
    por_marca = relatorio_por_marca().get_json()
    return jsonify({
        "status": status,
        "por_loja": por_loja,
        "por_marca": por_marca
    })
