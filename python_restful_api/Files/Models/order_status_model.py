from peewee import *
from Models.base_model import BaseModel
from Models.order_model import OrderModel
from Models.step_model import StepModel

class OrderStatusModel(BaseModel):
       order_status_id = AutoField(column_name='order_status_id')
       order_id = ForeignKeyField(OrderModel, to_field='order_id')
       order_status = ForeignKeyField(StepModel, to_field='step_id')
       check_date = DateField(column_name='check_date', null=True)
       
       class Meta:
              table_name = 'order_status'