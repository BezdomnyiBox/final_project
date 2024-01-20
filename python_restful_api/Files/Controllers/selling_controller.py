from Models.selling_model import SellingModel
from flask import abort, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model

#######################################
#CRUD для продажи
#######################################
def read_all():
    out_objects = list(SellingModel.select().dicts()) 
    return out_objects

def read_one(iden):
    check = SellingModel.get_or_none(selling_id=iden)
    if check is not None: 
        out_object = SellingModel.select().where(SellingModel.selling_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object      
    else:
        abort(
            404, f"Selling with ID {iden} not found"
        )

def create(person):
    iden = person.get("id")
    contract_id = person.get("contract_id")
    furniture_id = person.get("furniture_id")
    count = person.get("count")
    
    check = SellingModel.get_or_none(selling_id=iden)
    if check is None: 
        SellingModel.create(selling_id = iden,
                            contract_id= contract_id,
                            furniture_id = furniture_id,
                            count = count
                            )
        out_object = SellingModel.select().where(SellingModel.selling_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object, 201       
    else:
        abort(
            406,
            f"Selling with ID {iden} can't be create",
        )
        
def update(iden, person):
    check = SellingModel.get_or_none(selling_id=iden)
    if check is not None:
        query = SellingModel.update(contract_id=person.get("contract_id"),
                                    furniture_id=person.get("furniture_id"),
                                    count=person.get("count")).where(SellingModel.selling_id == iden)
        query.execute()
        out_object = SellingModel.select().where(SellingModel.selling_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object   
    else:
        abort(
            404,
            f"Selling with ID {iden} not found"
        )

def delete(iden):
    check = SellingModel.get_or_none(selling_id=iden)
    if check is not None:
        query = SellingModel.delete().where(SellingModel.selling_id == iden)
        query.execute()
        return make_response(
            f"Selling with ID {iden} successfully deleted", 204
        )
    else:
        abort(
            404,
            f"Selling with ID {iden} not found"
        )