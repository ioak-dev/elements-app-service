from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.core import serializers
import app.document.service as service

@api_view(['GET', 'PUT'])
def get_update_document(request):
    if request.method == 'GET':
        response = service.find(request)
        return JsonResponse(response[1], status=response[0])
    if request.method == 'PUT':
        response = service.update(request, request.body)
        return JsonResponse(response[1], status=response[0])
    
@api_view(['DELETE'])
def delete_document(request, id):
    if request.method == 'DELETE':
        response = service.delete(request, id)
        return JsonResponse(response[1], status=response[0])

@api_view(['GET'])
def get_by_id(request, id):
    if request.method == 'GET':
        response = service.find_by_id(request, id)
        return JsonResponse(response[1], status=response[0])
