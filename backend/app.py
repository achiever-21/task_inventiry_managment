from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Register Routes
    from routes import product_routes, user_routes, supplier_routes
    app.register_blueprint(product_routes.bp)
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(supplier_routes.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
