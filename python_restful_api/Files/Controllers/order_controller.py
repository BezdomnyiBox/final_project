from Models.order_model import OrderModel
from flask import abort, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model

#######################################
#CRUD для заказа мастера
#######################################
def read_all():
    out_objects = list(OrderModel.select().dicts()) 
    return out_objects

def read_one(iden):
    check = OrderModel.get_or_none(order_id=iden)
    if check is not None: 
        out_object = OrderModel.select().where(OrderModel.order_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object      
    else:
        abort(
            404, f"Order with ID {iden} not found"
        )

def create(person):
    iden = person.get("id")
    master_id = person.get("master_id")
    selling_id = person.get("selling_id")
    salary = person.get("salary")
    
    check = OrderModel.get_or_none(order_id=iden)
    if check is None: 
        OrderModel.create(order_id= iden,
                          master_id= master_id,
                          selling_id = selling_id,
                          salary = salary
                          )
        out_object = OrderModel.select().where(OrderModel.order_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object, 201       
    else:
        abort(
            406,
            f"Order with ID {iden} can't be create",
        )
        
def update(iden, person):
    check = OrderModel.get_or_none(order_id=iden)
    if check is not None:
        query = OrderModel.update(master_id=person.get("master_id"),
                                  selling_id=person.get("selling_id"),
                                  salary=person.get("salary")).where(OrderModel.order_id == iden)
        query.execute()
        out_object = OrderModel.select().where(OrderModel.order_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object   
    else:
        abort(
            404,
            f"Order with ID {iden} not found"
        )

def delete(iden):
    check = OrderModel.get_or_none(order_id=iden)
    if check is not None:
        query = OrderModel.delete().where(OrderModel.order_id == iden)
        query.execute()
        return make_response(
            f"Order with ID {iden} successfully deleted", 204
        )
    else:
        abort(
            404,
            f"Order with ID {iden} not found"
        )