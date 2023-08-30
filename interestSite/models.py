

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from interestSite import app


db = SQLAlchemy()

class DataItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    current_date = db.Column(db.String(25), nullable=False)
    boi_interest = db.Column(db.String(5), nullable=False)
    next_date = db.Column(db.String(25), nullable=False)


db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()
