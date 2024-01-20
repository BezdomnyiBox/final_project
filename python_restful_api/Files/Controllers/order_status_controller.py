from Models.order_status_model import OrderStatusModel
from flask import abort, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model

#######################################
#CRUD для состояния заказа
#######################################
def read_all():
    out_objects = list(OrderStatusModel.select().dicts()) 
    return out_objects

def read_one(iden):
    check = OrderStatusModel.get_or_none(order_status_id=iden)
    if check is not None: 
        out_object = OrderStatusModel.select().where(OrderStatusModel.order_status_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object      
    else:
        abort(
            404, f"Order status with ID {iden} not found"
        )

def create(person):
    iden = person.get("id")
    order_id = person.get("order_id")
    order_status = person.get("order_status")
    check_date = person.get("check_date")
    
    check = OrderStatusModel.get_or_none(order_status_id=iden)
    if check is None: 
        OrderStatusModel.create(order_status_id = iden,
                                order_id = order_id,
                                order_status = order_status,
                                check_date = check_date
                                )
        out_object = OrderStatusModel.select().where(OrderStatusModel.order_status_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object, 201       
    else:
        abort(
            406,
            f"Order status with ID {iden} can't be create",
        )
        
def update(iden, person):
    check = OrderStatusModel.get_or_none(order_status_id=iden)
    if check is not None:
        query = OrderStatusModel.update(order_id=person.get("order_id"),
                                        order_status=person.get("order_status"),
                                        check_date=person.get("check_date")).where(OrderStatusModel.order_status_id == iden)
        query.execute()
        out_object = OrderStatusModel.select().where(OrderStatusModel.order_status_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object   
    else:
        abort(
            404,
            f"Order status with ID {iden} not found"
        )

def delete(iden):
    check = OrderStatusModel.get_or_none(order_status_id=iden)
    if check is not None:
        query = OrderStatusModel.delete().where(OrderStatusModel.order_status_id == iden)
        query.execute()
        return make_response(
            f"Order status with ID {iden} successfully deleted", 204
        )
    else:
        abort(
            404,
            f"Order status with ID {iden} not found"
        )