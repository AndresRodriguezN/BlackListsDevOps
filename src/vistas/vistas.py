from flask import request,abort
from flask_restful import Resource
from modelos import db, Blacklist, BlacklistSchema
#from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity,get_jwt


blacklist_schema = BlacklistSchema()

class RegistrarEmail(Resource):
    
    def post(self):
    
        if request.json == None or not "email" in request.json or not "app_uuid" in request.json:
            return {"mensaje": "El correo no pudo ser registrado", "error":"el email y app_uuid son obligatorios"},400
        else:
            email = request.json["email"]
            app_uuid = request.json["app_uuid"]
            blocked_reason = request.json["blocked_reason"]

            if (not email) or (not app_uuid):
                return {"mensaje": "El correo no pudo ser registrado", "error":"el email y app_uuid son obligatorios"},400
            
            if len(blocked_reason)>255:
                return {"mensaje": "El correo no pudo ser registrado", "error":"El blocked_reason supera los 255 caracteres"},400  
           
            nueva_Blacklist = Blacklist(email = email, app_uuid = app_uuid , blocked_reason = blocked_reason, ip_address = request.remote_addr)
            db.session.add(nueva_Blacklist)
            db.session.commit()
            return {"mensaje": "El correo se ha registrado correctamente"},200
              
            
class ConsultarEmail(Resource):
    
    def get(self, email):
        resultado = Blacklist.query.filter(Blacklist.email == email).all()
        if len(resultado) == 0:
            return {"mensaje": "El correo no se encuentra en la lista negra"}, 200
        else:
            respuesta = {}
            for tarea in resultado:
                respuesta.update({"tarea":tarea.blocked_reason})
            return respuesta , 200
           

        