from flask import Flask
from flask import abort
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api


from src.modelos import db
from src.vistas import RegistrarEmail, ConsultarEmail, ObtenerToken

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blacklist.db'
#application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:clave1234@blacklists.cz0quxuty3ze.us-east-1.rds.amazonaws.com/emails'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['JWT_SECRET_KEY'] = 'frase-secreta'
application.config['PROPAGATE_EXCEPTIONS'] = True

app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()

cors = CORS(application)

api = Api(application)
jwt = JWTManager(application)

@jwt.invalid_token_loader
def invalid_token_callback(error):
    abort(401)

@jwt.unauthorized_loader
def unauthorized_token_callback(error):
    abort(400)


api.add_resource(ObtenerToken, '/')
api.add_resource(RegistrarEmail, '/blacklists')
api.add_resource(ConsultarEmail, '/blacklists/<email>')





