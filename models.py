from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Espaco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    loja = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(100), nullable=False)

def criar_e_popular_db():
    db.drop_all()
    db.create_all()

    espacos = [
        Espaco(nome="Display Entrada", status="ocupado", loja="TechHome Store", marca="Samsung"),
        Espaco(nome="Banner Central", status="disponível", loja="TechHome Store", marca="Apple"),
        Espaco(nome="Display Lateral", status="ocupado", loja="Eletrônica Center", marca="LG"),
        Espaco(nome="Totem Interativo", status="disponível", loja="Eletrônica Center", marca="Motorola"),
        Espaco(nome="Expositor Linha Branca", status="ocupado", loja="TechHome Store", marca="Electrolux")
    ]

    db.session.add_all(espacos)
    db.session.commit()
