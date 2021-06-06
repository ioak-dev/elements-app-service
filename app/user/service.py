import os, datetime, time
import library.db_utils as db_utils
from bson.objectid import ObjectId

domain = 'user'
domain_role_permissions = 'role_permissions'

def find(request):
    data = find_by_user_id(request.user_id)
    return (200, {'data': data})

def find_all(request):
    data = db_utils.find(domain, {})
    return (200, {'data': data})

def expand_authors(data):
    for item in data:
        last_modified_by = db_utils.find(domain, {'_id': item.get('lastModifiedBy')})
        created_by = db_utils.find(domain, {'_id': item.get('createdBy')})
        item['lastModifiedByEmail'] = last_modified_by[0].get('email')
        item['createdByEmail'] = created_by[0].get('email')
    return data

def do_update_user(request):
    updated_record = update_user(request.body, request.user_id)
    return (200, {'data': updated_record})

def find_permitted_actions(user_id):
    roles = db_utils.find(domain, {'_id': user_id})[0].get('roles')
    roles.append('open')
    return db_utils.find(domain_role_permissions, {'role': {'$in': roles}})

def find_by_user_id(user_id):
    return db_utils.find(domain, {'_id': user_id})

def update_user(data, user_id=None):
    return db_utils.upsert(domain, data, user_id)

def insert_user(data, user_id=None):
    data['_id'] = ObjectId(data['_id'])
    return db_utils.insert(domain, data, user_id)

def is_first_user():
    data = db_utils.find(domain, {})
    if len(data) == 0:
        return True
    else:
        return False
