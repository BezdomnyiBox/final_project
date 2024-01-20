from peewee import *
from Models.base_model import BaseModel
from Models.master_model import MasterModel
from Models.selling_model import SellingModel

class OrderModel(BaseModel):
       order_id = AutoField(column_name='order_id')
       master_id = ForeignKeyField(MasterModel, to_field='master_id')
       selling_id = ForeignKeyField(SellingModel, to_field='selling_id')
       salary = IntegerField(column_name='salary', null=True)   

       class Meta:
              table_name = 'orders'