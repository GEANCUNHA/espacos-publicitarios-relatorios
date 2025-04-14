from app import app
from models import db, criar_e_popular_db

if __name__ == "__main__":
    with app.app_context():
        criar_e_popular_db()
        print("✅ Banco criado e populado com sucesso.")

    app.run(host="0.0.0.0", port=5000)
