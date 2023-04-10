from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.sql import func

db = SQLAlchemy()

class Blacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000), nullable=False)
    app_uuid = db.Column(db.String(1000), nullable=False)
    blocked_reason = db.Column(db.String(1000), nullable=False)
    ip_address = db.Column(db.String(1000), nullable=False)
    date_create = db.Column(db.DateTime,server_default=func.now())

class BlacklistSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Blacklist
        load_instance = True
