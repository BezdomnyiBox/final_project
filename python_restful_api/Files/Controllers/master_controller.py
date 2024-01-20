from Models.master_model import MasterModel
from flask import abort, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model

#######################################
#CRUD для мастера
#######################################
def read_all():
    users = list(MasterModel.select().dicts()) 
    #json_data = json.dumps(model_to_dict(users))
    return users

def read_one(iden):
    check = MasterModel.get_or_none(master_id=iden)
    if check is not None: 
        master = MasterModel.select().where(MasterModel.master_id == iden).get()
        master = model_to_dict(master)
        return master      
    else:
        abort(
            404, f"Master with id  {iden} not found"
        )

def create(person):
    iden = person.get("id")
    name = person.get("name")
    phone = person.get("phone")
    exp = person.get("exp")
    
    check = MasterModel.get_or_none(master_id=iden)
    if check is None: 
        MasterModel.create(master_id= iden,
                           master_name= name,
                           master_phone = phone,
                           master_exp = exp
                           )
        master = MasterModel.select().where(MasterModel.master_id == iden).get()
        master = model_to_dict(master)
        return master, 201       
    else:
        abort(
            406,
            f"Master with name {name} can't be create",
        )
        
def update(iden, person):
    check = MasterModel.get_or_none(master_id=iden)
    if check is not None:
        query = MasterModel.update(master_name=person.get("name"),
                                   master_phone=person.get("phone"),
                                   master_exp=person.get("exp")).where(MasterModel.master_id == iden)
        query.execute()
        master = MasterModel.select().where(MasterModel.master_id == iden).get()
        master = model_to_dict(master)
        return master   
    else:
        abort(
            404,
            f"Master with ID {iden} not found"
        )

def delete(iden):
    check = MasterModel.get_or_none(master_id=iden)
    if check is not None:
        query = MasterModel.delete().where(MasterModel.master_id == iden)
        query.execute()
        return make_response(
            f"Master with {iden} successfully deleted", 204
        )
    else:
        abort(
            404,
            f"Master with ID {iden} not found"
        )
