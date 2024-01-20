from Models.furniture_model import FurnitureModel
from flask import abort, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model

#######################################
#CRUD для мебели
#######################################
def read_all():
    out_objects = list(FurnitureModel.select().dicts()) 
    return out_objects

def read_one(iden):
    check = FurnitureModel.get_or_none(furniture_id=iden)
    if check is not None: 
        out_object = FurnitureModel.select().where(FurnitureModel.furniture_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object      
    else:
        abort(
            404, f"Furniture with ID {iden} not found"
        )

def create(person):
    iden = person.get("id")
    name = person.get("name")
    type_id = person.get("type_id")
    color_id = person.get("color_id")
    length = person.get("length")
    width = person.get("width")
    height = person.get("height")
    price = person.get("price")
    
    check = FurnitureModel.get_or_none(furniture_id=iden)
    if check is None: 
        FurnitureModel.create(furniture_id =iden,
                              furniture_name = name,
                              furniture_type = type_id,
                              furniture_color = color_id,
                              furniture_length = length,
                              furniture_width = width,
                              furniture_height = height,
                              furniture_price = price
                              )
        out_object = FurnitureModel.select().where(FurnitureModel.furniture_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object, 201       
    else:
        abort(
            406,
            f"Furniture with ID {iden} can't be create",
        )
        
def update(iden, person):
    check = FurnitureModel.get_or_none(furniture_id=iden)
    if check is not None:
        query = FurnitureModel.update(furniture_name=person.get("name"),
                                      furniture_type=person.get("type_id"),
                                      furniture_color=person.get("color_id"),
                                      furniture_length=person.get("length"),
                                      furniture_width=person.get("width"),
                                      furniture_height=person.get("height"),
                                      furniture_price=person.get("price")).where(FurnitureModel.furniture_id == iden)
        query.execute()
        out_object = FurnitureModel.select().where(FurnitureModel.furniture_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object   
    else:
        abort(
            404,
            f"Furniture with ID {iden} not found"
        )

def delete(iden):
    check = FurnitureModel.get_or_none(furniture_id=iden)
    if check is not None:
        query = FurnitureModel.delete().where(FurnitureModel.furniture_id == iden)
        query.execute()
        return make_response(
            f"Furniture with ID {iden} successfully deleted", 204
        )
    else:
        abort(
            404,
            f"Furniture with ID {iden} not found"
        )