from Models.color_model import ColorModel
from flask import abort, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model

#######################################
#CRUD для цвета мебели
#######################################
def read_all():
    out_objects = list(ColorModel.select().dicts()) 
    return out_objects

def read_one(iden):
    check = ColorModel.get_or_none(color_id=iden)
    if check is not None: 
        out_object = ColorModel.select().where(ColorModel.color_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object      
    else:
        abort(
            404, f"Color with id  {iden} not found"
        )

def create(person):
    iden = person.get("id")
    name = person.get("name")
    
    check = ColorModel.get_or_none(color_id=iden)
    if check is None: 
        ColorModel.create(color_id = iden,
                          color_name= name)
        out_object = ColorModel.select().where(ColorModel.color_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object, 201       
    else:
        abort(
            406,
            f"Color with name {name} can't be create",
        )
        
def update(iden, person):
    check = ColorModel.get_or_none(color_id=iden)
    if check is not None:
        query = ColorModel.update(color_name=person.get("name")).where(ColorModel.color_id == iden)
        query.execute()
        out_object = ColorModel.select().where(ColorModel.color_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object   
    else:
        abort(
            404,
            f"Color with ID {iden} not found"
        )

def delete(iden):
    check = ColorModel.get_or_none(color_id=iden)
    if check is not None:
        query = ColorModel.delete().where(ColorModel.color_id == iden)
        query.execute()
        return make_response(
            f"Color with {iden} successfully deleted", 204
        )
    else:
        abort(
            404,
            f"Color with ID {iden} not found"
        )