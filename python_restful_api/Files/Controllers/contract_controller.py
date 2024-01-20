from Models.contract_model import ContractModel
from flask import abort, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model

#######################################
#CRUD для договора
#######################################
def read_all():
    out_objects = list(ContractModel.select().dicts()) 
    return out_objects

def read_one(iden):
    check = ContractModel.get_or_none(contract_id=iden)
    if check is not None: 
        out_object = ContractModel.select().where(ContractModel.contract_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object      
    else:
        abort(
            404, f"Contract with ID {iden} not found"
        )

def create(person):
    iden = person.get("id")
    client_id = person.get("client_id")
    date_1 = person.get("date_1")
    date_2 = person.get("date_2")
    
    check = ContractModel.get_or_none(contract_id=iden)
    if check is None: 
        ContractModel.create(contract_id= iden,
                             client_id= client_id,
                             check_in_date = date_1,
                             check_out_date = date_2
                             )
        out_object = ContractModel.select().where(ContractModel.contract_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object, 201       
    else:
        abort(
            406,
            f"Contract with ID {iden} can't be create",
        )
        
def update(iden, person):
    check = ContractModel.get_or_none(contract_id=iden)
    if check is not None:
        query = ContractModel.update(client_id=person.get("client_id"),
                                     check_in_date=person.get("date_1"),
                                     check_out_date=person.get("date_2")).where(ContractModel.contract_id == iden)
        query.execute()
        out_object = ContractModel.select().where(ContractModel.contract_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object   
    else:
        abort(
            404,
            f"Contract with ID {iden} not found"
        )

def delete(iden):
    check = ContractModel.get_or_none(contract_id=iden)
    if check is not None:
        query = ContractModel.delete().where(ContractModel.contract_id == iden)
        query.execute()
        return make_response(
            f"Contract with ID {iden} successfully deleted", 204
        )
    else:
        abort(
            404,
            f"Contract with ID {iden} not found"
        )