from flask import Flask
from flask import abort
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api


from modelos import db
from vistas import RegistrarEmail, ConsultarEmail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blacklist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
jwt = JWTManager(app)

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    abort(401)

@jwt.invalid_token_loader
def invalid_token_callback(error):
    abort(401)

@jwt.unauthorized_loader
def unauthorized_token_callback(error):
    abort(400)


api.add_resource(RegistrarEmail, '/blacklists')
api.add_resource(ConsultarEmail, '/blacklists/<email>')





