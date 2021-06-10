import os, datetime, time
import library.db_utils as db_utils
import app.sequence.service as sequence_service
import app.role.service as role_service
from bson.objectid import ObjectId

domain = 'document'

def find(request):
    documentList = db_utils.find(domain, {'createdBy': request.user_id})
    return 200, {'data': documentList}

def update(request, data):
    new_record = False
    updated_record = db_utils.upsert(domain, data, request.user_id)
    return 200, {'data': updated_record}

def delete(request, id):
    result = db_utils.delete(domain, {'createdBy': request.user_id, '_id': id}, request.user_id)
    return 200, {'deleted_count': result.deleted_count}

def find_by_id(request, id):
    documentList = db_utils.find(domain, {'createdBy': request.user_id, '_id': id})
    return 200, {'data': documentList}
