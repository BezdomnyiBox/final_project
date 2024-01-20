from Models.client_model import ClientModel
from flask import abort, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model

#######################################
#CRUD для клиента
#######################################
def read_all():
    out_objects = list(ClientModel.select().dicts()) 
    return out_objects

def read_one(iden):
    check = ClientModel.get_or_none(client_id=iden)
    if check is not None: 
        out_object = ClientModel.select().where(ClientModel.client_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object      
    else:
        abort(
            404, f"Client with id  {iden} not found"
        )

def create(person):
    iden = person.get("id")
    name = person.get("name")
    phone = person.get("phone")
    address = person.get("address")
    
    check = ClientModel.get_or_none(client_id=iden)
    if check is None: 
        ClientModel.create(client_id = iden,
                           client_name= name,
                           client_phone = phone,
                           client_address = address
                           )
        out_object = ClientModel.select().where(ClientModel.client_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object, 201       
    else:
        abort(
            406,
            f"Client with name {name} can't be create",
        )
        
def update(iden, person):
    check = ClientModel.get_or_none(client_id=iden)
    if check is not None:
        query = ClientModel.update(client_name=person.get("name"),
                                   client_phone=person.get("phone"),
                                   client_address=person.get("address")).where(ClientModel.client_id == iden)
        query.execute()
        out_object = ClientModel.select().where(ClientModel.client_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object   
    else:
        abort(
            404,
            f"Client with ID {iden} not found"
        )

def delete(iden):
    check = ClientModel.get_or_none(client_id=iden)
    if check is not None:
        query = ClientModel.delete().where(ClientModel.client_id == iden)
        query.execute()
        return make_response(
            f"Client with {iden} successfully deleted", 204
        )
    else:
        abort(
            404,
            f"Client with ID {iden} not found"
        )