from Models.step_model import StepModel
from flask import abort, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model

#######################################
#CRUD для типа мебели
#######################################
def read_all():
    out_objects = list(StepModel.select().dicts()) 
    return out_objects

def read_one(iden):
    check = StepModel.get_or_none(step_id=iden)
    if check is not None: 
        out_object = StepModel.select().where(StepModel.step_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object      
    else:
        abort(
            404, f"Step with id  {iden} not found"
        )

def create(person):
    iden = person.get("id")
    name = person.get("name")
    
    check = StepModel.get_or_none(step_id=iden)
    if check is None: 
        StepModel.create(step_id = iden,
                         step_name= name)
        out_object = StepModel.select().where(StepModel.step_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object, 201       
    else:
        abort(
            406,
            f"Step with name {name} can't be create",
        )
        
def update(iden, person):
    check = StepModel.get_or_none(step_id=iden)
    if check is not None:
        query = StepModel.update(step_name=person.get("name")).where(StepModel.step_id == iden)
        query.execute()
        out_object = StepModel.select().where(StepModel.step_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object   
    else:
        abort(
            404,
            f"Step with ID {iden} not found"
        )

def delete(iden):
    check = StepModel.get_or_none(step_id=iden)
    if check is not None:
        query = StepModel.delete().where(StepModel.step_id == iden)
        query.execute()
        return make_response(
            f"Step with {iden} successfully deleted", 204
        )
    else:
        abort(
            404,
            f"Step with ID {iden} not found"
        )