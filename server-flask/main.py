from flask import Flask
from app.database import db
from app.controllers.excel_loader import load_excel_data
from app.properties.data import name, password, server, database

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{name}:{password}@{server}/{database}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

        # Ejecutar la migración de Excel -> DB
        load_excel_data("app/data/areas.xls", "app/data/articulos.xls")

    return app

app = create_app()
