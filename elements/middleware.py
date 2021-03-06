# coding=utf-8
from django.utils.deprecation import MiddlewareMixin
import jwt
import json
from django.core.exceptions import PermissionDenied

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if JWTAuthenticationMiddleware.is_json(request.body):
            request._body = json.loads(request.body)

        if (request.method == 'OPTIONS') | request.path.startswith('/auth') | request.path.startswith('/api') | request.path.startswith('/space/create') | request.path.endswith('/authorize_user') | request.path.startswith('/favicon.ico'):
            return

        with open("public.pem") as key_file:
            try:
                claim = jwt.decode(request.headers.get('authorization'), key=key_file.read(), algorithms=['RS256'])
                request.claim = claim
                request.user_id = claim.get('user_id')
            except jwt.exceptions.DecodeError:
                raise PermissionDenied
        
        return

    @staticmethod
    def is_json(data):
        try:
            json_object = json.loads(data)
        except ValueError as e:
            return False
        return True

class CorsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET,PUT,POST,DELETE,PATCH,OPTIONS"
        response["Access-Control-Allow-Headers"] = "Origin, Content-Type, X-Auth-Token"
        return response