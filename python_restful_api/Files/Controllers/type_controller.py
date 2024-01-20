from Models.type_model import TypeModel
from flask import abort, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model

#######################################
#CRUD для типа мебели
#######################################
def read_all():
    out_objects = list(TypeModel.select().dicts()) 
    return out_objects

def read_one(iden):
    check = TypeModel.get_or_none(type_id=iden)
    if check is not None: 
        out_object = TypeModel.select().where(TypeModel.type_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object      
    else:
        abort(
            404, f"Type with id  {iden} not found"
        )

def create(person):
    iden = person.get("id")
    name = person.get("name")
    
    check = TypeModel.get_or_none(type_id=iden)
    if check is None: 
        TypeModel.create(type_id = iden,
                         type_name = name)
        out_object = TypeModel.select().where(TypeModel.type_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object, 201       
    else:
        abort(
            406,
            f"Type with name {name} can't be create",
        )
        
def update(iden, person):
    check = TypeModel.get_or_none(type_id=iden)
    if check is not None:
        query = TypeModel.update(type_name=person.get("name")).where(TypeModel.type_id == iden)
        query.execute()
        out_object = TypeModel.select().where(TypeModel.type_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object   
    else:
        abort(
            404,
            f"Type with ID {iden} not found"
        )

def delete(iden):
    check = TypeModel.get_or_none(type_id=iden)
    if check is not None:
        query = TypeModel.delete().where(TypeModel.type_id == iden)
        query.execute()
        return make_response(
            f"Type with {iden} successfully deleted", 204
        )
    else:
        abort(
            404,
            f"Type with ID {iden} not found"
        )